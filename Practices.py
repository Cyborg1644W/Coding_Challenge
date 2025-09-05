name = []

def get_text(prompt):
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a name ")

ask = get_text("enter a name:  ")
name.append(ask)
print(name)