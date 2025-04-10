"""
Hangman Game - A word guessing game with a graphical interface.

This module implements a Hangman game using Tkinter for the GUI.
The player must guess a randomly selected word letter by letter
before the hangman drawing is completed.
"""

import tkinter as tk
import random


class HangmanGame:
    """Implementation of the Hangman game with GUI."""
    
    def __init__(self, master):
        """Initialize a new Hangman game.
        
        Args:
            master: Tkinter root window
        """
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("900x650")
        self.master.configure(bg='light blue')
        
        # Word list for the game
        self.word_list = ["PYTHON", "JAVASCRIPT", "KOTLIN", "JAVA", "RUBY", "SWIFT", 
                          "ALGORITHM", "VARIABLE", "FUNCTION", "DEVELOPER", "COMPUTER"]
        
        # Game state variables
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        
        # Initialize the GUI elements
        self.initialize_gui()
    
    def initialize_gui(self):
        """Initialize GUI components."""
        # Define common styles
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        
        # Create hangman canvas for drawing
        self.hangman_canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.hangman_canvas.pack(pady=20)
        
        # Word display shows correctly guessed letters
        self.word_display = tk.Label(
            self.master, 
            text="_ " * len(self.secret_word), 
            font=("Helvetica", 30), 
            bg='light blue'
        )
        self.word_display.pack(pady=(40, 20))
        
        # Reset button
        self.reset_button = tk.Button(
            self.master, 
            text="Reset Game", 
            command=self.reset_game, 
            width=20, height=2, 
            bg=button_bg, fg=button_fg, 
            font=button_font
        )
        self.reset_button.pack(pady=(10, 0))
        
        # Frame for alphabet buttons
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)
        
        # Setup alphabet buttons for letter selection
        self.setup_alphabet_buttons()
    
    def setup_alphabet_buttons(self):
        """Create alphabet buttons for letter selection."""
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        
        # Split alphabet into two rows for better display
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper_row = alphabet[:13]
        lower_row = alphabet[13:]
        
        # Create frames for each row
        upper_frame = tk.Frame(self.buttons_frame)
        upper_frame.pack()
        lower_frame = tk.Frame(self.buttons_frame)
        lower_frame.pack()
        
        # Create buttons for the first row
        for letter in upper_row:
            button = tk.Button(
                upper_frame, 
                text=letter, 
                command=lambda l=letter: self.guess_letter(l), 
                width=4, height=2, 
                bg=button_bg, fg=button_fg, 
                font=button_font
            )
            button.pack(side="left", padx=2, pady=2)
        
        # Create buttons for the second row
        for letter in lower_row:
            button = tk.Button(
                lower_frame, 
                text=letter, 
                command=lambda l=letter: self.guess_letter(l), 
                width=4, height=2, 
                bg=button_bg, fg=button_fg, 
                font=button_font
            )
            button.pack(side="left", padx=2, pady=2)
    
    def choose_secret_word(self):
        """Select a random word from the word list.
        
        Returns:
            str: The randomly selected word
        """
        return random.choice(self.word_list)
    
    def update_hangman_canvas(self):
        """Update the hangman drawing based on incorrect guesses."""
        self.hangman_canvas.delete("all")
        
        # Define drawing functions for each part
        stages = [
            self.draw_head, 
            self.draw_body, 
            self.draw_left_arm, 
            self.draw_right_arm,
            self.draw_left_leg, 
            self.draw_right_leg, 
            self.draw_face
        ]
        
        # Draw parts based on number of incorrect guesses
        for i in range(len(self.incorrect_guesses)):
            if i < len(stages):
                stages[i]()
    
    def draw_head(self):
        """Draw the head of the hangman."""
        self.hangman_canvas.create_oval(125, 50, 185, 110, outline="black", width=2)
    
    def draw_body(self):
        """Draw the body of the hangman."""
        self.hangman_canvas.create_line(155, 110, 155, 170, fill="black", width=2)
    
    def draw_left_arm(self):
        """Draw the left arm of the hangman."""
        self.hangman_canvas.create_line(155, 130, 125, 150, fill="black", width=2)
    
    def draw_right_arm(self):
        """Draw the right arm of the hangman."""
        self.hangman_canvas.create_line(155, 130, 185, 150, fill="black", width=2)
    
    def draw_left_leg(self):
        """Draw the left leg of the hangman."""
        self.hangman_canvas.create_line(155, 170, 125, 200, fill="black", width=2)
    
    def draw_right_leg(self):
        """Draw the right leg of the hangman."""
        self.hangman_canvas.create_line(155, 170, 185, 200, fill="black", width=2)
    
    def draw_face(self):
        """Draw the face details of the hangman."""
        # Draw X eyes
        self.hangman_canvas.create_line(140, 70, 150, 80, fill="black", width=2)
        self.hangman_canvas.create_line(150, 70, 140, 80, fill="black", width=2)
        self.hangman_canvas.create_line(160, 70, 170, 80, fill="black", width=2)
        self.hangman_canvas.create_line(170, 70, 160, 80, fill="black", width=2)
        
        # Draw sad mouth
        self.hangman_canvas.create_arc(140, 85, 170, 105, start=0, extent=-180, fill="black")
    
    def guess_letter(self, letter):
        """Process a letter guess from the player.
        
        Args:
            letter (str): The guessed letter
        """
        # Check if letter is in secret word
        if letter in self.secret_word and letter not in self.correct_guesses:
            self.correct_guesses.add(letter)
        elif letter not in self.incorrect_guesses:
            self.incorrect_guesses.add(letter)
            self.attempts_left -= 1
            self.update_hangman_canvas()
        
        # Update display and check game status
        self.update_word_display()
        self.check_game_over()
    
    def update_word_display(self):
        """Update the displayed word with correctly guessed letters."""
        displayed_word = " ".join([letter if letter in self.correct_guesses else "_" for letter in self.secret_word])
        self.word_display.config(text=displayed_word)
    
    def check_game_over(self):
        """Check if the game is over due to a win or loss."""
        # Check win condition: all letters guessed
        if set(self.secret_word).issubset(self.correct_guesses):
            self.display_game_over_message("Congratulations, you've won!")
        
        # Check lose condition: no attempts left
        elif self.attempts_left == 0:
            self.display_game_over_message(f"Game over! The word was: {self.secret_word}")
    
    def display_game_over_message(self, message):
        """Display game over message and restart button.
        
        Args:
            message (str): The message to display
        """
        stylish_font = ("Arial", 18, "italic")
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        
        # Hide regular game controls
        self.reset_button.pack_forget()
        self.buttons_frame.pack_forget()
        
        # Show game over message
        self.game_over_label = tk.Label(
            self.master, 
            text=message, 
            font=stylish_font, 
            fg="red", 
            bg='light blue'
        )
        self.game_over_label.pack(pady=(10, 20))
        
        # Show restart button
        if not hasattr(self, 'restart_button'):
            self.restart_button = tk.Button(
                self.master, 
                text="Restart Game", 
                command=self.reset_game, 
                width=20, height=2, 
                bg=button_bg, fg=button_fg, 
                font=button_font
            )
        self.restart_button.pack(pady=(10, 20))
    
    def reset_game(self):
        """Reset the game to start a new round."""
        # Reset game state
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        
        # Reset visual elements
        self.hangman_canvas.delete("all")
        self.update_word_display()
        
        # Re-enable alphabet buttons
        for frame in self.buttons_frame.winfo_children():
            for button in frame.winfo_children():
                button.configure(state=tk.NORMAL)
        
        # Show game controls
        self.reset_button.pack(pady=(10, 0))
        
        # Remove game over message
        if hasattr(self, 'game_over_label') and self.game_over_label.winfo_exists():
            self.game_over_label.pack_forget()
        if hasattr(self, 'restart_button') and self.restart_button.winfo_exists():
            self.restart_button.pack_forget()
        
        # Show buttons frame
        self.buttons_frame.pack()


def main():
    """Main entry point for the Hangman game."""
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()