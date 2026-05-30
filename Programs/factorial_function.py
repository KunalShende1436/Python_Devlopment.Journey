#Function for factorial
def find_factorial(n):
    if n<0:
        print("Factorial does not exist for negative numbers")
    elif n==0:
        print("The factorial of 0 is 1")
    else:
        fact =1
        for i in range(1,n+1):
            fact=fact*i
        print(f"The factorial of {n} is {fact}")
        


num = int(input("Enter a number: "))
find_factorial(num)