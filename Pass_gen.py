import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0' '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '(', ')']
final_password = ""
password = ""
password_list = []
l = 1
n = 1
s = 1

print("Welcome to Python Password Generator! ")
nr_letters = int(input("How many letters would you like your password to contain?:\n"))
nr_numbers = int(input("How many numbers would you like your password to contain?: \n"))
nr_symbols = int(input ("How many symbols would you like your password to contain?:\n"))
pass_length = nr_letters + nr_numbers + nr_symbols + 1

# #easy version puts letters first then numbers and then symbols:
# for index in range(0, nr_letters):
#     password += random.choice(letters)
# for index in range(0, nr_numbers):
#     password += random.choice(numbers)
# for index in range(0, nr_symbols):
#     password += random.choice(symbols)
# print(password)

#Better version combines letters, numbers and symbols

for index in range(0, pass_length):
    if l <= nr_letters:
        password_list.append(random.choice(letters))
    if n <= nr_numbers:
        password_list.append(random.choice(numbers))
    if s <= nr_symbols:
        password_list.append(random.choice(symbols))
    l += 1
    n += 1
    s += 1
print(password_list)
random.shuffle(password_list)

for char in password_list:
    final_password += char
print("Your new password: " + final_password) 
