"""
Algorithm Utilities Module - Collection of common algorithms for problem solving.

This module provides implementations of various algorithms including:
- Two Sum problem solution
- Array/list manipulation algorithms
"""

def two_sum(numbers, target):
    """
    Find two numbers in the list that add up to the target.
    
    Args:
        numbers (list): List of integers
        target (int): Target sum
        
    Returns:
        tuple: Indices of two numbers that add up to the target, or None if no such pair exists
    """
    # Use a hash map to store numbers and their indices
    num_map = {}
    
    for i, num in enumerate(numbers):
        complement = target - num
        
        # Check if the complement exists in our map
        if complement in num_map:
            return (i, num_map[complement])
        
        # Add the current number to our map
        num_map[num] = i
    
    return None


def find_max_subarray_sum(array):
    """
    Find the maximum sum of a contiguous subarray using Kadane's algorithm.
    
    Args:
        array (list): List of integers
        
    Returns:
        int: Maximum sum of a contiguous subarray
    """
    if not array:
        return 0
        
    max_so_far = array[0]
    max_ending_here = array[0]
    
    for i in range(1, len(array)):
        max_ending_here = max(array[i], max_ending_here + array[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


def binary_search(array, target):
    """
    Perform binary search on a sorted array.
    
    Args:
        array (list): Sorted list of elements
        target: Element to find
        
    Returns:
        int: Index of the target if found, -1 otherwise
    """
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def merge_sort(array):
    """
    Sort an array using the merge sort algorithm.
    
    Args:
        array (list): List to sort
        
    Returns:
        list: Sorted list
    """
    if len(array) <= 1:
        return array
        
    # Split the array into two halves
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays.
    
    Args:
        left (list): First sorted list
        right (list): Second sorted list
        
    Returns:
        list: Merged sorted list
    """
    result = []
    i = j = 0
    
    # Compare elements from both lists and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    # Demo two_sum
    numbers = [2, 7, 11, 15]
    target = 9
    result = two_sum(numbers, target)
    print(f"Two Sum: In {numbers}, indices {result} add up to {target}")
    
    # Demo max subarray sum
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Max subarray sum in {array}: {find_max_subarray_sum(array)}")
    
    # Demo binary search
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    index = binary_search(sorted_array, target)
    print(f"Binary search: {target} found at index {index} in {sorted_array}")
    
    # Demo merge sort
    unsorted = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(unsorted)
    print(f"Merge sort: {unsorted} → {sorted_array}")