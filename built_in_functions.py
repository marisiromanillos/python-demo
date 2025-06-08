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
output 17.0
"""
print(float(19))

#int()
"""
Turns numbers into integers
output = 15
"""
print(int(31.6))

#round()
"""
Turns numbers into round numbers
output = 16
output = 15
"""
print(round(15.6))
print(round(15.3))

#float()
"""
Turns numbers into floats
"""
print(float(49))

#len()
"""

Return the length (the number of items) of an object.
The argument may be a sequence (such as a string, bytes, tuple,
list, or range) or a collection (such as a dictionary, set, or frozen set).
This is good for small lists

"""

arrayList = [1,2,3,4,5]

print(len(arrayList))

#The index numbers help us retrieve individual elements from a list. Looking back at the list row_1 from the code example above, we can retrieve the first element (the string 'Facebook') with the index number 0 by running the code print(row_1[0]).
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
print(row_1[0])

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]

difference = row_2[4] - row_1[4]
average_rating = (row_1[4] + row_2[4]) / 2

print(difference)
print(average_rating)