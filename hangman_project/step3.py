#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for x in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the 
# chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
blanks_are_filled=False
while not blanks_are_filled:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for k in range(len(chosen_word)):
        letter=chosen_word[k]
        if guess ==letter:
            display[k]=letter
    print(display)
    if "_" not in display:
        blanks_are_filled=True
        print("u win")
