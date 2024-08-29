import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0' '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '(', ')']
password = []

print("Welcome to Python Password Generator! ")
nr_letters = int(input("How many letters would you like your password to contain?:\n"))
nr_numbers = int(input("How many numbers would you like your password to contain?: \n"))
nr_symbols = int(input ("How many symbols would you like your password to contain?:\n"))

for index in range(1, nr_letters):
    password.append(random.choice(letters))
    for index in range(1, nr_numbers):
        password.append(random.choice(numbers))
        for index in range(1, nr_symbols):
            password.append(random.choice(symbols))
print(password)

print("Sit back while I generate your password :D")
#PROGRAMM NOT FINISHED