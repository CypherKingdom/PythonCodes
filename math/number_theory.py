"""
Number Theory Module - Collection of number theory functions and algorithms.

This module provides various number-related functions including:
- Factorial calculation
- Digit sum calculation
- Collatz conjecture implementation
- Even/odd checker
- Pyramid height calculator
"""

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


def sum_of_digits(number):
    """
    Recursively calculates the sum of all digits in a positive integer.
    
    Args:
        number (int): A positive integer
        
    Returns:
        int: The sum of all digits in the number
    """
    if number <= 0:
        return 0  # Base case: return 0 for non-positive numbers
    
    return number % 10 + sum_of_digits(number // 10)


def collatz_conjecture(n):
    """
    Implements the Collatz Conjecture (3n+1 problem).
    
    For a given positive integer n:
    - If n is even, divide it by 2
    - If n is odd, multiply by 3 and add 1
    - Repeat until n reaches 1
    
    Args:
        n (int): A positive integer greater than 1
        
    Returns:
        int: Number of steps to reach 1
    """
    steps = 0
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
        
        sequence.append(n)
        steps += 1
    
    return steps, sequence


def is_even(number):
    """
    Recursively determines if a number is even or odd.
    
    Args:
        number (int): An integer to check
        
    Returns:
        bool: True if the number is even, False if odd
    """
    if number == 0:
        return True  # 0 is considered even
    if number == 1:
        return False  # 1 is considered odd
        
    if number < 0:
        return is_even(-number)
    
    return is_even(number - 2)  # Subtract 2 recursively


def pyramid_height(blocks):
    """
    Calculates the maximum height of a pyramid that can be built with given blocks.
    
    The pyramid is stacked according to one simple principle: 
    each lower layer contains one block more than the layer above.
    
    Args:
        blocks (int): Number of available blocks
        
    Returns:
        int: Maximum height of pyramid
    """
    height, level = 0, 1
    while level <= blocks:
        blocks -= level
        height += 1
        level += 1
    return height


def is_prime(n):
    """
    Checks if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if number is prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


def gcd(a, b):
    """
    Calculates the greatest common divisor of two integers.
    
    Args:
        a (int): First integer
        b (int): Second integer
        
    Returns:
        int: Greatest common divisor
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Calculates the least common multiple of two integers.
    
    Args:
        a (int): First integer
        b (int): Second integer
        
    Returns:
        int: Least common multiple
    """
    return a * b // gcd(a, b)


if __name__ == "__main__":
    # Demo each function
    print("Factorial examples:")
    for i in range(6):
        print(f"{i}! = {factorial(i)}")
    
    print("\nDigit sum examples:")
    for num in [123, 9999, 1051]:
        print(f"Sum of digits in {num} = {sum_of_digits(num)}")
    
    print("\nCollatz Conjecture example:")
    steps, sequence = collatz_conjecture(27)
    print(f"27 takes {steps} steps to reach 1")
    print(f"Sequence: {sequence}")
    
    print("\nEven/Odd checker:")
    for num in [0, 1, 2, 15, 22, -3]:
        print(f"{num} is {'even' if is_even(num) else 'odd'}")
    
    print("\nPyramid height examples:")
    for blocks in [6, 10, 15, 21]:
        print(f"With {blocks} blocks, maximum height is {pyramid_height(blocks)}")
    
    print("\nPrime checker:")
    for num in [2, 7, 10, 13, 25]:
        print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")