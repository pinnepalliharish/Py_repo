print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = (name1+ " " +name2).lower()
T=combined_name.count("t")
R=combined_name.count("r")
U=combined_name.count("u")
E=combined_name.count("e")
number_1=str(T+R+U+E)

L=combined_name.count("l")
O=combined_name.count("o")
V=combined_name.count("V")
E=combined_name.count("e")
number_2=str(L+O+V+E)

score= int( (number_1)+ (number_2))
print(score)

if (score <=10 or score>=90):
    print(f"your score is {score} , u are like coke and mentos") 
if (score>=40 and score<=50):
    print(f"your scoe is {score},u are alright:)")
else:
    print (f"ur score is {score}")

