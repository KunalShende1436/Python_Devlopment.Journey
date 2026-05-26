#Reverse a String/Number: Take a string or an integer input from the user and reverse it without using built-in slicing methods ([::-1]).


str=input("Enter a string or a number: ")
rev_str="" 
#Method 1: Using a for loop
print("Using a for loop")
for i in str:
    rev_str = i + rev_str
print(f"The reverse of {str} is {rev_str}")

#Method 2: Using a while loop
print("Using a while loop")
rev_str=""  
i = len(str) - 1
while i >= 0:
    rev_str += str[i]
    i -= 1
print(f"The reverse of {str} is {rev_str}")

#Method 3: Using Slicing
print("Using Slicing")
rev_str = str[::-1]
print(f"The reverse of {str} is {rev_str}")