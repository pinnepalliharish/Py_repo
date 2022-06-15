#***USING FUNCTIONS***

# def prime_checker(number):
#     condition=True
#     for value in range(2,n):
#         if n%value==0:
#             condition=False
#     if condition:
#         print("it is a prime number")
#     else:
#         print("it's not a prime number")
# n = int(input("Check this number: "))

# prime_checker(number=n)


#***NORMAL METHODS***

n= (int(input("check this number :")))
condition=True
for value in range (2,n):
    if n%value==0:
        condition=False
if condition:
    print("it is a prime number")
else:
    print("it is not a prime number")