"""
Geometry Module - Classes and utilities for geometric calculations.

This module provides various geometry-related classes including:
- Rectangle with area and perimeter calculations
- Point with distance calculations
- Circle with area and circumference calculations
"""

import math


class Point:
    """2D point with x and y coordinates."""
    
    def __init__(self, x, y):
        """
        Initialize a new Point.
        
        Args:
            x (float): x-coordinate
            y (float): y-coordinate
        """
        self.x = x
        self.y = y
    
    def distance_to(self, other_point):
        """
        Calculate distance to another point.
        
        Args:
            other_point (Point): Another point to calculate distance to
            
        Returns:
            float: Euclidean distance between points
        """
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
    def __str__(self):
        """String representation of a Point."""
        return f"({self.x}, {self.y})"


class Rectangle:
    """Rectangle with width and height."""
    
    def __init__(self, length=1.0, breadth=1.0):
        """
        Initialize a new Rectangle.
        
        Args:
            length (float): Length of the rectangle (default 1.0)
            breadth (float): Breadth/width of the rectangle (default 1.0)
        """
        self.length = length
        self.breadth = breadth
    
    def area(self):
        """
        Calculate rectangle area.
        
        Returns:
            float: Area of the rectangle
        """
        return self.length * self.breadth
    
    def perimeter(self):
        """
        Calculate rectangle perimeter.
        
        Returns:
            float: Perimeter of the rectangle
        """
        return 2 * (self.length + self.breadth)
    
    def __str__(self):
        """String representation of a Rectangle."""
        return f"Rectangle(length={self.length}, breadth={self.breadth})"


class Circle:
    """Circle with radius and center point."""
    
    def __init__(self, radius, x=0, y=0):
        """
        Initialize a new Circle.
        
        Args:
            radius (float): Radius of the circle
            x (float): x-coordinate of the center
            y (float): y-coordinate of the center
        """
        self.radius = radius
        self.center = Point(x, y)
        
        # Calculate derived properties
        self._calculate_derived_properties()
    
    def _calculate_derived_properties(self):
        """Calculate derived properties (diameter, area, circumference)."""
        self.diameter = 2 * self.radius
        self.area = math.pi * (self.radius ** 2)
        self.circumference = 2 * math.pi * self.radius
    
    def contains_point(self, point):
        """
        Check if a point is inside the circle.
        
        Args:
            point (Point): Point to check
            
        Returns:
            bool: True if the point is inside the circle, False otherwise
        """
        distance = self.center.distance_to(point)
        return distance <= self.radius
    
    def __str__(self):
        """String representation of a Circle."""
        return f"Circle(center={self.center}, radius={self.radius})"


class Triangle:
    """Triangle defined by three points."""
    
    def __init__(self, a, b, c):
        """
        Initialize a new Triangle.
        
        Args:
            a (Point): First vertex
            b (Point): Second vertex
            c (Point): Third vertex
        """
        self.a = a
        self.b = b
        self.c = c
        
        # Calculate side lengths
        self.side_ab = a.distance_to(b)
        self.side_bc = b.distance_to(c)
        self.side_ca = c.distance_to(a)
    
    def area(self):
        """
        Calculate the area of the triangle using Heron's formula.
        
        Returns:
            float: Area of the triangle
        """
        # Semi-perimeter
        s = (self.side_ab + self.side_bc + self.side_ca) / 2
        
        # Heron's formula
        return math.sqrt(s * (s - self.side_ab) * (s - self.side_bc) * (s - self.side_ca))
    
    def perimeter(self):
        """
        Calculate the perimeter of the triangle.
        
        Returns:
            float: Perimeter of the triangle
        """
        return self.side_ab + self.side_bc + self.side_ca
    
    def is_valid(self):
        """
        Check if the triangle is valid (sum of two sides is greater than the third).
        
        Returns:
            bool: True if the triangle is valid, False otherwise
        """
        return (self.side_ab + self.side_bc > self.side_ca and
                self.side_bc + self.side_ca > self.side_ab and
                self.side_ca + self.side_ab > self.side_bc)
    
    def __str__(self):
        """String representation of a Triangle."""
        return f"Triangle(vertices=[{self.a}, {self.b}, {self.c}])"


def distance_between_points(x1, y1, x2, y2):
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


if __name__ == "__main__":
    # Demo Point
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(f"Distance between {p1} and {p2}: {p1.distance_to(p2)}")
    
    # Demo Rectangle
    rect = Rectangle(5, 10)
    print(f"\n{rect}")
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    
    # Demo Circle
    circle = Circle(5, 1, 2)
    print(f"\n{circle}")
    print(f"Diameter: {circle.diameter}")
    print(f"Area: {circle.area}")
    print(f"Circumference: {circle.circumference}")
    
    # Check if point is inside circle
    test_point = Point(2, 3)
    print(f"Is {test_point} inside the circle? {circle.contains_point(test_point)}")
    
    # Demo Triangle
    triangle = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
    print(f"\n{triangle}")
    print(f"Area: {triangle.area()}")
    print(f"Perimeter: {triangle.perimeter()}")
    print(f"Is valid triangle? {triangle.is_valid()}")