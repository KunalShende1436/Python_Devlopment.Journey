# count char and vowels and consonants in a string
str=input("Enter a string: ")
vowels='aeiouAEIOU'
char_count=0
vowel_count=0
consonant_count=0
for char in str:
    if char.isalpha():
        char_count+=1
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print(f"Number of characters: {char_count}")
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")            