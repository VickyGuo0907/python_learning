

## 10 Python built-in functions you should know 
[link](https://towardsdatascience.com/10-python-built-in-functions-you-should-know-f6beba1698bb){target="_blank"}


### 1. isinstance

The isinstance(object, classinfo) function returns True if the object argument is an instance of the classinfo argument. 
If not, the function returns False. If classinfo is a tuple of objects, the function returns True if object is an instance of any of them.

**Example:**

```
  numers = [1, 2, 3, 4, 5]
  
  isinstance(numbers, list)
  # True

  isinstance(numbers, float)
  # False

  isinstance(numbers, (list, float))
  # True

```

### 2. zip

The zip(*iterables) function returns an iterator of tuples, where the i tuple contains the i element from each of the iterables. The length of the tuples is equal to the number of iterables passed to the function. In the following code block, two lists are passed to the zip function, obtaining an iterator of tuples each of length two.

```

# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']

# list of prices
prices = [50, 20, 200, 150, 10]

# iterator of tuples - containing each tuple a product and its price
zip(products, prices)
# <zip at 0x1ab80c8b788>

# to visualize the iterator we have to convert it into a list
list(zip(products, prices))
# [('table', 50), ('chair', 20), ('sofa', 200), ('bed', 150), ('lamp', 10)]

```

The zip function can accept any type of iterable such as lists, strings, tuples, or dictionaries, returning an iterator object. To visualize this object, we can convert it into a list with the built-in function list().

**Example:**

This function can come in handy when dealing with loops, allowing to loop through multiple iterables at once. 
We can easily loop through two list with the zip function as follows:

```

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

```

This function can also be used in combination with the built-in function dict() to create a dictionary from two lists in the following manner:


```

# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']

# list of prices
prices = [50, 20, 200, 150, 10]

# create a dictionary from two lists
dict(zip(products, prices))
# {'table': 50, 'chair': 20, 'sofa': 200, 'bed': 150, 'lamp': 10}
```

The function zip can also be used to unzip a sequence into independent 
sequences using the unpacking operator *. In the following block of code, we unzip a list of tuples into two tuples.

```

# list of tuples containing products and prices
products_and_prices = [('table', 50), ('chair', 20), ('sofa', 200), ('bed', 150), ('lamp', 10)]

# unzip the list of tuples into two tuples with the zip function and the unpacking operator *
products, prices = zip(*products_and_prices)

# tuple of products
print(products)
# ('table', 'chair', 'sofa', 'bed', 'lamp')

# tuple of prices
print(prices)
# (50, 20, 200, 150, 10)

```


### 3. map

The map(function, iterable, ...) function applies a given function to each element of an iterable. The returned value is a map object.
This object is basically an iterator that we can easily convert into a list or set, using again built-in functions.

The map function takes as first argument a function. When we think about a function in Python, we automatically think about the def keyword, but the map function does not only accept functions created by the user using def keyword, but also built-in, and anonymous functions (lambda expressions). The second argument is an iterable. An iterable is an object with a countable number of values that can be iterated for example using a for loop. Lists, sets, tuples, or dictionaries are iterables that can be used as the second argument of the map function.


**Examples**
The map function can be very useful when we want to apply a mathematical operation to all the elements of an iterable. In the following code block, three different mathematical operations are applied to the elements of a list.

```
# list of numbers
numbers = [1, 2, 3, 4, 5]

# add 1
list(map(lambda x: x + 1, numbers))
# [2, 3, 4, 5, 6]

# multiply by 2
list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]

# obtain the cube
list(map(lambda x: x ** 3, numbers))
# [1, 8, 27, 64, 125]

```

As shown above, we have employed anonymous functions, since they are pretty useful for short-term use. However, as I mentioned previously, we can also use regular functions.

```

# list of numbers
numbers = [1, 2, 3, 4, 5]

# add 1 funtion - regular function
def add_one(element):
    return element + 1 

# add 1 to each element of the list
list(map(add_one, numbers))
# [2, 3, 4, 5, 6]
```

If multiple iterable arguments are passed, the function is applied to the items from all iterables in parallel. 
The following code shows how we can multiply the elements of two iterables (lists) with the map function.

```
# lists of numbers
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

# multiply the elements of both lists
list(map(lambda x, y: x * y, numbers_1, numbers_2))
# [6, 14, 24, 36, 50]

```

### 4. filter

The filter(function, iterable) function takes a function and an iterable as inputs, returning the elements from the iterable for which the function returns True. As with the map function, the filter function does not only accept regular functions (def keyword), but also built-in, and anonymous functions.

**Example**

The code below uses the filter function to get the odd numbers from a list.

```
# list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# get odd numbers
list(filter(lambda x: x % 2, numbers))
# [1, 3, 5]
```

The filter function accepts as second argument any type of iterable such as lists, strings, tuples, or dictionaries, returning an iterator object. To visualize this object, we can convert it into a list with the built-in function list().
In the following code block, we use as input a tuple of strings, filtering those that start with M or V.

```

# list of cities
cities = ('Madrid', 'Valencia', 'Barcelona', 'Munich', 'Stuttgart')

# cities that start with M or V
tuple(filter(lambda x: x.startswith(('M', 'V')), cities))
# ('Madrid', 'Valencia', 'Munich')

```

### 5. input 
The input([prompt]) function gets raw input from the user, returning it as a string. This function takes an optional argument (prompt) that can be used to show a message to the user when asking for input.

**Examples**
The code below asks the user to input his/her name.

```
# ask the user to input a name
name = input('Enter your name: ')

# use the name in the following greeting
print('Hello {}'.format(name))
# Hello Amanda
```


If we want to use the input as a number, we have to convert it into an integer or floating-point number, since the function stores the input as a string.

```
# ask the user to input a number
number_1 = float(input('Enter a number: '))
# Enter a number: 2.5

# ask the user to input another number
number_2 = float(input('Enter another number: '))
# Enter another number: 3.4

# print the sum of both numbers
print('The sum is: {}'.format(number_1 + number_2))
# The sum is: 5.9

```

As shown above, the input of the user is transformed into a floating-point number with the built-in function float().

### 6. id
The id(object) function returns the identity of an object. This is an integer which is unique and constant for the object during its lifetime.

**Examples**

This function can come in handy when duplicating objects to check that we have created an independent copy of the object.
In Python, the = operator does not copy objects. It provides another name to refer to the same object, meaning any modification to the new object is reflected in the original one. The following code block shows that the assignment operator (=) does not create a new object, but a new reference to the original object, since both variables have the same id number.

```
# list of numbers
numbers = [1, 2, 3, 4, 5]

# new list of numbers
new_numbers = numbers

# both list have the same id number
print('numbers id: {}, new_numbers id: {}'.format(id(numbers), id(new_numbers)))
# numbers id: 1836112528136, new_numbers id: 1836112528136

# we can also check that they refer to the same object with the identity operator is
numbers is new_numbers
# True
```

We can also use the following identity operators to check whether two variables point to the same object:

* is → Evaluates to True if both sides have the same identity
* is not → Evaluates to True if both sides have different identities

As shown above, both variables (numbers and new_numbers) point to the same object, since the is operator evaluates to True.
To create a fully independent clone of the object, we can employ the copy.deepcopy(x) function (defined in the copy module). This function creates an independent copy, meaning we can change the new object without modifying the original one. In this case, both variables have different id numbers, and the identity operator is evaluates to False.

```
import copy

# list of numbers
numbers = [1, 2, 3, 4, 5]

# new list of numbers
new_numbers = copy.deepcopy(numbers)

# both list have different id numbers
print('numbers id: {}, new_numbers id: {}'.format(id(numbers), id(new_numbers)))
# numbers id: 1836112528648, new_numbers id: 1836112763528

# we can also check that both variables point to different objects with the identity operator is
numbers is new_numbers
# False
```

### 7. hex 

The hex(x) function converts an integer number to a lowercase hexadecimal string. This string starts with the prefix ‘0x’, indicating is a hexadecimal number. The function raises an exception (TypeError) if an object different than an integer is provided as input. The code below converts the integer 10 into a hexadecimal number.

```
hex_number = hex(10)

print(hex_number)

#0xa
print(type(hex_number))
# <class 'str'>

# An exception is raised if a float is provided as input
hex_number = hex(10.0)
# TypeErro


```


**Examples**

Hexadecimal numbers are often used by programmers to specify colors, as they provide a wider range that string values such as ‘green’ or ‘red’. Python represents hexadecimal colors using strings of the form ‘#RRGGBB’ where RR (red), GG (green), and BB (blue) are hexadecimal numbers between 00 and FF, representing the intensity of the color. Colors can also be represented using a tuple RGB (red, green, and blue) where each parameter defines the intensity of the color with an integer between 0 and 255. Now suppose you want a function that maps an RGB tuple representation to a hexadecimal string. The following block code shows how we can achieve this conversion with the help of the hex function.

```
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
```

### 8.bin

The bin(x) function converts an integer number to a binary string prefixed with ‘0b’.

**Example**

The bin function raises an exception (TypeError) if an object different from an integer is provided as input. To avoid this problem, we can use the try and except statements when trying to convert an integer into a binary number. The try clause contains the operation that can raise an exception (bin function), and the except clause includes the code that handles the exception. The function below converts an integer to a binary number, taking into account that an exception is raised if an object different from an integer is provided as input. In addition, the prefix ‘0b’ is eliminated, returning only the binary number.

```

def int2bin(integer):
    """Function that converts an integer to a binary string"""
    try:
        binary = bin(integer)
        return binary[2:] # string slicing to elimininate the prefix '0b'

    except TypeError:
        print('An integer should be provided as input')

int2bin(5)
# '101'

int2bin(6)
# '110'

int2bin(4.0)
# An integer should be provided as input
```

### 9. format

The format(value[, format_spec]) function returns a formatted representation of the given value controlled by the format specifier.

**Examples**
The format specifier determines how the value is formatted, presenting the following structure:
[[fill]align][sign][#][0][width][grouping_option][.precision][type]
You can learn more about all the options to format your values in the following [link](https://docs.python.org/3/library/string.html#formatspec)


Now, let’s see some examples:
* Fixed-point notation rounded off to two decimal places
* Percentage rounded off to one decimal place
* Hexadecimal number
* Exponential notation rounded off two decimal places with sign for both positive and negative numbers
* Number with fill character, width, and right-alignment

```
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
```
As you can observe, the format function provides a wide variety of ways of format your values. Combine the different parameters of the format specifier to discover more representations. 

### 10. open
The open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) function takes a string as input, specifying the path of the file, and returns a file object. If the file cannot be opened, an OSError is raised.

**Example**
We use the open function to read and write files in Python. To read a file, first we open it using the open function in reading mode (mode=’r’). This function returns a file object which we assign to the variable f. Then, we use the read method to access the content of the file and put it into a string. Finally, we close the file using the close method. It is important to remember to close all files when we no longer need them to avoid running out of file handles.

```

# open a file in reading mode 
f = open('reading_file.txt', 'r')
content = f.read()
print(content)
# Successful file reading!

# close the file to avoid running out of file handles
f.close()
```

We can also read all lines in the file as a list of strings using the .readlines() method as follows:

```
# open a file in reading mode
f = open('reading_lines.txt', 'r')
content = f.readlines()
print(content)
# ['First line\n', 'Second line\n', 'Third line\n']

# close the file to avoid running out of file handles
f.close()
```

To read the file line by line, we use the readline() method. This method read one entire line from the file, 
and returns it as a string.

```
# open a file in reading mode
f = open('reading_lines.txt', 'r')
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

```


## Basic Python cheat sheet 

 [PDF link ](../../resources/cheatsheet/beginners_python_cheat_sheet_pcc_all.pdf){target="_blank"}

 
<!-- Embed PDF File -->
<iframe src="../../resources/cheatsheet/beginners_python_cheat_sheet_pcc_all.pdf" style="width:1000px; height:800px;" frameborder="0" allowfullscreen></iframe>


## Python cheat sheet for Scikit learn

 [PDF link ](../../resources/cheatsheet/Python-Cheat-Sheet-for-Scikit-learn-Edureka.pdf){target="_blank"}

 
<!-- Embed PDF File -->
<iframe src="../../resources/cheatsheet/Python-Cheat-Sheet-for-Scikit-learn-Edureka.pdf" style="width:1000px; height:800px;" frameborder="0" allowfullscreen></iframe>