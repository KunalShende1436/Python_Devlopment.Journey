l=[11, 22, 33, 44, 55, 66, 77, 88, 99]
print("Original list:", l)
j= 2
for i in range(1,len(l),2):
    l[i]= j
    j+=2
print("Modified list:", l)