# strings
"""

# The string starts with double a quotation mark (")
example = "Facebook's parent company, Meta, created numerous AI chatbots with 'unique personalities'."

example = "Facebook's parent company, Meta, created numerous AI chatbots with 'unique personalities'."
print(example)

Output
Facebook's parent company, Meta, created numerous AI chatbots with 'unique personalities'.

Fortunately, we can cancel the special function of the second single quotation mark (its special function is to end the string) by typing a backslash character '\' in front of it:

# Notice the backslash character in 'Facebook\'s'
example = 'Facebook\'s parent company, Meta, created numerous AI chatbots with "unique personalities".'
print(example)

"""

example = 'Facebook\'s parent company, Meta, created numerous AI chatbots with "unique personalities".'
print(example)


# When we have two or more distinct strings, it's possible to link them using the + operator:

print('a' + 'b')
print('a' + ' ' + 'b')
print('This' + 'is' + 'a' + 'sentence.')
print('This' + ' ' + 'is' + ' ' + 'a' + ' ' + 'sentence.')

print('a' * 1)
print('a' * 4)
print('a ' * 5)

#We can't perform arithmetical operations between strings and integers, or strings and floats (decimal numbers).

print('a' * 0) # No output for this line
print('a' * -1) # No output for this line

# Using triple quotation marks also allows us to use both single and double quotation marks without needing to escape them.

motto = '''Facebook's old motto was 'move fast and break things'.'''
print(motto)