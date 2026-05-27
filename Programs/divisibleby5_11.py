num=int(input("Enter a number:"))
if num % 5 ==0 and num % 11 ==0:
    print(num,"is divisible by both 5 and 11")
elif num % 5 ==0:
    print(num,"is divisible by 5 but not by 11")
elif num % 11 ==0:
    print(num,"is divisible by 11 but not by 5")    
else:
    print(num,"is not divisible by either 5 or 11")        