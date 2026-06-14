def absolute_value(num):
    if num >= 0:
        return num
    else:
        return num * -1


num = int(input("Enter Number="))
absolute_value = absolute_value(num)
print(f"absolute number of{num} is {absolute_value}")
