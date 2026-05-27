#binary sum of two numbers
a = input("Enter first number: ")
b = input("Enter second number: ")

i=len(a)-1
j=len(b)-1
carry=0
sum=""
while i >= 0 and j >= 0 or carry:
    total=carry
    if i >= 0:
        total += int(a[i])
        i -= 1
    if j >= 0:
        total += int(b[j])
        j -= 1
    sum = str(total % 2) + sum
    carry = total // 2         
print(f"The binary sum of {a} and {b} is {sum}.")    