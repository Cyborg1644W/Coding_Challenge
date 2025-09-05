import random
words = ("banana", "bottle", "camera", "carpet", "castle", "cheese", "circle", "cotton", "doctor", "donkey",
    "drawer", "engine", "farmer", "father", "finger", "flower", "forest", "friend", "garden", "guitar",
    "hammer", "hanger", "hunger", "island", "jacket", "jungle", "kitten", "ladder", "laptop", "lawyer",
    "letter", "magnet", "market", "marker", "monkey", "mother", "napkin", "number", "orange", "packet",
    "pencil", "pepper", "pickle", "pirate", "planet", "pocket", "rabbit", "remote", "rocket", "rubber",
    "runner", "school", "screen", "singer", "silver", "simple", "sister", "sketch", "slipper", "soccer",
    "spider", "spoon", "spring", "square", "straws", "sweater", "tablet", "ticket", "tomato", "toilet",
    "tunnel", "turtle", "vacuum", "violin", "walnut", "wallet", "window", "winner", "yellow", "zipper",
    "animal", "beacon", "butter", "candle", "circle", "clover", "cotton", "danger", "desert", "dinner",
    "dragon", "eagle", "effect", "energy", "family", "forest", "galaxy", "garage", "golden", "ground")

life = {0:'❤️ ❤️ ❤️ ❤️ ❤️', 
        1:'❤️ ❤️ ❤️ ❤️',
        2:'❤️ ❤️ ❤️',
        3:'❤️ ❤️',
        4:'❤️',
        5:'💔 You LOSE'}

def display_life(wrong_guess)  :
    for heart in life[wrong_guess]:
        print(heart, end = '')
    print()
    
def hide_word(hint):
    print(" ".join(hint))

    
def reveal(answer):
    print(" ".join(answer))

def main():
    random_word = random.choice(words)
    hint = ['_ '] * len(random_word)
    wrong_guess = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_life(wrong_guess)
        hide_word(hint)
        guess = input("Enter a Letter:  ").lower()
        
        if guess in guessed_letters:
            wrong_guess += 1
            print("Already Guessed")
            
        elif len(guess) != 1 or not guess.isalpha:
            print("Invalid Input")
            wrong_guess += 1
            
        elif guess not in random_word:   
            print("Try Again   ") 
            wrong_guess += 1
            
        elif guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    hint[i] = guess 
        guessed_letters.add(guess)
        
        if wrong_guess == 5:
            print(f"{random_word} is the answer, YOU LOSE")
            is_running = False
            
        elif "_ " not in hint:
            display_life(wrong_guess)
            reveal(random_word)
            print(f"{random_word} is The Correct word, YOU WIN!")
            is_running = False
            
if __name__ == '__main__':
    main()