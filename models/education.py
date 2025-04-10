"""
Education Utilities Module - Tools for educational purposes.

This module provides various education-related functions including:
- Grade to GPA conversion
- Forest density analysis
- Educational data processing
"""

def convert_grades_to_gpa(grades):
    """
    Converts a list of letter grades to their equivalent GPA values.
    
    Args:
        grades (list): A list of letter grades (A, A-, B+, etc.)
        
    Returns:
        list: A list of GPA values corresponding to the letter grades
    """
    gpa_conversion = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.67,
        "B+": 3.33,
        "B": 3.0,
        "B-": 2.67,
        "C+": 2.33,
        "C": 2.0,
        "C-": 1.67,
        "D+": 1.33,
        "D": 1.0,
        "D-": 0.67,
        "F": 0.0
    }
    
    return [gpa_conversion.get(grade, 0.0) for grade in grades]


def calculate_gpa(grades):
    """
    Calculate the overall GPA from a list of letter grades.
    
    Args:
        grades (list): List of letter grades
        
    Returns:
        float: The calculated GPA
    """
    gpa_values = convert_grades_to_gpa(grades)
    if not gpa_values:
        return 0.0
    return sum(gpa_values) / len(gpa_values)


def get_countries_with_high_tree_density(min_density=20000):
    """
    Identifies countries with tree density above a specified threshold.
    
    Args:
        min_density (int): Minimum tree density threshold (trees per sq km)
        
    Returns:
        list: A list of countries with tree density above the threshold
    """
    tree_density = {
        "Finland": 90652, 
        "Taiwan": 69593, 
        "Japan": 49894, 
        "Russia": 41396, 
        "Brazil": 39542, 
        "Canada": 36388, 
        "Bulgaria": 24987, 
        "France": 24436, 
        "Greece": 24323, 
        "United States": 23513, 
        "Turkey": 11126, 
        "India": 11109, 
        "Denmark": 6129, 
        "Syria": 534, 
        "Saudi Arabia": 1, 
        "Lebanon": 20000
    }
    
    high_density_countries = []
    for country, density in tree_density.items():
        if density > min_density:
            high_density_countries.append((country, density))
            
    # Sort by density in descending order
    high_density_countries.sort(key=lambda x: x[1], reverse=True)
    return high_density_countries


def create_grade_histogram(grades):
    """
    Create a histogram (dictionary) of grade frequencies.
    
    Args:
        grades (list): List of letter grades
        
    Returns:
        dict: Dictionary with grades as keys and frequencies as values
    """
    histogram = {}
    for grade in grades:
        if grade in histogram:
            histogram[grade] += 1
        else:
            histogram[grade] = 1
    
    return histogram


def calculate_grade_statistics(grades):
    """
    Calculate statistics for a list of numerical grades.
    
    Args:
        grades (list): List of numerical grades
        
    Returns:
        dict: Dictionary containing various statistics
    """
    if not grades:
        return {
            "count": 0,
            "mean": 0,
            "median": 0,
            "min": 0,
            "max": 0,
            "range": 0
        }
    
    # Sort the grades for easier calculation
    sorted_grades = sorted(grades)
    count = len(sorted_grades)
    
    # Calculate statistics
    mean = sum(sorted_grades) / count
    
    # Calculate median
    if count % 2 == 0:
        median = (sorted_grades[count // 2 - 1] + sorted_grades[count // 2]) / 2
    else:
        median = sorted_grades[count // 2]
    
    # Min, max, range
    min_grade = sorted_grades[0]
    max_grade = sorted_grades[-1]
    grade_range = max_grade - min_grade
    
    return {
        "count": count,
        "mean": mean,
        "median": median,
        "min": min_grade,
        "max": max_grade,
        "range": grade_range
    }


def determine_letter_grade(score, scale='standard'):
    """
    Convert a numerical score to a letter grade based on a grading scale.
    
    Args:
        score (float): Numerical score (0-100)
        scale (str): Grading scale to use ('standard' or 'plus_minus')
        
    Returns:
        str: Letter grade
    """
    if scale == 'standard':
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    elif scale == 'plus_minus':
        if score >= 97:
            return 'A+'
        elif score >= 93:
            return 'A'
        elif score >= 90:
            return 'A-'
        elif score >= 87:
            return 'B+'
        elif score >= 83:
            return 'B'
        elif score >= 80:
            return 'B-'
        elif score >= 77:
            return 'C+'
        elif score >= 73:
            return 'C'
        elif score >= 70:
            return 'C-'
        elif score >= 67:
            return 'D+'
        elif score >= 63:
            return 'D'
        elif score >= 60:
            return 'D-'
        else:
            return 'F'
    
    else:
        raise ValueError("Invalid scale. Use 'standard' or 'plus_minus'")


if __name__ == "__main__":
    # Demo grade to GPA conversion
    student_grades = ["A", "C-", "B+", "B", "D"]
    gpa_values = convert_grades_to_gpa(student_grades)
    overall_gpa = calculate_gpa(student_grades)
    
    print(f"Letter Grades: {student_grades}")
    print(f"GPA Values: {gpa_values}")
    print(f"Overall GPA: {overall_gpa:.2f}")
    
    # Demo high tree density countries
    print("\nCountries with high tree density:")
    high_density_countries = get_countries_with_high_tree_density()
    for country, density in high_density_countries:
        print(f"- {country}: {density} trees per sq km")
    
    # Demo grade histogram
    class_grades = ["A", "B", "A", "C", "F", "B", "A", "B", "C", "D"]
    histogram = create_grade_histogram(class_grades)
    print("\nGrade distribution:")
    for grade, count in sorted(histogram.items()):
        print(f"{grade}: {'*' * count} ({count})")
    
    # Demo numerical grade statistics
    numerical_grades = [85, 92, 78, 65, 90, 88, 76, 94]
    statistics = calculate_grade_statistics(numerical_grades)
    print("\nGrade statistics:")
    for key, value in statistics.items():
        print(f"{key}: {value}")