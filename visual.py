import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import time
import pyautogui

# Initialize Mediapipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize system volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
min_vol, max_vol = volume.GetVolumeRange()[:2]  # Volume range

# Variables for state management
last_volume_change = time.time()
volume_cooldown = 0.3  # Cooldown for volume control
is_playing = False  # Media playback state

# Function to count fingers
def count_fingers(landmarks):
    fingers = [False, False, False, False, False]  # [Thumb, Index, Middle, Ring, Pinky]
    hand_orientation = landmarks[5].x > landmarks[17].x  # Right hand or left hand
    
    # Thumb detection
    if hand_orientation:
        fingers[0] = landmarks[4].x < landmarks[2].x
    else:
        fingers[0] = landmarks[4].x > landmarks[2].x
    
    # Other fingers: Tip is above the PIP joint
    for i, tip_idx in enumerate([8, 12, 16, 20]):
        fingers[i + 1] = landmarks[tip_idx].y < landmarks[tip_idx - 2].y
    
    return fingers

# Function to detect gesture based on fingers raised
def detect_gesture(fingers):
    if fingers[0] and not any(fingers[1:]):  # Only Thumb
        return "Thumb"
    elif not any(fingers):  # All fingers are down
        return "Fist"
    elif all(fingers):  # All fingers are up
        return "Palm"
    elif fingers[1] and not any(fingers[2:]):  # Only Index Finger
        return "Pointing"
    return None

# Function to control volume based on gestures
def control_volume(landmarks):
    global last_volume_change

    current_time = time.time()
    if current_time - last_volume_change < volume_cooldown:
        return  # Enforce cooldown
    
    index_tip = landmarks[8].y
    index_pip = landmarks[6].y
    thumb_tip = landmarks[4].y
    thumb_mcp = landmarks[2].y
    
    current_volume = volume.GetMasterVolumeLevel()
    
    # Volume up: Index finger up
    if index_tip < index_pip:
        new_volume = min(current_volume + 2, max_vol)
        volume.SetMasterVolumeLevel(new_volume, None)
        print("Volume Up")

    # Volume down: Thumb up
    elif thumb_tip < thumb_mcp:
        new_volume = max(current_volume - 2, min_vol)
        volume.SetMasterVolumeLevel(new_volume, None)
        print("Volume Down")
    
    last_volume_change = current_time

# Function to control media playback
def control_media_playback(gesture):
    global is_playing
    
    if gesture == "Palm":
        # Play media
        if not is_playing:
            pyautogui.press('playpause')
            print("Playing")
            is_playing = True
    elif gesture == "Fist":
        # Pause media
        if is_playing:
            pyautogui.press('playpause')
            print("Paused")
            is_playing = False

# Main function to run the program
def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not access webcam.")
        return

    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            # Convert BGR to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Process the frame
            results = hands.process(image)

            # Convert RGB back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw landmarks
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS
                    )

                    # Count fingers and detect gestures
                    fingers = count_fingers(hand_landmarks.landmark)
                    gesture = detect_gesture(fingers)

                    # Gesture-based actions
                    if gesture in ["Palm", "Fist"]:
                        control_media_playback(gesture)
                    elif gesture in ["Thumb", "Pointing"]:
                        control_volume(hand_landmarks.landmark)

            # Show the video feed without text
            cv2.imshow("Hand Gesture Control", image)

            # Exit loop on pressing 'q'
            if cv2.waitKey(5) & 0xFF == ord('q'):
                print("Exiting...")
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

