"""
Python Best Practices Guide

This module serves as a reference for Python best practices including:
- Code style
- Naming conventions
- Comments
- Project structure
- Function design
- Error handling
- Testing
- Performance optimization

Use this file as a template and reference for maintaining high-quality Python code.
"""

# -----------------------------------------
# NAMING CONVENTIONS
# -----------------------------------------

# Module names: lowercase with underscores
# Example: data_processing.py, user_authentication.py

# Package names: short, lowercase, no underscores
# Example: utils, models, views, controllers

# Class names: CamelCase
class UserProfile:
    """Example of a properly named class using CamelCase."""
    pass

# Function/method names: lowercase with underscores
def calculate_average(numbers):
    """Example of a properly named function using snake_case."""
    return sum(numbers) / len(numbers)

# Variable names: lowercase with underscores
user_name = "John Doe"  # good
userName = "John Doe"    # avoid in Python (better for JavaScript)

# Constants: uppercase with underscores
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30

# -----------------------------------------
# CODE STYLE
# -----------------------------------------

# Indentation: 4 spaces (not tabs)
def example_function():
    if True:
        print("Properly indented with 4 spaces")
        
# Line length: limit to 79 characters for code, 72 for comments

# Imports: one per line, grouped in order of standard library, third-party, local
import os
import sys
from datetime import datetime

import requests
import pandas as pd

from .local_module import local_function

# -----------------------------------------
# COMMENTS BEST PRACTICES
# -----------------------------------------

# Block comments: Use complete sentences with capital letters and periods.
# This example shows how to properly format block comments that span
# multiple lines. Notice the capitalization and punctuation.

# Inline comments: keep brief, lowercase, no period
x = x + 1  # compensate for border offset

def example_docstring_function(param1, param2):
    """
    Short description of function purpose.
    
    More detailed explanation if needed. This function provides
    an example of proper docstring formatting.
    
    Args:
        param1 (int): Description of first parameter.
        param2 (str): Description of second parameter.
        
    Returns:
        bool: Description of return value.
        
    Raises:
        ValueError: When input parameters are invalid.
    """
    # Function implementation
    return True

# TODO comments for future work
# TODO: Implement error handling for network timeouts

# -----------------------------------------
# FUNCTION DESIGN
# -----------------------------------------

# Keep functions small and focused on a single task
def validate_email(email):
    """Validate email format."""
    import re
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

# Avoid mutable default arguments
def bad_append(item, items=[]):  # DON'T DO THIS
    items.append(item)
    return items

def good_append(item, items=None):  # Do this instead
    if items is None:
        items = []
    items.append(item)
    return items

# Use type hints for better clarity (Python 3.5+)
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discounted price."""
    return price * (1 - discount_percent / 100)

# -----------------------------------------
# ERROR HANDLING
# -----------------------------------------

# Use try/except blocks properly
def safe_division(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid types for division")
        return None

# Raise exceptions with clear messages
def set_age(age):
    """Set user age with validation."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")
    # Set the age...

# -----------------------------------------
# CLASSES AND OOP
# -----------------------------------------

class Rectangle:
    """
    A class representing a rectangle.
    
    This demonstrates proper class definition with properties, methods,
    and appropriate docstrings.
    """
    
    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height
    
    @property
    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height
    
    def __str__(self):
        """String representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"

# -----------------------------------------
# TESTING
# -----------------------------------------

# Example test function (would typically be in a separate test file)
def test_rectangle_area():
    """Test the Rectangle.area property."""
    rect = Rectangle(5, 10)
    assert rect.area == 50, "Area calculation is incorrect"

# -----------------------------------------
# PERFORMANCE TIPS
# -----------------------------------------

# Use generators for memory efficiency
def first_n_squares(n):
    """Generate the first n square numbers."""
    for i in range(n):
        yield i * i

# Use list comprehensions for clarity and performance
squares = [x*x for x in range(10)]  # Better than a for loop with append

# Use proper data structures
# - Lists for ordered collections: [1, 2, 3]
# - Dictionaries for key-value pairs: {"name": "John", "age": 30}
# - Sets for unique values: {1, 2, 3}
# - Tuples for immutable sequences: (1, 2, 3)

# -----------------------------------------
# MAIN EXECUTION
# -----------------------------------------

if __name__ == "__main__":
    # Code that should run when this file is executed directly
    print("This file serves as a Python best practices reference")
    
    # Example of running a test
    test_rectangle_area()
    print("All tests passed!")