"""
Collection of interactive games and educational programs.
"""

import random


def number_guessing_game():
    """
    Run a number guessing game where the user tries to guess a random number.
    The game provides feedback on whether to guess higher or lower.
    """
    game_number = 1
    
    while True:
        print(f"Game {game_number}:")
        target_number = random.randint(0, 100)
        attempt = 1
        
        while True:
            try:
                user_guess = int(input(f"Guess the number (attempt {attempt}): "))
                
                if user_guess == target_number:
                    print("Correct!!")
                    break
                elif user_guess > target_number:
                    print("Go lower")
                else:
                    print("Go higher")
                
                attempt += 1
            except ValueError:
                print("Please enter a valid number")
        
        play_again = input("Play another game? (y/n): ").lower()
        if play_again != 'y':
            break
        
        game_number += 1


def child_math_game():
    """
    Run a simple subtraction math game for children.
    Generates random subtraction problems and checks the answers.
    """
    correct_count = 0
    total_problems = 0
    
    while True:
        # Generate two random numbers
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        
        # Ensure num1 is greater than or equal to num2
        if num2 > num1:
            num1, num2 = num2, num1
        
        correct_answer = num1 - num2
        
        try:
            # Present the problem to the user
            user_answer = int(input(f"What is {num1} - {num2}? "))
            total_problems += 1
            
            # Check if the answer is correct
            if user_answer == correct_answer:
                print("The answer is correct!")
                correct_count += 1
            else:
                print(f"The answer is wrong. The correct answer is {correct_answer}")
            
            # Ask if the user wants to continue
            continue_game = input("Another problem? (y/n): ").lower()
            if continue_game != 'y':
                break
                
        except ValueError:
            print("Please enter a valid number")
    
    # Show final score
    if total_problems > 0:
        percentage = (correct_count / total_problems) * 100
        print(f"\nFinal score: {correct_count} correct out of {total_problems} ({percentage:.1f}%)")


def lotto_game():
    """
    Run a lottery simulation game where users select numbers and check against random draws.
    """
    
    def get_user_selection():
        """
        Get 5 numbers from the user.
        
        Returns:
            list: Selected numbers or empty list if user wants to quit
        """
        selection = []
        
        print("Select 5 numbers between 1 and 99:")
        for i in range(5):
            while True:
                try:
                    num = int(input(f"Number {i+1} (or -1 to quit): "))
                    
                    if num == -1:
                        return []
                        
                    if num < 1 or num > 99:
                        print("Please enter a number between 1 and 99")
                        continue
                        
                    if num in selection:
                        print("You've already selected that number")
                        continue
                        
                    selection.append(num)
                    break
                    
                except ValueError:
                    print("Please enter a valid number")
        
        return selection
    
    def check_results(selection):
        """
        Generate random lottery numbers and check matches with user selection.
        
        Args:
            selection (list): User's selected numbers
            
        Returns:
            int: Number of matches found
        """
        # Generate 10 random lottery numbers
        lottery_numbers = []
        for _ in range(10):
            lottery_numbers.append(random.randint(1, 99))
        
        # Count matches
        matches = 0
        for num in selection:
            if num in lottery_numbers:
                matches += 1
        
        print(f"Lottery numbers: {lottery_numbers}")
        print(f"Your numbers: {selection}")
        print(f"Matches: {matches}")
        
        return matches
    
    # Main game loop
    while True:
        print("\n=== LOTTERY GAME ===")
        
        # Get user's number selection
        selection = get_user_selection()
        
        # Check if user wants to quit
        if not selection:
            print("Thanks for playing!")
            break
        
        # Check results
        matches = check_results(selection)
        
        # Determine if user won
        if matches >= 3:
            print("Congratulations! You won!")
        else:
            print("Sorry, not enough matches. Try again!")


def run_game(game_choice):
    """
    Run a selected game.
    
    Args:
        game_choice (int): 1 for number guessing, 2 for child math, 3 for lotto
    """
    if game_choice == 1:
        number_guessing_game()
    elif game_choice == 2:
        child_math_game()
    elif game_choice == 3:
        lotto_game()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    print("=== GAME SELECTION ===")
    print("1. Number Guessing Game")
    print("2. Math Practice Game")
    print("3. Lottery Game")
    
    try:
        choice = int(input("Select a game (1-3): "))
        run_game(choice)
    except ValueError:
        print("Please enter a valid number")