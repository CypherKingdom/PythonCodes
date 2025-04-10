"""
Mathematical utilities module.
Contains functions for various mathematical calculations and operations.
"""

import math
import random


def factorial(n):
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): Number to calculate factorial for
        
    Returns:
        int: Factorial of n
    """
    if n <= 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


def factorial_recursive(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): Number to calculate factorial for
        
    Returns:
        int: Factorial of n
    """
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def sum_of_series(n):
    """
    Calculate the sum of the series 1/1! + 1/2! + ... + 1/n!
    
    Args:
        n (int): Upper limit of the series
        
    Returns:
        float: Sum of the series
    """
    total = 0
    for i in range(1, n + 1):
        total += 1 / factorial(i)
    
    return total


def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    Args:
        year (int): Year to check
        
    Returns:
        bool: True if leap year, False otherwise
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def solve_quadratic_equation(a, b, c):
    """
    Solve a quadratic equation of the form ax² + bx + c = 0
    
    Args:
        a (float): Coefficient of x²
        b (float): Coefficient of x
        c (float): Constant term
        
    Returns:
        tuple: Solutions to the quadratic equation
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate solutions based on discriminant
    if discriminant > 0:
        # Two real and different solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # One real solution (repeated)
        x = -b / (2*a)
        return x
    else:
        # Complex solutions
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return (complex(real_part, imaginary_part), 
                complex(real_part, -imaginary_part))


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float: Average of the numbers
    """
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)


def count_above_average(numbers):
    """
    Count how many numbers in a list are greater than or equal to the average.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int: Count of numbers above or equal to the average
    """
    avg = calculate_average(numbers)
    return sum(1 for num in numbers if num >= avg)


def calculate_distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points.
    
    Args:
        x1 (float): x-coordinate of first point
        y1 (float): y-coordinate of first point
        x2 (float): x-coordinate of second point
        y2 (float): y-coordinate of second point
        
    Returns:
        float: Distance between the two points
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def generate_math_problem():
    """
    Generate a random subtraction problem for children.
    
    Returns:
        tuple: Two numbers and their difference
    """
    x1 = random.randint(0, 9)
    x2 = random.randint(0, 9)
    
    # Ensure x1 is greater than or equal to x2
    if x2 > x1:
        x1, x2 = x2, x1
    
    return x1, x2, x1 - x2


# Example usage
def demo():
    """Demonstrate math utilities."""
    # Factorial examples
    n = 5
    print(f"Factorial of {n}: {factorial(n)}")
    print(f"Factorial of {n} (recursive): {factorial_recursive(n)}")
    
    # Series sum example
    print(f"Sum of series 1/1! + 1/2! + ... + 1/5!: {sum_of_series(5)}")
    
    # Leap year example
    year = 2024
    print(f"Is {year} a leap year? {is_leap_year(year)}")
    
    # Quadratic equation example
    a, b, c = 1, -3, 2
    print(f"Solutions to {a}x² + {b}x + {c} = 0: {solve_quadratic_equation(a, b, c)}")
    
    # Average calculation example
    numbers = [5, 10, 15, 20, 25]
    avg = calculate_average(numbers)
    above_avg = count_above_average(numbers)
    print(f"Average of {numbers}: {avg}")
    print(f"Numbers above or equal to average: {above_avg}")
    
    # Distance calculation example
    x1, y1 = 0, 0
    x2, y2 = 3, 4
    print(f"Distance between ({x1},{y1}) and ({x2},{y2}): {calculate_distance(x1, y1, x2, y2)}")
    
    # Math problem generation example
    num1, num2, diff = generate_math_problem()
    print(f"Math problem: {num1} - {num2} = {diff}")


if __name__ == "__main__":
    demo()