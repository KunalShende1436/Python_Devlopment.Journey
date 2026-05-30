#Function for factorial using recursion
def find_factorial(n):
    if n<0:
        return "Factorial does not exist for negative numbers"  
    elif n==0:
        return 1
    else:
        if n==1:
            return 1
        else:
            return n * find_factorial(n-1)  
        
        
num = int(input("Enter a number: "))
print(find_factorial(num))