print(f"Compound Interest Calculator")

principle = 0
rate = 0
time = 0
peryear = 0

principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate amount: "))/100
time = float(input("Enter the time in years: "))
peryear = float(input("Enter the times per year, interest is compounded: "))

while True:
    if principle <= 0:
        print("INVALID NUMBER")
        principle = float(input("Enter the principle amount: "))
    elif rate <= 0:
        print("INVALID NUMBER")
        rate = float(input("Enter the rate amount: "))/100
    elif time <= 0:
        print("INVALID NUMBER")
        time = float(input("Enter the time in years: "))
    elif peryear <= 0:
        print("INVALID NUMBER")
        peryear = float(input("Enter the times per year, interest is compounded: "))
    amount = principle * pow((1 + rate/peryear), peryear*time)
    print(f"The Final Amount is at ${amount:.2f} in {time} years")
    break