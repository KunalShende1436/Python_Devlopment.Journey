# Febonacci Series
num = int(input("Enter the number of terms: "))
a=0
b=1
if num<=0:
    print("Please enter a positive integer.")
elif num==1:
    print("Fibonacci sequence up to", num, ":")
    print(a)
else:
    for i in range(num):
        print(a,end=" ")
        next_num=a+b
        a=b
        b=next_num
        