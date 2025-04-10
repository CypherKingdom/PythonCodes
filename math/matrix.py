"""
Matrix operations utility module.
Contains functions for matrix validation, multiplication, and analysis.
"""

import random


def create_random_matrix(rows, cols, min_val=0, max_val=100):
    """
    Create a random matrix with the specified dimensions.
    
    Args:
        rows (int): Number of rows
        cols (int): Number of columns
        min_val (int): Minimum random value (inclusive)
        max_val (int): Maximum random value (inclusive)
        
    Returns:
        list: A matrix (list of lists) with random values
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """
    Print a matrix in a readable format.
    
    Args:
        matrix (list): Matrix to print
    """
    for row in matrix:
        print(row)


def is_square_matrix(matrix):
    """
    Check if the matrix is square (rows = columns).
    
    Args:
        matrix (list): Matrix to check
        
    Returns:
        bool: True if square, False otherwise
    """
    # Check if matrix is empty
    if not matrix:
        return False
    
    # Get the number of rows
    rows = len(matrix)
    
    # Check if all rows have the same number of columns
    for row in matrix:
        if len(row) != rows:
            return False
    
    return True


def is_diagonal_matrix(matrix):
    """
    Check if the matrix is diagonal (non-zero elements only on the main diagonal).
    
    Args:
        matrix (list): Matrix to check
        
    Returns:
        bool: True if diagonal, False otherwise
    """
    if not is_square_matrix(matrix):
        return False
    
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != 0:
                return False
    
    return True


def diagonal_sum(matrix):
    """
    Calculate the sum of elements on the main diagonal.
    
    Args:
        matrix (list): Matrix to sum
        
    Returns:
        float: Sum of diagonal elements
    """
    if not is_square_matrix(matrix):
        raise ValueError("Matrix must be square to calculate diagonal sum")
    
    return sum(matrix[i][i] for i in range(len(matrix)))


def can_multiply(matrix1, matrix2):
    """
    Check if two matrices can be multiplied (cols of first = rows of second).
    
    Args:
        matrix1 (list): First matrix
        matrix2 (list): Second matrix
        
    Returns:
        bool: True if matrices can be multiplied, False otherwise
    """
    # Check if matrices are empty
    if not matrix1 or not matrix2:
        return False
    
    # Get dimensions
    cols1 = len(matrix1[0]) if matrix1 and matrix1[0] else 0
    rows2 = len(matrix2)
    
    return cols1 == rows2


def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices.
    
    Args:
        matrix1 (list): First matrix
        matrix2 (list): Second matrix
        
    Returns:
        list: Result of matrix multiplication
    """
    if not can_multiply(matrix1, matrix2):
        raise ValueError("Matrices are not compatible for multiplication")
    
    rows1 = len(matrix1)
    cols2 = len(matrix2[0])
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result


# Example usage
def demo():
    """Demonstrate matrix operations."""
    # Create random matrices
    matrix1 = create_random_matrix(3, 3)
    matrix2 = create_random_matrix(3, 2)
    
    print("Matrix 1:")
    print_matrix(matrix1)
    
    print("\nMatrix 2:")
    print_matrix(matrix2)
    
    # Check if matrix1 is square
    print(f"\nMatrix 1 is square: {is_square_matrix(matrix1)}")
    
    # Check if matrix1 is diagonal
    print(f"Matrix 1 is diagonal: {is_diagonal_matrix(matrix1)}")
    
    # Check if matrices can be multiplied
    if can_multiply(matrix1, matrix2):
        print("\nMatrices can be multiplied")
        result = multiply_matrices(matrix1, matrix2)
        print("\nResult of multiplication:")
        print_matrix(result)
    else:
        print("\nMatrices cannot be multiplied")
    
    # Create a diagonal matrix
    diagonal_matrix = [[5, 0, 0], [0, 10, 0], [0, 0, 15]]
    print("\nDiagonal matrix:")
    print_matrix(diagonal_matrix)
    print(f"Is diagonal: {is_diagonal_matrix(diagonal_matrix)}")
    print(f"Diagonal sum: {diagonal_sum(diagonal_matrix)}")


if __name__ == "__main__":
    demo()