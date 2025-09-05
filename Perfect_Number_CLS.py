class P_number:
    def __init__(self, number):
        self.number = number
        self.list = []
        
    def Divisor(self):
        try:
            self.list.clear()
            for num in range(1, self.number + 1):
                if self.number % num == 0:
                    if num not in self.list:
                        self.list.append(num)
                    quotient = int(self.number/num)
                    if quotient not in self.list:
                        self.list.append(quotient)
            self.list.remove(self.number)
            self.list.sort()
            return self.list
        except ValueError:
            return f"{self.number} is not valid, Please enter a possitive number"

    def Perfect_number(self):
        
        total_num = 0
        for number in self.list:
            total_num += number
        if total_num == self.number:
            return f"{self.number} is a perfect number"
        else:
            return f"{self.number} is not a perfect number"           
    
def main():
    is_running = True
    while is_running:
        try:
            user = input("What Number:  ")
            number = P_number(int(user))
            print(number.Divisor())
            print(number.Perfect_number())
        except ValueError:
            print("Please enter postive integers only")

    
if __name__ == '__main__':
    main()