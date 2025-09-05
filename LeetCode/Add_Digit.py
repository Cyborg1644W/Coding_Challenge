def addDigits(num:int):
    new_num = num
    while True:
        new_num = sum(list(map(int, str(new_num))))
        if new_num < 10:
            return new_num
        new_num = new_num
        
print(addDigits(38))    