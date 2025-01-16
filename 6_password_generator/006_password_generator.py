# Step 1: Import required modules for handling strings and generating secure random values
# Step 2: Define a function to check for uppercase characters in a password
   # Iterate over each character in the password
      # If an uppercase character is found, return True
   # If no uppercase character is found, return False
# Step 3: Define a function to check for symbols in a password
   # Iterate over each character in the password
      # If the character is in the punctuation set, return True
   # If no symbol is found, return False
# Step 4: Define a function to generate a random password based on user preferences

    # Step 5: Start with a base combination of lowercase letters and digits

    # Step 6: If symbols are required, add punctuation to the combination

    # Step 7: If uppercase letters are required, add them to the combination

    # Step 8: Calculate the total number of available characters in the combination

    # Step 9: Initialize an empty string to store the generated password

    # Step 10: Use a loop to generate random characters for the password

        # Append a randomly chosen character from the combination to the password
    
    # Step 11: Return the generated password

# Step 12: Use the main block to test the password generator

    # Step 13: Generate and display 5 random passwords with specifications

        # Generate a password of length 15 with symbols and uppercase letters

        # Check the specifications of the generated password

        # Print the password along with its specifications


import string
import secrets

def contains_upper(password: str) -> bool:
    
    for char in password:
        if char.isupper():
            return True

    return False

def contains_symbols(password: str) -> bool:

    for char in password:
        if char in string.punctuation:
            return True

    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:

    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length: int = len(combination)

    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    
    return new_password


if __name__ == '__main__':

    for i in range(1, 6):
        new_pass: str = generate_password(length=15, symbols=True, uppercase=True)
        specs: str = f'U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')