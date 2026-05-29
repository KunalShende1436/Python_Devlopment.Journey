# Check Number is Palindrome or not
x = int(input("Enter a number: "))
if x < 0:
    print(f"{x} is not a palindrome number")    
orginal = x
rev = 0
while x:
        digit = x % 10
        rev = rev * 10 + digit
        x //= 10
if orginal == rev:
    print(f"{orginal} is a palindrome number")
else:   
    print(f"{orginal} is not a palindrome number")        
