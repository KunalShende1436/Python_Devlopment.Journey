# Roman to Integer
 
roman=input("Enter a Roman numeral: ")
Roman_num={ 'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

int_num=0
for i in range(len(roman)):
    if i < len(roman)-1 and Roman_num[roman[i]] < Roman_num[roman[i+1]]:
        int_num -= Roman_num[roman[i]]
    else:
        int_num += Roman_num[roman[i]]
print(f"The integer value of the Roman numeral {roman} is {int_num}.")    