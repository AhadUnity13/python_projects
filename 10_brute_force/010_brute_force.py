#Import itertools, time, and string

import itertools
import string
import time

#define common_guess and change it to type str | None
#Check for Common Passwords 

def common_guess(word: str) -> str | None:

    with open('words.text', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f"Common match: {match} (#{i})"


#Define Brute Force Function
def brute_force(word: str, length: int, digits=False, symbols=False) -> str | None:

    chars: str = string.ascii_lowercase

# add if statements to digits and symbols where the variable chars += to chars.(the variable)

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'
        

#Define main function

def main():
    print('Searching...')
    password: str = 'pass1'

    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password, length=5, digits=True, symbols=False):
            print(cracked)
        else:
            print('There was no match...')

    end_time: float = time.perf_counter()

    print(round(end_time - start_time, 2), 's')

#Run Script using __name__

if __name__ == '__main__':
    main()