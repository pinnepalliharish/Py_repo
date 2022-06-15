#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password=""
# for k in range(0,nr_letters):
#     char= random.choice(letters)
#     password+=char
# for L in range(0,nr_symbols):
#     sym=random.choice(symbols)
#     password+=sym
# for M in range(0,nr_numbers):
#     digit=random.choice(numbers)
#     password+=digit
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8
password_list=[]
for k in range(0,nr_letters):
    char= random.choice(letters)
    password_list+=char
for k in range(0,nr_symbols):
    sym=random.choice(symbols)
    password_list+=sym
for k in range(0,nr_numbers):
    digit=random.choice(numbers)
    password_list+=digit
random.shuffle(password_list)
print(password_list)

password=""
for k in password_list:
    password+=k
print(password)