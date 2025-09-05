import math


def input_coordinate():
    x1 = int(input("Enter first x :  "))
    y1 = int(input("Enter first y :  "))
    x2 = int(input("Enter second x :  "))
    y2 = int(input("Enter second y :  "))
    return x1, y1, x2, y2

def get_abc():
    a = int(input("Enter a :  "))
    b = int(input("Enter b :  "))
    c = int(input("Enter c :  "))
    return a, b, c
        
def count_decimals(number):
    number_str = str(number)
    if '.' in number_str:
        return len(number_str.split('.')[1])
    return 0


class Pythagorean:
    def __init__(self):
        self.first_num = int(input("Enter the first number : "))
        self.second_num = int(input("Enter the second number :  "))

    def ask(self):
        while True:
            try:
                user = int(input("Pythagorean Solver\n1:Hypothenuse\n2:Leg\n"))
                if user in [1, 2]:
                    return user
                else:
                    print("Please enter 1 or 2 only.")
            except ValueError:
                return "Enter a Valid Number"
    
    def solve(self):
        solv = self.ask()
        try:
            if solv == 1:
                answer = math.sqrt((self.first_num**2)+(self.second_num**2))
                return f"The hypotenuse is {answer:,.2f}"
            elif solv == 2:
                c = max(self.first_num, self.second_num)
                a = min(self.first_num, self.second_num)
                if c <= a:
                    return "Invalid input: hypotenuse must be larger than leg."
                answer = math.sqrt(c**2 - a**2)
                return f"The leg is {answer:,.2f}"
        except ValueError:
            return "Math error: Check if inputs are valid for a right triangle."


class Quadratic: # X = (-b ± √(b²-4ac)) / (2a)
    def __init__(self):
        print("STANDARD FORM : ax² + bx + c")
        self.a, self.b, self.c = get_abc()
        
    def solve(self):
        try:
            numerator = math.sqrt(self.b ** 2 - (4 * self.a * self.c)) #√(b²-4ac)
            denominator = self.a * 2 #2a
            answer_1 = (-1 * self.b + numerator)/denominator #positive
            answer_2= (-1 * self.b - numerator)/denominator #negative
            return f"Answer: {answer_1:,.2f} and {answer_2:,.2f}"
        except ValueError:
            return f"Math Error: Enter a Valid Number"


class DistanceFormula: #d = √((x₂ - x₁)² + (y₂ - y₁)²).
    def __init__(self):
        self.x_1 , self.y_1 , self.x_2 , self.y_2 = input_coordinate()

    def solve(self):
        try:
            distance = math.sqrt((self.x_2 - self.x_1)**2 + (self.y_2 - self.y_1)**2)
            return f"The distance is {distance:,.2f}"
        except:
            return "Math Error: Check if you input the right number"


class Slope: #m = (y2 - y1) / (x2 - x1)
    def __init__(self):
        self.x_1 , self.y_1 , self.x_2 , self.y_2 = input_coordinate()
        
    def solve(self):
        try:
            slope = (self.y_2 - self.y_1)/(self.x_2 - self.x_1)
            return f"The slope is : {slope}"
        except ValueError:
            return "Math Error: Check if you input the right number"
        
        
class Triangle: #Area = sqrt(s(s - a)(s - b)(s - c))    ;    bh/2
    def __init__(self):
        try:
            self.choice = input("1 : All Sides Given\n2 : Base & Height Given\n---> ")
            if self.choice == '1':
                self.a = int(input("enter side A : "))
                self.b = int(input("enter side B : "))
                self.c = int(input("enter side C : "))    
            elif self.choice == '2':
                self.base = int(input("enter base"))
                self.height = int(input("enter height"))
            else:
                print("1 and 2 only")
        except ValueError:
            return "Math Error: Enter a Valid Number"
        
    def solve(self):
        if self.choice == '1': #sqrt(s(s - a)(s - b)(s - c))
            try:
                semi_p = (self.a + self.b + self.c)/2
                answer = math.sqrt(semi_p * (semi_p - self.a) * (semi_p - self.b) * (semi_p - self.c))
                return f"The area of the triangle is {answer:,.2f}"
            except ValueError:
                return "Math Error: Enter a Valid Number"
            
        elif self.choice == '2': #bh/2
            try:
                area = (self.base * self.height) / 2
                return f"The area of the triangle is {area:.2f}"
            except ValueError:
                return "Math Error: Enter a Valid Number"
            
            
class Circle:
    def __init__(self):
        self.radius = int(input("Enter the radius :  "))

    def ask(self):
        while True:
            try:
                choice = input("Solving for Area or Circumference?  ")
                if choice.lower() == 'area':
                    return 1
                elif choice.lower() == 'circumference':
                    return 2
                else:
                    print("Please Enter a Valid Number")
            except ValueError:
                return "Enter a Valid Number"

    def solve(self):
        choice = self.ask()
        try:
            if choice == 1:
                answer = math.pi*(self.radius**2)
                return f"The Area is {answer:,.2f}"
            elif choice == 2:
                answer = math.pi*self.radius*2
                return f"The Circumference is {answer:,.2f}"
        except:
            return "Math Error: Check if you input the right number"


class AngleConvertion: # radian and degree
    def __init__(self):
        try:
            self.number = int(input("Enter a Number : "))
            while True:
                self.options = int(input("1: Degreee to Radian\n2: Radian to Degree\n---> "))
                if self.options in [1,2]:
                    False
        except ValueError:
            return "Enter a Valid Number"
        
    def solve(self):
        if self.options == 1:
            answer = math.pi/self.number
        else:
            answer = self.number/math.pi
        return answer
           
            
class PrimeFactorization:
    def __init__(self,number = None):
        self.list = []
        if number is not None:
            self.number = number
        else:
            self.number = int(input("Enter a Number :  "))

    def solve(self):
        while True:
            try:
                user_num = self.number
                for number in range(1,user_num + 1):
                    if user_num % number == 0:
                        self.list.append(number)
                return self.list
            except ValueError:
                return "Math Error: Enter a Valid Number"


class GCF(PrimeFactorization):
    def __init__(self,number1 = None, number2 = None):
        if number1 is not None and number2 is not None:
            self.first_num = number1
            self.second_num = number2
        else:
            self.first_num = int(input("Enter The First Number :  "))
            self.second_num = int(input("Enter The Second Number :  "))
        
    def solve(self):
        first_factor = PrimeFactorization(self.first_num).solve()
        second_factor = PrimeFactorization(self.second_num).solve()
        common = set(first_factor) & set(second_factor)
        return max(common)
          
                
class LCM(GCF): # ab/GCF
    def __init__(self): 
        self.a = int(input("Enter The First Number :  "))
        self.b = int(input("Enter The Second Number :  "))
    
    def solve(self):
        lcm = (self.a * self.b)/GCF(self.a, self.b).solve()
        return lcm


class DecimaltoFraction(GCF): 
    def __init__(self):
        try:
            self.fraction = float(input("Enter a Number"))
        except ValueError:
            return "Math Error: Enter a Valid Number"
        
    def solve(self):
        denominator = 1
        decimal_length = count_decimals(self.fraction)
        separated = str(self.fraction).split(".")
        numerator = int("".join(separated))
        for i in range(decimal_length ):
            denominator *= 10
        gcf = GCF(numerator,denominator).solve()
        return f"{int(numerator/gcf)}/{int(denominator/gcf)}"
    
    
def main():
    is_running = True
    options = {1 : Pythagorean,
            2 : Quadratic,
            3 : DistanceFormula,
            4 : Slope,
            5 : Triangle,
            6 : Circle,
            7 : AngleConvertion,
            8 : PrimeFactorization,
            9 : GCF,
            10: LCM,
            11: DecimaltoFraction}
    
    while is_running:
        not_options = True
        while not_options:
            for key, value in options.items():
                print(f"{key} : {value.__name__}")
            user_choice = int(input("---> "))
            if user_choice in options.keys():
                not_options = False
        
        solver = options[user_choice]()
        print(solver.solve())
        quit = input("Press anything to continue, Q to Quit : ")
        if quit.lower == 'q':
            is_running = False
        
        
if __name__ == '__main__':
    main()