# Anagram Strings

a = input("Enter the first string: ")
b = input("Enter the second string: ")
if sorted(a.lower())==sorted(b.lower()):
    print(f"{a} and {b} are anagrams.")
else:
    print(f"{a} and {b} are not anagrams.")