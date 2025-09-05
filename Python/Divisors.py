def Find_Divisors(number):
    divisors = []
    
    for i in range(1, number + 1):
        if number % i == 0:
            new_num = number // i  
            if i not in divisors:
                divisors.append(i)
            if new_num not in divisors:
                divisors.append(new_num)
    divisors.remove(number)
    divisors.sort()
    return divisors

def Divisor_Length(number):
    return len(Find_Divisors(number))

def main():
    user = input("Enter A number to find its divisors : ")
    print(Find_Divisors(int(user)))
    print(f"The length of the divisor is {Divisor_Length(int(user))}")

if __name__ == '__main__':
    main()