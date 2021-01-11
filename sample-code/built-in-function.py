# 1. isinstance check if an object is of type list

numbers = [1, 2, 3, 4, 5]

print(isinstance(numbers, list))


print(isinstance(numbers, float))

print(isinstance(numbers, (list, float)))


# 2. zip

# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']

# list of prices
prices = [50, 20, 200, 150, 10]

# iterator of tuples - containing each tuple a product and its price
zip(products, prices)
# <zip at 0x1ab80c8b788>

# to visualize the iterator we have to convert it into a list
lst_zip = list(zip(products, prices))
print(lst_zip)
# [('table', 50), ('chair', 20), ('sofa', 200), ('bed', 150), ('lamp', 10)]

# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']

# list of prices
prices = [50, 20, 200, 150, 10]

for product, price in zip(products, prices):
    print('Product: {}, Price: {}'.format(product, price))


# Product: table, Price: 50
# Product: chair, Price: 20
# Product: sofa, Price: 200
# Product: bed, Price: 150
# Product: lamp, Price: 10

# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']

# list of prices
prices = [50, 20, 200, 150, 10]

# create a dictionary from two lists
dic = dict(zip(products, prices))
print(dic)
# {'table': 50, 'chair': 20, 'sofa': 200, 'bed': 150, 'lamp': 10}


# list of tuples containing products and prices
products_and_prices = [('table', 50), ('chair', 20), ('sofa', 200), ('bed', 150), ('lamp', 10)]

# unzip the list of tuples into two tuples with the zip function and the unpacking operator *
products, prices = zip(*products_and_prices)

# tuple of products
print(products)

# tuple of prices
print(prices)


# 3. map

# list of numbers
numbers = [1,2,3,4,5]

# add 1
lst = list(map(lambda x : x + 1, numbers))
print(lst)

# multiple by 2
lst = list(map(lambda x: x * 2, numbers))
print(lst)

#obtain the cube
lst = list(map(lambda x: x ** 3, numbers))
print(lst)


# list of numbers
numbers = [1,2, 3,  4, 5]

# add 1 function - regular function
def add_one(element):
    return element + 1 

# add 1 to each element of the list
print(list(map(add_one,numbers)))


# lists of numbers
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

# multiply the elements of both lists
print(list(map(lambda x, y : x * y, numbers_1, numbers_2)))

# 4. filter

# list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# get odd numbers
lst = list(filter(lambda x: x % 2, numbers))
print(lst)
# [1, 3, 5]

# list of cities
cities ={'Madrid', 'Valencia', 'Barcelona', 'Munich', 'Stuttgart'}

# cities that start with M or V
tup = tuple(filter(lambda x: x.startswith(('M', 'V')), cities))

print(tup)
# ('Madrid', 'Valencia', 'Munich')

# 5. input

# # ask the user to input a name
# name = input('Enter your name: ')

# # use the name in the following greeting
# print('Hello {}'.format(name))

# #Hello Danny


# # ask the user to input a number
# number_1 = float(input('Enter a number: '))
# # Enter a number: 2.5

# # ask the user to input another number
# number_2 = float(input('Enter another number: '))
# # Enter another number: 3.4

# # print the sum of both numbers
# print('The sum is: {}'.format(number_1 + number_2))
# # The sum is: 5.9

# 6. id

# list of numbers
numbers = [1, 2, 3, 4, 5]

# new list of numbers
new_numbers = numbers

# both list have the same id number
print('numbers id: {}, new_numbers id: {}'.format(id(numbers), id(new_numbers)))
# numbers id: 1836112528136, new_numbers id: 1836112528136

# we can also check that they refer to the same object with the identity operator is
print(numbers is new_numbers)
# True


# 7. hex 

# convert the integer 10 into a hexadecimal number
hex_number = hex(10)

print(hex_number)
# 0xa
print(type(hex_number))
# <class 'str'>

# An exception is raised if a float is provided as input
#hex_number = hex(10.0)
# TypeError


def rgb_to_hex(rgb_triple):
    """Function that maps a RGB tuple representation to a hexadecimal string
    Parameters:
    rgb_triple (tuple): RGB tuple representation (red, green, and blue)
    Returns:
    hex_string (string): Hexadecimal string representation '0xRRGGBB'
    """
    hex_string = ''
    # we loop through the red, green, blue values of the tuple rgb_tuple
    for integer in rgb_triple:
        hexadecimal = hex(integer)[2:] # string slicing to elimininate the prefix '0x'
        if len(hexadecimal) == 1:
            hexadecimal = '0' + hexadecimal # pad the string to the left with a 0
        hex_string += hexadecimal
    return '#' + hex_string

# call the function
color_1 = (255, 255, 255)
color_2 = (255, 255, 0)
color_3 = (70, 90, 200)

color_1_hex = rgb_to_hex(color_1)
# '#ffffff'

color_2_hex = rgb_to_hex(color_2)
# '#ffff00'

color_3_hex = rgb_to_hex(color_3)
# '#465ac8'

print(color_1_hex, color_2_hex, color_3_hex)

# 9. format

# fixed-point notation rounded off to two decimal places 
format(123.45789,'.2f')
# '123.46'

# percentage rounded off to one decimal place
format(0.1569,'.1%')
# '15.7%'

# hexadecimal number 
format(10,'x')
# 'a'

# exponential notation rounded off two decimal places with sign for both positive and negative numbers
format(123.45789,'+.2e')
# '+1.23e+02'

# number with fill character, width, and right-alignment
format(123.45789,'*>30')
# '*********************123.45789'

# 10. open 

# create a new file in writing mode
f = open('new_file.txt', 'w')
f.write('This is a new file!')

# close the file to avoid running out of file handles
f.close()

 # open a file in reading mode 
f = open('reading_lines.txt', 'r')
content = f.read()
print(content)
# Successful file reading!

# close the file to avoid running out of file handles
f.close()


# open a file in reading mode
f = open('reading_lines.txt', 'r')
content = f.readlines()
print(content)
# ['First line\n', 'Second line\n', 'Third line\n']

# close the file to avoid running out of file handles
f.close()


# open a file in reading mode
f = open('./reading_lines.txt', 'r')
first_line = f.readline()
print(first_line)
# First line
second_line = f.readline()
print(second_line)
# Second line
third_line = f.readline()
print(third_line)
# Third line

# close the file to avoid running out of file handles
f.close()


# the with statement automatically closes the file after the nested block of code is executed.
with open('./reading_lines.txt', 'r') as f:
    content = f.readlines()
    print(content)
    # ['First line\n', 'Second line\n', 'Third line\n']

