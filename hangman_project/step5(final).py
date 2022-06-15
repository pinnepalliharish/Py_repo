#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
name_list=["gambhir",'dhoni','virat','sachin','zaheer','harbhajan','sehwag','raina','yuvraj','munafpatel','sreeshanth','ashwin',"chawla",
'yusyf']
chosen_word = random.choice(name_list)

lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
print("2011 CWC team INDIA")
#Testing code
#Create blanks
display = []
for x in range(len(chosen_word)): 
    display+="_"

blanks_are_filled=False
while not blanks_are_filled :
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"the letter {guess} is already guessed,so try another letter.***NO LIFE LOST***")

    #Check guessed letter
    for k in range(len(chosen_word)):
        letter=chosen_word[k]
        if guess ==letter:
            display[k]=letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"the letter {guess} , is not in the chosen word,so its wrong and you lost a life ")
        lives -= 1
        if lives == 0:
            blanks_are_filled = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        blanks_are_filled = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    print(stages[lives])