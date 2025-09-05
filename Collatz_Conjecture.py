class Collatz_Conjecture: #3N + 1 Conjecture
    def __init__(self,num):
        self.num = num
        self.num_list = []

    def lists(self):
        number = self.num
        is_running = True
        while is_running:
            self.num_list.append(number)
            if number == 1:
                is_running = False
            elif number%2 == 0:
                number = int(number/2)
            else:
                number = int((number*3)+1)
        return self.num_list

    def length(self):
        self.lists()
        return len(self.num_list)

def main():  
    running = True
    while running:
        number = int(input("Enter A Number :  "))
        option = input("1: Length of Conjecture\n2: Lists of Numbers\nENTER HERE--->  ")
        num_1 = Collatz_Conjecture(number)

        if option.strip() == "1":
            print(num_1.length())

        elif option.strip() =="2":
            print(num_1.lists())
        user = input("Enter anything to ask again, Q to Quit :  ")
        if user.lower() == 'q':
            print("BYE")
            running = False

if __name__ == '__main__':
    main()