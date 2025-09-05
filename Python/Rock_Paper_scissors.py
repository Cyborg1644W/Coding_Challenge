import random

choices = ("Rock", "Paper", "Scissor")
player_loss = 0
computer_loss = 0

life = {
    0: '❤️ ❤️ ❤️ ❤️ ❤️',
    1: '❤️ ❤️ ❤️ ❤️',
    2: '❤️ ❤️ ❤️',
    3: '❤️ ❤️',
    4: '❤️',
    5: '💔'
}

def display_life(): 
    print(f"""
    Player   : {life[player_loss]}
    Computer : {life[computer_loss]}
    """)

def continue_playing():
    choice = input("Enter anything to continue, or 'Q' to quit:\n---> ")
    return choice.lower().strip() != 'q'

def computer_move():
    return random.choice(choices)

def main():
    global player_loss, computer_loss
    print("-- ROCK - PAPER - SCISSOR --")

    playing = True
    while playing:
        player_loss = 0
        computer_loss = 0
        display_life()

        while player_loss < 5 and computer_loss < 5:
            player_input = input(f"{choices} (R/P/S)\n---> ").lower().strip()
            move_map = {'r': 'Rock', 'p': 'Paper', 's': 'Scissor'}

            if player_input not in move_map:
                print("Invalid Input! Please enter R, P, or S.\n")
                continue

            player = move_map[player_input]
            comp = computer_move()

            print(f"\nYou chose: {player}")
            print(f"Computer chose: {comp}")

            if player == comp:
                print("It's a TIE!")
            elif (player == "Rock" and comp == "Scissor") or \
                 (player == "Paper" and comp == "Rock") or \
                 (player == "Scissor" and comp == "Paper"):
                print("-- YOU WIN! --")
                computer_loss += 1
            else:
                print("-- YOU LOSE --")
                player_loss += 1

            display_life()

        playing = continue_playing()

if __name__ == '__main__':
    main()
