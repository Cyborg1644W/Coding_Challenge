# 🔁 Happy Numbers
# Statement: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process. If it eventually reaches 1, it's a happy number. Otherwise, it loops endlessly.
# 📌 You can write:
# Start with a number n.
# Replace n with the sum of the squares of its digits.
# Repeat this process.
# If you eventually reach 1, then n is a happy number.
# If you get stuck in a loop that never hits 1, n is not happy.


def Happy_Number(number):
    running = True
    New_num = number
    done_list = []
    while running:
        number = list(str(New_num))
        number = {int(i) for i in number}
        number = {num**2 for num in number}
        New_num = 0
        for squared in number:
            New_num += squared

        if New_num == 1:
            return True,done_list
        elif New_num in done_list:
            return False, done_list
        done_list.append(New_num)
    
def main():
    print(Happy_Number(412))
    

if __name__ == '__main__':
    main()