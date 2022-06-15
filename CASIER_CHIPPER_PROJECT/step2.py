alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_en,shift_en):
    encrypted_text=""
    for k in text_en:
        position=alphabet.index(k)
        new_position=position+shift_en
        new_letter=alphabet[new_position]
        encrypted_text+=new_letter
    print(f"The encrypted text is {encrypted_text}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text_de,shift_de):
    decrypted_text=""
    for k in text_de:
        position=alphabet.index(k)
        new_poisition=position-shift_de
        new_letter=alphabet[new_poisition]
        decrypted_text+=new_letter
    print(f"The decrypted value is {decrypted_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
  #  amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
  

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
# Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction=="encode":
    encrypt(text_en=text,shift_en=shift)
elif direction=="decode":
    decrypt(text_de=text,shift_de=shift)
else:
    print("You entered incorrect info,please enter *encode* or *decode")


