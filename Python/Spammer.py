import pyautogui
import time

message = "TEXT DITO"  # Message to spam
count = 10  # How many times to send
delay = 0.3  # Delay between messages in seconds

print("You have 5 seconds to click the chatbox...")
time.sleep(5)  # Time to click into the message input box

for i in range(count):
    pyautogui.write(message)
    pyautogui.press("enter")
    time.sleep(delay)   