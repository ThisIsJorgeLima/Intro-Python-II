print('Python String split() Method:')
print('Syntax:')
print('string.split(separator, maxsplit)')
"""
Parameters:
Separator = Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator.

Or

Maxsplit = Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
"""


print('Example 1:')
print('Split a string into a list where each word is a list item:')

txt = "welcome to the jungle"

x = txt.split()

print(x)
print('+---------------------------------+')
print('More Examples:')
print('Example 2.')
print('Split the string, using comma, followed by a space, as a separator:')
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)
print('+---------------------------------+')
print('Example 3.')
print('Use a hash character as a separator:')
txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)
print('+---------------------------------+')
print('Example 4.')
print('Split the string into a list with max 2 items:')
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)
print('+---------------------------------+')
print('Python super() Function')
print('Example 1')
print('Create a class that will inherit all the methods and properties from another class:')


class Parent:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)


class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)


x = Child("Hello, and welcome!")

x.printmessage()

print('+---------------------------------+')

"""
Definition and Usage

The super() function is used to give acces to methods and properties of a parent or sibling class.

The super() function returns an object that represents the parent class.

Syntax
super()

Parameter Values
None
"""
print('Python Functions')
"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""
print('Creating a function')
print('In Python a function is defined using the def keyword:')
print('Example 1:')


def my_function():
    print("Hello from a function")


print('+---------------------------------+')
print('Calling a Function')
print('To call a function, use the function name followed by parenthesis:')
print('Example 2:')


def my_function():
    print("Hello from a function")


print('+---------------------------------+')

"""
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
"""


my_function()
print('Example 3:')


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")

print('+---------------------------------+')

"""
Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""
print('Number of Arguments')
print('By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.')
print('Example 4')
print('This function expects 2 arguments, and gets 2 arguments:')


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")
print('+---------------------------------+')

# '''
# If you try to call the function with 1 or 3
# arguments you will get an error:
# ''''

print('Example 5')
print('This function expects 2 arguments, but gets only 1:')

# This code will get an error:
# def my_function(fname, lname):
#     print(fname + " " + lname)
#
#
# my_function("Emil")
print('Arbitrary Arguments, *args')
'''
      If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

      This way the function will receive a tuple of arguments, and can access the items accordingly:
'''
print('Example 6')
print('If the number of arguments is unknown, add a * before the parameter name:')


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

print('+---------------------------------+')
print('Example 1')
print('Filter the array, and return a new array with only the values equal to or above 18:')
ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, ages)

for x in adults:
    print(x)

"""
Definition and Usage
The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
"""
"""
Syntax:
filter(function, iterable)

Parameter Values:
function = A Function to be run for each item in the iterable
iterable = The iterable to be filtered
"""
print('+---------------------------------+')
print('Python slice() Function')
print('Example 1')
print('Create a tuple and a slice object. Use the slice object to get only the two first items of the tuple:')

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

"""
Definition and Usage
The slice() function returns a slice object.

A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.

Syntax:
slice(start, end, step)

Parameter Values:
start = Optional. An integer number specifying at which position to start the slicing. Default is 0
end = An integer number specifying at which position to end the slicing
step =Optional. An integer number specifying the step of the slicing. Default is 1
"""
print('More Examples')
print('Example 2')
print('Create a tuple and a slice object. Start the slice object at position 3, and slice to position 5, and return the result:')

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])
print('+---------------------------------+')
print('Example 3')
print('Create a tuple and a slice object. Use the step parameter to return every third item:')
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])
print('+---------------------------------+')
print('Python Dictionaries')
print('Dictionary')
print('A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.')
print('Example 1')
print('Create and print a dictionary:')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print('+---------------------------------+')
print('Accessing Items')
print('You can access the items of a dictionary by referring to its key name, inside square brackets:')
print('Example 1')
print('Get the value of the "model" key:')
x = thisdict["model"]

# There is also a method called get() that will give you the same result:
print('+---------------------------------+')
print('Example 2')
print('Get the value of the "model" key:')
x = thisdict.get("model")
print('+---------------------------------+')
print('Change Values')
print('You can change the value of a specific item by referring to its key name:')
print('Example 3')
print('Change the "year" to 2018:')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
"""
Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
"""
print('+---------------------------------+')
print('Example 4')
print('Print all key names in the dictionary, one by one:')
for x in thisdict:
    print(x)
print('+---------------------------------+')
print('Example 5')
print('Print all values in the dictionary, one by one:')
for x in thisdict:
    print(thisdict[x])
print('+---------------------------------+')
print('Example 6')
print('You can also use the values() method to return values of a dictionary:')
for x in thisdict.values():
    print(x)
print('+---------------------------------+')
print('Example 7')
print('Loop through both keys and values, by using the items() method:')
for x, y in thisdict.items():
    print(x, y)
"""
Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:
"""
print('+---------------------------------+')
print('Example 8')
print('Check if "model" is present in the dictionary:')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

"""
Dictionary Length
To determine how many items(key-value pairs) a dictionary has, use the len() function.
"""
print('+---------------------------------+')
print('Example 9')
print('Print the number of items in the dictionary:')
print(len(thisdict))

"""
Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
"""
print('+---------------------------------+')
print('Example 10')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
print('+---------------------------------+')
print('Removing Items')
print('There are several methods to remove items from a dictionary:')
print('Example 11')
print('The pop() method removes the item with the specified key name:')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

print('+---------------------------------+')
print('Example 12')

"""
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

print('+---------------------------------+')
print('Example 13')
print('The del keyword removes the item with the specified key name:')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)
print('+---------------------------------+')
print('Example 14')
# print('The del keyword can also delete the dictionary completely:')
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# del this dict
# print(thisdict)  # this will cause an error because "thisdict" no longer exists.

print('+---------------------------------+')
print('Example 15')
print('The clear () method empties the dictionary:')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)
"""
Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
print('+---------------------------------+')
print('Example 16')
print('Make a copy of a dictionary with copy() method:')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)
print('+---------------------------------+')
print('Another way to make a copy is to use the built-in function dict().')
print('Example 17')
print('Make a copy of a dictionary with the dict() function:')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)
print('+---------------------------------+')
print('Nested Dictionaries:')
print('A dictionary can also contain many dictionaries, this is called nested dictionaries.')
print('Example 18')
print('Create a dictionary that contain three dictionaries:')
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
# print(myfamily)
print('+---------------------------------+')
print('Or, if you want to nest three dictionaries that already exists as dictionaries:')
print('Example 19')
print('Create a dictionary that contain three dictionaries:')
print('Create three dictionaries, then create one dictionary that will contain the other three dictionaries:')
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
# print(myfamily)
print('+---------------------------------+')
print('The dict() Constructor')
print('It is also possible to use the dict() constructor to make a new dictionary:')
print('Example 20')
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
