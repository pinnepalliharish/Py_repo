alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text_r,shift_r,direction_r):
    if direction == "encode":
        encrypt_text = ""
        for k in text_r:
            position = alphabet.index(k)
            new_position = position + shift_r
            encrypt_text += alphabet[new_position]
        print(f"The encoded text is {encrypt_text}")

    elif direction == "decode":
        decrypt_text = ""
        for k in text_r:
            position = alphabet.index(k)
            new_position = position - shift_r
            decrypt_text += alphabet[new_position]
        print(f"The decoded text is {decrypt_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text_r=text,shift_r=shift,direction_r=direction)