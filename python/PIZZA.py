# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1



# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L :")
add_pepperoni = input("Do you want pepperoni? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N :")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

if size=="S":
  bill=15
  if add_pepperoni =="Y" and extra_cheese =="Y":
    bill+=3
    print("ur total bill is :" , bill)
  if add_pepperoni =="Y" and extra_cheese =="N":
    bill+=2
    print("ur total bill is :" , bill)
  if add_pepperoni =="N" and extra_cheese =="Y":
    bill+=1
    print("ur total bill is :" , bill)
  if add_pepperoni =="N" and extra_cheese =="N":
    print("ur total bill is :", bill)

if size =="M":
  bill=20
  if add_pepperoni =="Y" and extra_cheese =="Y":
    bill+=4
    print("ur total bill is :" , bill)
  if add_pepperoni =="Y" and extra_cheese =="N":
    bill+=3
    print("ur total bill is :" , bill)
  if add_pepperoni =="N" and extra_cheese =="Y":
    bill+=1
    print("ur total bill is :" , bill)
  if add_pepperoni =="N" and extra_cheese =="N":
    print("ur total bill is :", bill)

if size =="L":
  bill=25
  if add_pepperoni =="Y" and extra_cheese =="Y":
    bill+=4
    print("ur total bill is :" , bill)
  if add_pepperoni =="Y" and extra_cheese =="N":
    bill+=3
    print("ur total bill is :" , bill)
  if add_pepperoni =="N" and extra_cheese =="Y":
    bill+=1
    print("ur total bill is :" , bill)
  if add_pepperoni =="N" and extra_cheese =="N":
    print("ur total bill is :", bill)

# BILL=0

# if size=="S":
#   BILL=BILL+15
# elif size=="M":
#   BILL=BILL+20
# else:
#   BILL+=25

# if add_pepperoni=="Y":
#   if size=="S":
#     BILL=BILL+2
#   else:
#     BILL+=3

# if extra_cheese=="Y":
#   BILL+=1
# else:
#   BILL=BILL
 
# print (f"the total bill is : {BILL}")







