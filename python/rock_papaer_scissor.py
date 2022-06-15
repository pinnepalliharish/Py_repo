

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

posibilities=[rock,paper,scissors]
my_selection=int(input("press 0 for rock/1 for paper/2 for scissors : "))
print("your choice is:")
print(posibilities[my_selection])
import random
computer_selection=random.randint(0,2)
print("computers choice is:")
print(posibilities[computer_selection])


if my_selection==computer_selection:
    print(" match is drawn")
elif my_selection==0 and computer_selection==2:
    print("u won")
elif my_selection==1 and computer_selection==0:
    print("u won")
elif my_selection==2 and computer_selection==1:
    print("u won")
elif my_selection==0 and computer_selection==1:
    print(" u lost")
elif my_selection==1 and computer_selection==2:
    print(" u lost")
elif my_selection==2 and computer_selection==1:
    print(" u lost")

   


