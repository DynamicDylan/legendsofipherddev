# cipher_game_logic.py

# Function to encrypt a message using Caesar cipher
def encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt the ciphered message
def decrypt(cipher_text, shift):
    decrypted_text = encrypt(cipher_text, -shift)
    return decrypted_text

