print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n") 

direction=input("ur at the starting point which way do u wanna go 'left' or 'right' ?\n" )
if direction =="left":
    travel=input("u have reached bank of river ,so u wanna 'wait' for a boat or will u 'swim' ?\n")
    if travel =="wait":
        door=input("u have reached final stage ,select a door among RED ,BLUE,GRAY ?\n")
        if door=="gray":
            print(''' hurray !! u have won the game and the treasure is yours :
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
 ''')
        else :
            print(" u had opened wrong door ,# hard try :(,better luck nxt tym :)")
    else:
        print(" oops! u was eaten by a shark ,u have lost the game ,better luck nxt tym:(")
else:
    print(" *** BOOM *** u stepped on a landmine  ,by selecting wrong direction, u have lost ,better luck nxt tym :( ")
