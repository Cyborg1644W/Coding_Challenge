import math
import random

def solve_hyp(a, b):
    return math.sqrt((a ** 2) + (b ** 2))

def solve_nhyp(c, a):
    return math.sqrt((c ** 2) - (a ** 2))

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")

def solve_discriminant(A,B,C):
    return (B**2)-(4*A*C)


def pythagorean():
    while True:
        user = input("Solving for hypotenuse? (Y/n): ").strip().upper()
        if user == 'Y':
            leg_1 = get_number("Value of leg 1: ")
            leg_2 = get_number("Value of leg 2: ")
            print(f"Answer: {solve_hyp(leg_1, leg_2)}")
        elif user == 'N':
            hyp = get_number("Value of hypotenuse: ")
            leg = get_number("Value of leg: ")
            print(f"Answer: {solve_nhyp(hyp, leg)}")
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")
            continue

        ask = input("Do you want to solve again? (Y/n): ").strip().upper()
        if ask != 'Y':
            break

def disciminant():
    while True:
        A = get_number("What's the value of A:  ")
        B = get_number("What's the value of B:  ")
        C = get_number("What's the value of C:  ")
        print(f"The Answer is {solve_discriminant(A,B,C)}")

        ask = input("Do you want to solve again? (Y/n): ").strip().upper()
        if ask != 'Y':
            break

def main():
    calc = get_number("solve for \n\t1:discriminant\n\t2:hypothenuse\n")
    if calc == 1:
        disciminant()
    elif calc == 2:
        pythagorean()

if __name__ == '__main__':
    main()