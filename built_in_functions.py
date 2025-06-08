# abs()

"""
How abs() works:

For integers and floats:

If the number is positive or zero, it returns the same number
If the number is negative, it returns the number with the sign flipped to positive


For complex numbers:

It returns the magnitude (also called modulus) of the complex number
For a complex number a+bi, the magnitude is √(a² + b²)


For custom objects:

If your object implements the __abs__() method, abs() will call that method

"""

# Integers
abs(5)      # Returns 5
abs(-5)     # Returns 5
abs(0)      # Returns 0

# Floating-point numbers
abs(3.14)   # Returns 3.14
abs(-3.14)  # Returns 3.14

# Complex numbers
print(abs(3 + 4j))  # Returns 5.0 (√(3² + 4²) = √(9 + 16) = √25 = 5)

#type()

"""

Type Objects represents the various objects types.

There are no special operations on types - type() defines names for all

standard built-in types

"""
numberType = 5
print(type(numberType))

#float()
"""
Turns numbers into floats
"""
print(float(17))