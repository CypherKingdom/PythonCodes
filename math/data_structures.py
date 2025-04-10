"""
Data Structures Module - Collection of functions for list, array, and set operations.

This module provides various data structure operations including:
- List operations (filtering, transformations)
- Removing duplicates while preserving order
- Finding common elements between lists
"""

def remove_duplicates(items):
    """
    Removes duplicate values from a list while preserving order.
    
    Args:
        items (list): The list to remove duplicates from
        
    Returns:
        list: A new list with duplicates removed
    """
    seen = set()
    result = []
    
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result


def find_intersection(list1, list2):
    """
    Finds the common elements between two lists without duplicates.
    
    Args:
        list1 (list): The first list
        list2 (list): The second list
        
    Returns:
        list: A list containing the unique common elements
    """
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    
    return result


def filter_by_length(items, length, predicate=lambda x, y: len(x) == y):
    """
    Filters items in a list based on their length and a predicate.
    
    Args:
        items (list): List of items to filter
        length (int): Length to compare against
        predicate (function): Function that takes an item and length,
                            returns True if the item should be included
        
    Returns:
        list: Filtered list of items
    """
    return [item for item in items if predicate(item, length)]


def filter_even_length(items):
    """
    Filters items in a list to only include those with even length.
    
    Args:
        items (list): List of items to filter
        
    Returns:
        list: List of items with even length
    """
    return filter_by_length(items, 0, lambda x, y: len(x) % 2 == 0)


def is_divisible_by_both(number, div1, div2):
    """
    Checks if a number is divisible by both div1 and div2.
    
    Args:
        number (int): Number to check
        div1 (int): First divisor
        div2 (int): Second divisor
        
    Returns:
        bool: True if number is divisible by both div1 and div2
    """
    return number % div1 == 0 and number % div2 == 0


def number_game(start, end):
    """
    Implements a FizzBuzz-style number game (ZipZap).
    
    For each number in the range:
    - Print "ZipZap" if divisible by both 3 and 5
    - Print "Zip" if divisible by 3
    - Print "Zap" if divisible by 5
    - Print the number itself for other cases
    
    Args:
        start (int): Starting number (inclusive)
        end (int): Ending number (inclusive)
        
    Returns:
        list: Results of the game for each number
    """
    results = []
    
    for i in range(start, end + 1):
        if is_divisible_by_both(i, 3, 5):
            results.append("ZipZap")
        elif i % 3 == 0:
            results.append("Zip")
        elif i % 5 == 0:
            results.append("Zap")
        else:
            results.append(str(i))
    
    return results


if __name__ == "__main__":
    # Demo remove_duplicates
    numbers = [1, 2, 3, 2, 4, 1, 5]
    print(f"Original list: {numbers}")
    print(f"Without duplicates: {remove_duplicates(numbers)}")
    
    # Demo find_intersection
    list1 = [1, 2, 3, 3, 5, 7]
    list2 = [3, 5, 7, 3]
    print(f"\nList 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Common elements: {find_intersection(list1, list2)}")
    
    # Demo filter_even_length
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    print(f"\nWords: {words}")
    print(f"Words with even length: {filter_even_length(words)}")
    
    # Demo number_game
    print("\nNumber game (ZipZap) from 1 to 15:")
    results = number_game(1, 15)
    for i, result in enumerate(results, 1):
        print(f"{i}: {result}")