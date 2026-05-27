# Reverse Interger
x=int(input("Enter an Interger:"))
sign = -1 if x < 0 else 1
x = abs(x)
rev = 0
while x != 0:
    digit = x % 10
    rev = rev * 10 + digit
    x //= 10
    rev *= sign
if rev < -(2**31) or rev > (2**31 - 1):
    print("The reversed integer is out of the 32-bit signed integer range.")
else:
    print(f"The reverse of the integer is {rev}")
