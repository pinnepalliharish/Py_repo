names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(",")
import random
print(f"{random.choice(names)} is going to pay the bill") 