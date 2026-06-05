#First Non-Repeating Character
str=input("Enter a string: ")
char_count={}
for char in str:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
first_non_repeating=None
for char in str:
    if char_count[char]==1:
        first_non_repeating=char
        break   
if first_non_repeating:
    print(f"The first non-repeating character is: {first_non_repeating}")