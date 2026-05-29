# Largest element in an array/list
list=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    list.append(element)
largest=list[0]
for i in range(1,n):
    if list[i]>largest:
        largest=list[i] 
print(f"The largest element in the list is: {largest}")           