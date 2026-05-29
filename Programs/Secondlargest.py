# Second largest element in an array/list
list=[] 
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    list.append(element)
largest = second_largest = float('-inf')

for num in list:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)