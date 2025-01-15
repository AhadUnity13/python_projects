import random  # For generating random choices for AI
import sys  # For exiting the program

# Define the RPS class
class RPS:
    def __init__(self):
        # Initialize the game with a welcome message and setup
        print('Welcome to RPS 9000!')
        
        # A dictionary mapping moves to their respective symbols
        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'}
        
        # A list of valid move names extracted from the dictionary keys
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        # Prompt the user to input their move
        user_move: str = input('Rock, paper, or scissors? >> ').lower()

        # Exit the game if the user types 'exit'
        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        # If the input is not valid, display an error and restart the game
        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()

        # Randomly select a move for the AI
        ai_move: str = random.choice(self.valid_moves)

        # Display the moves made by both the user and the AI
        self.display_moves(user_move, ai_move)
        
        # Check the outcome of the game based on the moves
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        # Print the moves chosen by the user and the AI
        print('----')
        print(f'You: {self.moves[user_move]}')  # Show the user's move and its symbol
        print(f'AI: {self.moves[ai_move]}')  # Show the AI's move and its symbol
        print('----')

    def check_move(self, user_move: str, ai_move: str):
        # Determine the outcome of the game and print the result
        if user_move == ai_move:
            print('It is a tie!')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!')
        else:
            print('AI wins...')


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()