alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
 'v', 'w', 'x', 'y', 'z']





def caesar(text_r,shift_r,direction_r):
    if direction == "encode":
        encrypt_text = ""
        for k in text_r:
            if k in alphabet:
                position = alphabet.index(k)
                new_position = position + shift_r
                encrypt_text += alphabet[new_position]
            #TODO-3: What happens if the user enters a number/symbol/space?
            #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
            #e.g. start_text = "meet me at 3"
            #end_text = "•••• •• •• 3"  
            else:
                encrypt_text+=k
 
        print(f"The encoded text is {encrypt_text}")

    elif direction == "decode":
        decrypt_text = ""
        for k in text_r:
            if k in alphabet:
                position = alphabet.index(k)
                new_position = position - shift_r
                decrypt_text += alphabet[new_position]
            #TODO-3: What happens if the user enters a number/symbol/space?
            #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
            #e.g. start_text = "meet me at 3"
            #end_text = "•••• •• •• 3"
            else:
                decrypt_text+=k
            
        print(f"The decoded text is {decrypt_text}")

#TODO-1: Import and print the logo from art.py when the program starts.


#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 





#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
yes=False
while not yes:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesar(text_r=text,shift_r=shift,direction_r=direction)
    

    select=input("\nType 'yes' if you want to go again. Otherwise type 'no' :    \n")

    if select == "no":
        yes=True
        print("byee")




