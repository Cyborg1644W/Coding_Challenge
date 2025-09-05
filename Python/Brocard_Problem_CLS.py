#n!+1=m² without using math module

class Brocard:
    def __init__(self,num):
        self.num = num

    def find_n(self):
        Nth = (self.num-1)
        divisor = 2
        while Nth != 1:
            Nth = Nth/divisor
            divisor +=1
        return divisor-1

    def find_m(self):
        factorial = self.num +1
        current_num = 1
        for i in range(2,factorial):
            current_num = current_num * i 
        answer = (current_num + 1) ** 0.5
        return answer

def main():
    is_running = True   
    while is_running:
        user_choice = input("brocard's Problem (n!+1=m²)  \nType 'N' to find n, 'M' to find M :   ")
        user_num = int(input("Enter a Number :  "))
        number = Brocard(user_num) 
        if user_choice.lower() == 'n':
            print(f"N is equal to {number.find_n()}!")
        elif user_choice.lower() == 'm':
            print(f"M is equal to {number.find_m()}")

if __name__ == '__main__':
    main()