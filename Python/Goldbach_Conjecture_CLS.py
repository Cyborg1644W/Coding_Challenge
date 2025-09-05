#Statement: Every even number greater than 2 is the sum of two prime numbers.
# 📌 You can write code that:
# Takes an even number as input
# Finds two primes that sum up to it
import math

class Goldbach:
    def __init__(self, number):
        self.number = number
        self.done_num = {}
        
    def __str__(self):
        result_lines = []
        for key, value in self.done_num.items():
            result_lines.append(f"{key} + {value}")
        return "\n".join(result_lines)
    
    def count(self):
        return len(self.done_num)
        
    def is_prime(number):
        if number <= 1:
            return False
        for num in range(2, int(math.sqrt(number))+1):
            if number % num == 0:
                return False
        return True
    

    def Goldbach_Conjecture(self):
        done = []
        for i in range(self.number):
            if Goldbach.is_prime(i):
                new_num = self.number - i
                if new_num in done or i in done:
                    continue
                done.append(i)
                done.append(new_num)
                if Goldbach.is_prime(new_num):
                    self.done_num[i] = new_num
        done.clear()
        return self.done_num

def main():
    is_running = True
    user = input("What Number: ")
    while is_running:
        numb = Goldbach(int(user))
        numb.Goldbach_Conjecture()
        print(numb)
        print(f"Total pair count is : {numb.count():,}")
        user = input(f"What Number (Q to Quit): ")
        if user.lower() == 'q':
            is_running = False

if __name__ == '__main__':
    main()