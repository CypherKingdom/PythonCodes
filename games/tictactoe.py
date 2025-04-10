"""
Tic-Tac-Toe Game - A classic game where the player competes against the computer.

This module provides a fully-functional implementation of the Tic-Tac-Toe game
with a text-based interface. The player uses 'O' while the computer uses 'X'.
"""

import random


class TicTacToe:
    """Implementation of the Tic-Tac-Toe game."""
    
    def __init__(self):
        """Initialize a new game with an empty board."""
        # Initialize the board with numbers 1-9 for position selection
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # Place the first 'X' in the middle
        self.board[1][1] = 'X'
    
    def display_board(self):
        """Display the current state of the game board."""
        print("+-------+-------+-------+")
        for row in range(3):
            print("|       |       |       |")
            print(f"|   {self.board[row][0]}   |   {self.board[row][1]}   |   {self.board[row][2]}   |")
            print("|       |       |       |")
            print("+-------+-------+-------+")
    
    def enter_move(self):
        """
        Process the player's move.
        
        Returns:
            bool: True if the move was successful, False otherwise
        """
        while True:
            try:
                user_move = int(input("Enter your move (1-9): "))
                if user_move < 1 or user_move > 9:
                    print("Invalid input! Please enter a number between 1 and 9.")
                    continue
                
                # Convert user's move (1-9) to board coordinates
                row = (user_move - 1) // 3
                col = (user_move - 1) % 3
                
                # Check if the cell is already occupied
                if self.board[row][col] == 'X' or self.board[row][col] == 'O':
                    print("That position is already taken! Try another one.")
                    continue
                
                # Valid move, place 'O' on the board
                self.board[row][col] = 'O'
                return True
                
            except (ValueError, TypeError):
                print("Invalid input! Please enter a number.")
    
    def get_free_fields(self):
        """
        Get a list of empty positions on the board.
        
        Returns:
            list: List of (row, column) tuples for empty positions
        """
        free_fields = []
        for row in range(3):
            for col in range(3):
                if isinstance(self.board[row][col], int):
                    free_fields.append((row, col))
        return free_fields
    
    def computer_move(self):
        """Make a move for the computer by randomly selecting from free positions."""
        free_fields = self.get_free_fields()
        if free_fields:
            row, col = random.choice(free_fields)
            self.board[row][col] = 'X'
            print("Computer's move:")
    
    def check_win(self, sign):
        """
        Check if a player has won the game.
        
        Args:
            sign (str): 'X' for computer or 'O' for player
            
        Returns:
            bool: True if the player with the given sign has won, False otherwise
        """
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == sign:
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == sign:
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == sign:
            return True
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == sign:
            return True
        
        return False
    
    def is_board_full(self):
        """
        Check if the board is full.
        
        Returns:
            bool: True if there are no empty positions left, False otherwise
        """
        return len(self.get_free_fields()) == 0
    
    def play(self):
        """Start and manage the game until completion."""
        print("Welcome to Tic-Tac-Toe!")
        print("You play as 'O', and the computer plays as 'X'.")
        print("The computer has already placed 'X' in the middle.")
        
        while True:
            # Display the current board
            self.display_board()
            
            # Player's turn
            self.enter_move()
            
            # Check if player has won
            if self.check_win('O'):
                self.display_board()
                print("Congratulations! You've won!")
                break
            
            # Check if the board is full (draw)
            if self.is_board_full():
                self.display_board()
                print("It's a draw!")
                break
            
            # Computer's turn
            self.computer_move()
            
            # Check if computer has won
            if self.check_win('X'):
                self.display_board()
                print("The computer has won!")
                break
            
            # Check if the board is full (draw)
            if self.is_board_full():
                self.display_board()
                print("It's a draw!")
                break


def main():
    """Main entry point for the game."""
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()