#In this I am learning how to import an external module and made the game harder by only having 3 tries using while loops and if statements. 
#For example, I learned to import randint from random.

from random import randint

#My generator will randomly generate a number from 1 to 10 and you will have 3 tries to guess the correct one.

lower_num, upper_num = 1, 10

#Now my generator will randomly generate by using randint

random_number: int = randint(lower_num, upper_num)
print(f'Enter a range of number between {lower_num} and {upper_num}')

#I will now use while loop to start my game.

number_tries: int = 1

while True:
    #Now we'll ensure the game won't crash by adding a try block and writing int(input()) to convert it from string to integer.
    try:
        user_guess: int = int(input('Guess: ')) #I need to find out how int function throws a ValueError and what other type of errors it throws.
    except ValueError as e:
        #Now to prevent the game crashing we will print a statement to continue the game.
        print('Please enter a valid number.')
        continue

    #Write if and elif statements if the user_guess number is higher than random number print a statement saying number is lower. 
    #If user_guess number is lower than random_number prints a number saying number is higher.
    #If you guessed correct number, print a statement saying "You guessed it!"

    if user_guess > random_number:
        print("The number is lower.")
        print(f"Try {number_tries}")
    elif user_guess < random_number:
        print("The number is higher.")
        print(f"Try {number_tries}")
    else:
        print("You guessed it!")
        break

    if number_tries == 3:
        print("You used all your tries. Game over.")
        break
    number_tries = number_tries + 1
