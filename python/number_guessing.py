#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
number=random.choice(range(1,100))
logo=""" 
  _______  ____  ____   _______   ________  ________      ___________  __    __    _______      _____  ___   ____  ____  ___      ___  _______    _______   _______   
 /" _   "|("  _||_ " | /"     "| /"       )/"       )    ("     _   ")/" |  | "\  /"     "|    (\"   \|"  \ ("  _||_ " ||"  \    /"  ||   _  "\  /"     "| /"      \  
(: ( \___)|   (  ) : |(: ______)(:   \___/(:   \___/      )__/  \\__/(:  (__)  :)(: ______)    |.\\   \    ||   (  ) : | \   \  //   |(. |_)  :)(: ______)|:        | 
 \/ \     (:  |  | . ) \/    |   \___  \   \___  \           \\_ /    \/      \/  \/    |      |: \.   \\  |(:  |  | . ) /\\  \/.    ||:     \/  \/    |  |_____/   ) 
 //  \ ___ \\ \__/ //  // ___)_   __/  \\   __/  \\          |.  |    //  __  \\  // ___)_     |.  \    \. | \\ \__/ // |: \.        |(|  _  \\  // ___)_  //      /  
(:   _(  _|/\\ __ //\ (:      "| /" \   :) /" \   :)         \:  |   (:  (  )  :)(:      "|    |    \    \ | /\\ __ //\ |.  \    /:  ||: |_)  :)(:      "||:  __   \  
 \_______)(__________) \_______)(_______/ (_______/           \__|    \__|  |__/  \_______)     \___|\____\)(__________)|___|\__/|___|(_______/  \_______)|__|  \___) 
                                                                                                                                                                      
 """
print(logo)
print("welcome to number guessing :) game ")
print("i'm thinking of the number between 1 and 100 ")
difficulty=input("choose the difficulty . 'easy' or 'hard' : " )
if difficulty=="easy":
    print("u have 10 guesses left")
    n=[10,9,8,7,6,5,4,3,2,1]
    for k in n:
        select=int(input("guess the number : "))
        if  select!=number:
            if select>number and k!=0:
                print("too high")
            if select<number and k!=0:
                print("too low")
                if k!=0:
                    print("guess again")
            k-=1
            if k==0:
                print("you have ran out of guesses :(") 
                print("u lost")
                print(f"the correct number is {number}")
            if k!=0:
                print(f"u have {k} guesse left ")
                  
        if  select==number:
            print(f"yes! the number is {number} and you won")


elif difficulty=="hard":
    print("u have 5 guesses left")
    n=[5,4,3,2,1]
    for k in n:
        select=int(input("guess the number : "))
        if  select!=number:
            if select>number and k!=0:
                print("too high")
            if select<number and k!=0:
                print("too low")
                if k!=0:
                    print("guess again")
            k-=1
            if k==0:
                print("you have ran out of guesses :(") 
                print("u lost")
                print(f"the correct number is {number}")
            if k!=0:
                print(f"u have {k} guesse left ")    
        if  select==number:
            print(f"yes! the number is {number} and you won")