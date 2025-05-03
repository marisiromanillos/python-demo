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