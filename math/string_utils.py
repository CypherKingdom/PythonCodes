"""
String Utilities Module - Collection of string manipulation functions.

This module provides various string operations including:
- String reversal
- Vowel/consonant separation
- String matching operations
"""

def reverse_string(text):
    """
    Reverses a string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    return text[::-1]


def split_vowels_consonants(text):
    """
    Splits a string into vowels and consonants.
    
    Args:
        text (str): Input string to split
        
    Returns:
        tuple: (vowels_string, consonants_string)
    """
    vowels = ""
    consonants = ""
    
    for char in text:
        if char.lower() in "aeiou":
            vowels += char
        else:
            consonants += char
    
    return vowels, consonants


def has_matching_ends(text):
    """
    Checks if the first and last characters of a string match (case-insensitive).
    
    Args:
        text (str): String to check
        
    Returns:
        bool: True if first and last characters match, False otherwise
    """
    if len(text) < 2:
        return False
    
    return text[0].lower() == text[-1].lower()


def count_matching_strings(strings):
    """
    Counts strings that have matching first and last characters.
    
    Args:
        strings (list): List of strings to check
        
    Returns:
        int: Count of strings with matching first and last characters
    """
    count = 0
    for s in strings:
        if has_matching_ends(s):
            count += 1
    
    return count


def search_replace_word(filename, search_word=None, replace_word=None, auto_replace=False):
    """
    Search for a word in a file and replace it if desired.
    
    Args:
        filename (str): The name of the file to search in
        search_word (str, optional): Word to search for
        replace_word (str, optional): Word to replace with
        auto_replace (bool): Whether to automatically replace without confirmation
        
    Returns:
        tuple: (success, message) indicating result of operation
    """
    if search_word is None:
        search_word = input("Enter the word to be searched: ")
    
    if replace_word is None:
        replace_word = input("Enter the word to replace it with: ")

    try:
        with open(filename, 'r') as file:
            file_content = file.read()

        if search_word in file_content:
            if not auto_replace:
                choice = input("Word found in the file. Do you want to replace it? (yes/no): ").lower()
                should_replace = choice == 'yes'
            else:
                should_replace = True
                
            if should_replace:
                new_content = file_content.replace(search_word, replace_word)
                with open(filename, 'w') as file:
                    file.write(new_content)
                return True, "Word replaced successfully."
            else:
                return False, "Operation canceled."
        else:
            return False, "Word not found in the file."

    except FileNotFoundError:
        return False, f"File '{filename}' not found."


def count_character_occurrences(char, text):
    """
    Count occurrences of a single character in a string.
    
    Args:
        char (str): Character to count (must be a single character)
        text (str): Text to search in
        
    Returns:
        int or str: Count of occurrences or error message
    """
    if len(char) != 1:
        return "Error: Input must be a single character"
    
    return text.count(char)


def create_indexed_dictionary(text):
    """
    Create a dictionary mapping position numbers to characters in a string.
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary with positions (1-based) as keys and characters as values
    """
    dictionary = {}
    for i in range(len(text)):
        dictionary[i + 1] = text[i]
    return dictionary


def count_alphabetic_chars(text):
    """
    Count alphabetic characters in a string.
    
    Args:
        text (str): Input text
        
    Returns:
        int: Number of alphabetic characters
    """
    return sum(1 for char in text if char.isalpha())


def separate_vowels_consonants(text):
    """
    Separate vowels and consonants from a string.
    
    Args:
        text (str): Input text
        
    Returns:
        tuple: Lists of vowels and consonants, and their counts
    """
    vowels = []
    consonants = []
    
    for char in text:
        if char.lower() in 'aeiou':
            vowels.append(char)
        elif char.isalpha():
            consonants.append(char)
    
    return vowels, len(vowels), consonants, len(consonants)


def is_palindrome(text):
    """
    Check if a string is a palindrome (reads the same forward and backward).
    
    Args:
        text (str): Input text
        
    Returns:
        bool: True if text is a palindrome, False otherwise
    """
    # Normalize the text by removing spaces and converting to lowercase
    text = text.strip().lower()
    
    # Check if the normalized text equals its reverse
    return text == text[::-1]


def count_letter_frequency(text):
    """
    Count frequency of each letter in a text.
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary with characters as keys and their counts as values
    """
    # Convert to lowercase to treat case-insensitively
    text = text.lower()
    
    # Create a set of unique characters in the text
    unique_chars = set(text)
    
    # Count each character and create a dictionary
    frequency = {}
    for char in unique_chars:
        frequency[char] = text.count(char)
    
    return frequency


def count_letter_frequency_in_file(filename):
    """
    Count frequency of each letter in a file.
    
    Args:
        filename (str): Path to the text file
        
    Returns:
        dict: Dictionary with characters as keys and their counts as values
    """
    frequency = {}
    
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            
            for char in text:
                if char.isalpha():
                    if char in frequency:
                        frequency[char] += 1
                    else:
                        frequency[char] = 1
        
        return frequency
    
    except FileNotFoundError:
        return {"error": "File not found"}


if __name__ == "__main__":
    # Demo string reversal
    text = "Hello, World!"
    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}")
    
    # Demo vowel/consonant splitting
    text = "Python Programming"
    vowels, consonants = split_vowels_consonants(text)
    print(f"\nText: {text}")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    
    # Demo matching ends checker
    words = ["level", "Python", "radar", "programming", "AmericA"]
    print("\nWords with matching first and last characters:")
    for word in words:
        if has_matching_ends(word):
            print(f"- {word}")
    
    # Count of words with matching ends
    print(f"\nCount of words with matching ends: {count_matching_strings(words)}")
    
    # Demo search and replace (commented out as it requires file I/O)
    # result, message = search_replace_word("sample.txt", "old", "new", auto_replace=True)
    # print(f"\nFile operation: {message}")