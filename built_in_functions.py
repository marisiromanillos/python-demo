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

#to abstract date instead of using row[0], row[1], row[2], we can use a syntax shortcut [0:3]

row_a = ['Facebook', 0.0, 'USD', 2974676, 3.5]
slicePartially = row_a[0:3]
print(slicePartially)
#output ['Facebook', 0.0, 'USD']

row_b = ['Instagram', 0.0, 'USD', 2974676, 3.5]
sliceFirst3 = row_b[:3]
print(sliceFirst3)
#['Instagram', 0.0, 'USD']

sliceFromLastsIndex = row_b[3:]
print(sliceFromLastsIndex)
#[2974676, 3.5]

slicelast3 = row_b[-3:]
print(slicelast3)
#['USD', 2974676, 3.5]

#we can store our five variables in a single list:

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

data_set = [row_1, row_2, row_3, row_4, row_5]
print(data_set)
print(data_set[0])
print(data_set[3])
print(data_set[1])

'''

outputs the 4 index from  index 0 (row_1)
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
3.5

'''
print(data_set[0][4])

'''

Group the five lists together in a list of lists. Assign the resulting list of lists to a variable named app_data_set.
Compute the average rating of the apps by retrieving the right data points from the app_data_set list of lists.

'''

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
list_of_lists = row_1[4] + row_2[4] + row_3[4] + row_4[4] + row_5[4]
print(list_of_lists)
avg_rating = list_of_lists / 5
print(avg_rating)
#output sum 21
#output division 4.2

#open()

'''

The open() function opens a file, and returns it as a file object.

The type of file object returned by the open() function depends on the mode. When open() is used to open a file in a text mode ('w', 'r', 'wt', 'rt', etc.), it returns a subclass of io.TextIOBase (specifically io.TextIOWrapper). When used to open a file in a binary mode with buffering, the returned class is a subclass of io.BufferedIOBase. The exact class varies: in read binary mode, it returns an io.BufferedReader; in write binary and append binary modes, it returns an io.BufferedWriter, and in read/write mode, it returns an io.BufferedRandom. When buffering is disabled, the raw stream, a subclass of io.RawIOBase, io.FileIO, is returned.

syntax -> open(file, mode)
file The path and name of the file
mode A string, define which mode you want to open the file in

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''

#open() example

'''
opened_file = open('AppleStore.csv')
print(opened_file)

Output
<_io.TextIOWrapper name='AppleStore.csv' mode='r' encoding='UTF-8'>

'''

#read()

'''

The open() function returns a file object, which has read() method for reading the content of the file

opened_file.read() -> returns a string

example: The command opened_file.read() returned a string which we assigned to read_file. Let's take a look at its first 300 characters. To do this we'll use slices like we did on lists. It also work on strings!
opened_file = open('AppleStore.csv')

read_file = opened_file.read()
print(read_file[:300])

output
id,track_name,size_bytes,currency,price,rating_count_tot,rating_count_ver,user_rating,user_rating_ver,ver,cont_rating,prime_genre,sup_devices.num,ipadSc_urls.num,lang.num,vpp_lic
284882215,Facebook,389879808,USD,0.0,2974676,212,3.5,3.5,95.0,4+,Social Networking,37,1,29,1
389801252,Instagram,11395481

'''

#close()

'''

To close a file we use the close() command, with the same syntax as read()

opened_file = open('AppleStore.csv')
read_file = opened_file.read()
print(read_file[:300])
opened_file.close()

'''



#split()

'''

To work on a list of lists we can use split()

opened_file = open('AppleStore.csv')
read_file = opened_file.read()
new_line_split = read_file.split("\n")
print(new_line_split[:5])

Output
['id,track_name,size_bytes,currency,price,rating_count_tot,rating_count_ver,user_rating,user_rating_ver,ver,cont_rating,prime_genre,sup_devices.num,ipadSc_urls.num,lang.num,vpp_lic', '284882215,Facebook,389879808,USD,0.0,2974676,212,3.5,3.5,95.0,4+,Social Networking,37,1,29,1', '389801252,Instagram,113954816,USD,0.0,2161558,1289,4.5,4.0,10.23,12+,Photo & Video,37,0,29,1', '529479190,Clash of Clans,116476928,USD,0.0,2130805,579,4.5,4.5,9.24.12,9+,Games,38,5,18,1', '420009108,Temple Run,65921024,USD,0.0,1724546,3842,4.5,4.0,1.6.2,9+,Games,40,5,1,1']

'''

