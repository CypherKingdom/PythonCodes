"""
Student-related models for educational applications.
Contains the Student base class and the Undergrad derived class.
"""

class Student:
    """Base Student class with common attributes for all student types."""
    
    def __init__(self, name, major, gpa, id=None, age=None):
        """
        Initialize a new Student.
        
        Args:
            name (str): Student's full name
            major (str): Student's major field of study
            gpa (float): Student's grade point average
            id (int, optional): Student ID number
            age (int, optional): Student's age
        """
        self._name = name
        self._major = major
        self._gpa = gpa
        self._id = id
        self._age = age
    
    def getName(self):
        """Get student's name."""
        return self._name
    
    def getMajor(self):
        """Get student's major."""
        return self._major
    
    def getGpa(self):
        """Get student's GPA."""
        return self._gpa
    
    def setGpa(self, gpa):
        """Set student's GPA."""
        self._gpa = gpa
    
    def __str__(self):
        """String representation of a Student."""
        base_str = f"Student Name: {self._name} | Major: {self._major} | GPA: {self._gpa}"
        if self._id is not None:
            base_str = f"ID: {self._id} | " + base_str
        if self._age is not None:
            base_str += f" | Age: {self._age}"
        return base_str


class Undergrad(Student):
    """Undergraduate student with additional course tracking and year."""
    
    def __init__(self, name, major, gpa, year, id=None, age=None):
        """
        Initialize a new Undergraduate student.
        
        Args:
            name (str): Student's full name
            major (str): Student's major field of study
            gpa (float): Student's grade point average
            year (int): Student's graduation year
            id (int, optional): Student ID number
            age (int, optional): Student's age
        """
        super().__init__(name, major, gpa, id, age)
        self._year = year
        self._numberOfCourses = 0
        self._courses = []
    
    def getYear(self):
        """Get student's graduation year."""
        return self._year
    
    def setYear(self, year):
        """Set student's graduation year."""
        self._year = year
    
    def getCourses(self):
        """Get list of student's courses."""
        return self._courses
    
    def addCourse(self, course):
        """Add a course to the student's course list."""
        self._courses.append(course)
        self._numberOfCourses += 1
    
    def printCourses(self):
        """Print all of student's courses."""
        for course in self.getCourses():
            print(course)
    
    def __str__(self):
        """String representation of an Undergraduate student."""
        return (super().__str__() + 
                f" | Number of Courses: {self._numberOfCourses} | Year: {self._year}")


class Course:
    """Course class representing an academic course offering."""
    
    def __init__(self, name, code, credits):
        """
        Initialize a new Course.
        
        Args:
            name (str): Course name
            code (str): Course code identifier
            credits (int): Number of credits for the course
        """
        self._name = name
        self._code = code
        self._credits = credits
    
    def __str__(self):
        """String representation of a Course."""
        return f"Course: {self._name} ({self._code}) - {self._credits} credits"


# Example usage
def demo():
    """Demonstrate the usage of the Student and Undergrad classes."""
    # Create an undergraduate student
    student = Undergrad("John Doe", "Computer Science", 3.8, 2024)
    
    # Add courses to the student
    student.addCourse(Course("Python Programming", "CSCI101", 3))
    student.addCourse(Course("Data Structures", "CSCI201", 4))
    
    # Print student information
    print(student)
    print("\nCourses:")
    student.printCourses()


if __name__ == "__main__":
    demo()