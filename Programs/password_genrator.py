import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
print("Easy Level")
password = ""
for char in range(1,n_letters+1):
    random_char = random.choice(letters)
    password += random_char
for sym in range (1,n_symbols+1):
    rando_sym = random.choice(symbols)
    password += rando_sym    
for num in range (1,n_numbers+1):
    rando_num = random.choice(numbers)
    password += rando_num
print(f"Your password is: {password}")    

print("Hard Level")
password_list = []
for char in range(1,n_letters+1):
    password_list.append(random.choice(letters))
for sym in range (1,n_symbols+1):
    password_list.append(random.choice(symbols))
for num in range (1,n_numbers+1):
    password_list.append(random.choice(numbers))
print(f"Your password is: {password_list}")  
random.shuffle(password_list)
print(f"Your password is: {password_list}")
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")