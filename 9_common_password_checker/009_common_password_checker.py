# Step 1: Define the check_password Function
# Purpose: To determine if a given password is among the 100,000 most common passwords.
# Write a Docstring:
# Include a brief explanation of the function's purpose.
# Provide the source URL for the common password list used in the script.
# Open and Read the Common Passwords File:
# Use the open() function to access the file (passwords.text) containing the common passwords.
# Read the file content and split it into a list of strings using .splitlines().
# Compare Input Password Against Common Passwords:
# Iterate over the list of common passwords using a for loop:
# Use enumerate() to keep track of the index (i) of each password, starting at 1.
# Check if the input password matches the current common_password.
# Handle a Match:
# If a match is found, print a message indicating the password is common (❌) and include its rank (#i).
# Exit the function using return to stop further processing.
# Handle a Unique Password:
# If no match is found after the loop, print a message indicating the password is unique (✅).

def check_password(password: str):

    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
    
    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: ❌ (#{i})')
            return
        
    print(f'{password}: ✅ (Unique)')

# Step 2: Define the main Function
# Purpose: To serve as the entry point for the script and handle user input.
# Prompt the User for a Password:
# Use input() to ask the user to enter a password.
# Call the check_password Function:
# Pass the user-provided password as an argument to the check_password function.

def main():

    user_password: str = input('Enter a password: ')
    check_password(password=user_password)

# Step 3: Set the Script Entry Point
# Use the if __name__ == '__main__': construct to ensure the script runs only when executed directly.
# Call the main() function to start the password check process.

if __name__ == '__main__':
    main()