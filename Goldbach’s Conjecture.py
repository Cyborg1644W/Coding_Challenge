#Statement: Every even number greater than 2 is the sum of two prime numbers.
# 📌 You can write code that:
# Takes an even number as input
# Finds two primes that sum up to it
import math
import time

def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, int(math.sqrt(number))+1):
        if number % num == 0:
            return False
    return True

def Goldbach_Conjecture(number):
    answers = {}
    for i in range(number):
        if is_prime(i):
            new_num = number - i 
            if is_prime(new_num):
                answers[i] = new_num
    return answers

def main():
    try: 
        user_input = int(input("What even number :  "))
        if user_input % 2 != 0:
            print("Even number Only")
        elif user_input < 1:
            print("Enter positive number only")
        else:
            answer = Goldbach_Conjecture(user_input)
            time.sleep(.1)
    except Exception:
        print("Please Enter A Number")
    main()

if __name__ == '__main__':
    main()