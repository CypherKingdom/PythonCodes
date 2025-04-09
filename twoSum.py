"""
    Find two numbers in the list that add up to the target.

    :param numbers: List of integers
    :param target: Target sum
    :return: Tuple of two numbers that add up to the target, or None if no such pair exists
"""

def two_sum(numbers, target):
    num_map = {number: i for i, number in enumerate(numbers) if (target - number) not in numbers[:i]}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_map and num_map[complement] != i:
            return (i, num_map[complement])
    return None

    """
    Method 2: Using a generator expression to find the 
    first pair of indices that sum to the target.
    num_map = {}
    return next(((i, num_map[complement]) 
                 for i, num in enumerate(numbers)
                 if (complement := target - num) in num_map 
                 or not num_map.setdefault(num, i)), None)
    """

print(two_sum([1, 2, 3, 4, 5], 6))