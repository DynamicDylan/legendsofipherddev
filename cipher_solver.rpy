# Define the encryption function for the Caesar cipher
label begin:
    python:
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

    # Define the decryption function for the Caesar cipher
    python:
        def decrypt(cipher_text, shift):
            decrypted_text = ""
            for char in cipher_text:
                if char.isalpha():
                    shifted = ord(char) - shift  # Shift the character in the opposite direction
                    if char.islower():
                        if shifted < ord('a'):
                            shifted += 26  # Wrap around if shifted character is before 'a'
                    elif char.isupper():
                        if shifted < ord('A'):
                            shifted += 26  # Wrap around if shifted character is before 'A'
                    decrypted_text += chr(shifted)
                else:
                    decrypted_text += char  # Keep non-alphabetic characters unchanged
            
            return decrypted_text

    # Function to check the player's guess
    label check_guess:
        python:
            cipher_text = "Slnlukz vm Pwolyk"  # Replace this with your encrypted text
            decrypted_text = decrypt(cipher_text, 7)  # Assuming the cipher used a shift of 7

            guess = renpy.input("Enter your guess: ")  # Ren'Py input function to get player's guess

            if guess.lower() == decrypted_text.lower():
                renpy.display("cipher_game_screen", "result_text", "Congratulations! You solved the cipher!")
            else:
                renpy.display("cipher_game_screen", "result_text", "Sorry, that's not the correct answer. Try again.")

# Screen definition for the cipher-solving mini-game
screen cipher_game_screen():
    vbox:
        align (0.5, 0.5)  # Center align vertically and horizontally
        text "Welcome to the Cipher Solver!"
        text "Enter your guess:"
        input default "Enter your guess here:" id "guess_input"  # Assign an id to the input field
        button:
            text "Check Answer"
            action Function(check_guess)

        # Display the result text using 'text' within the screen
        text "Result Text Displayed Here" id "result_text"  # Assign an id to the result text
