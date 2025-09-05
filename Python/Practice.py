numbers = int(input("Enter a Number:    "))

while not numbers == 'q':
    for n in range(2,int(numbers)):
        if int(numbers)%n == 0:
            print(f"{numbers} is NOT a Prime Number")
            numbers = input("Enter another Number (q to quit):    ")
            break
        elif not int(numbers)%n == 0:
            print(f"{numbers} is a Prime Number")
            numbers = input("Enter another Number (q to quit):    ")
            break