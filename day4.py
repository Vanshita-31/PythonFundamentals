# python strings
s = '''Strings in python are surrounded by either single quotation marks, 
or double quotation marks.'''
print(s)
# To check the type of the string

print(type(s))

# Index of string
# Indexing is started from 0

print(s[20])


# last char of string can be s[-1]
print(s[-2])
print(s[-1])

# slicing
# slicing is used to get the substring of the string
print(s[5:])

# Slice From the Start
h = "helicopter, airplane"
print(h[:5])

print(h[-5:-2])

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "helicopter":
    print(x)

# String Length
# To get the length of a string, use the len() function.

a = "hello world"
print(len(a))


# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

print("world" in a)

# Use it in an if statement:

if "world" in a:
    print("yes world is present")

# Upper Case
c = "catmaeo  !  "
print(c.upper())
print(c.lower())
print(c.strip())
print(c.rstrip("!"))
print(c.split(","))
print(c.replace("cat", "bili"))

# string concatenation

j = "joker"
k = "king"
print(j+k)
print(j + " "+k)

# String Format

b = "30"
l = "hello my name is krutika my age is" + " " + b
print(l)

# or

b = "30"
l = "hello my name is krutika my age is {}"
print(l .format(b))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# we can also use indexes
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {1} pieces of item {2} for {0} dollars."
print(myorder.format(quantity, itemno, price))

# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

text = "my name is \"vanshita\""
print(text)

txt1 = 'it\'s alright.'
print(txt1)

txt2 = "hello \n world"
print(txt2)

txt3 = " world \r hello"
print(txt3)

txt4 = " hello \t\t\t\t world"
print(txt4)

txt5 = " hello \bworld"
print(txt5)

# Code	Result
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

# list

marks = [90, 91, 92, 99, 100]
print(marks[len(marks)-3])  # 5-2 = 3 so it is giving 92


colors = ["red", "blue", "yellow"]
if "silver" in colors:
    print("yes")
else:
    print("no")

myName = ["vanshita", "sono", "rosa", "dona", "bruno"]
myNameWith_o = [item for item in myName if "o" in item]
print(myNameWith_o)

lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)

# methods of list

# append()
num = [1, 2, 3, 4]
print(num)
num.append(5)
print(num)

# reverse()
lst = [1, 2, 3]
print(lst)
lst.reverse()
print(lst)


# index()
numb = [1, 2, 3, 4, 5, 6, 7]
print(numb.index(2))  # gives the address of the index i.e 2 is located at 1 index

# count()
numb2 = [1, 2, 3, 3, 4, 5, 6, 2, 1, 2]
print(numb2.count(2))

# copy()
myList = ["vanshita", "sono", "rosa", "dona", "bruno"]
NewList = myList.copy()
print(NewList)

# insert()
number = [1, 2, 3, 4, 4, 5]
print(number)
number.insert(1, 1)
print(number)

# extend()
myList = ["vanshita", "sono", "rosa", "dona", "bruno"]
yourList = ["van", "can"]
myList.extend(yourList)
print(myList)

# Tuple

# tup = (1)
# print(tup)
# print(type(tup)) it will give output as <class 'int'>
# because it consider as int so whenever we create tuple we have to give comma for eg:
tuple = (1,)
print(type(tuple))
# it can alo be
tuple2 = (1, 2, 3, 4, 5)
print(tuple2)

# Sets

a = {10, 20, 30, 40, 5}
print(a)
print(type(a))

# print(a[1]) TypeError: 'set' object is not subscriptable

# set object does not suppoet indexing

d = {'a': "apple", 'b': "bat", 'c': "cat"}
print(d['b'])

# Conversion between data types
a = float(5)
print(a)

a = int(100.2)
print(a)

a = str(5)
print(a)
print(type(a))

# a = int('5d')
# print(a) it will give error

user = "vanshita"
lines = 100
print("congrats " + user + " you have written " + str(lines) + " lines of code.")
# if we remove str it will give error

# We can convert one sequence to another
a = ['1,2,3,4']
print(type(a))  # type list
s = set(a)
print(type(s))  # type set

s = list("hello")
print(s)
print(type(s))

a = 10
print("the value of a is " + str(a))

# Python input and output
# python output
# we use print function to output data to the standard output device
print("hello world")

ab = 20

# print("hello! the value of a is " + ab)
# if we not declare str here it will give error like print("hello! the value of a is " + ab)
# TypeError: can only concatenate str (not "int") to str
print("hello! the value of ab is ", str(ab))
print("the value of ab is " + str(ab))

# output Formatting
a = 10
b = 30  # multiple statements in single line
print("The value of a is {} and the value of b is {}".format(a, b))  # default
# specify the position of variable that is by giving it's index value
print("the value of a is {0} and the value of b is {1}".format(10, 20))
# Or
# We can use keyword arguments to format the string
print("hello {user} , {greetings}! have a nice day".format(
    user="Vanshita", greetings="Good morning"))

# We can combine positional arguments with keywords arguments
print("The story of {0}, {1} and {others}".format('Cat', 'Dog', others="LION"))

# Python Input
# In python we can simply use input() function to take the input from the user

num = input("Enter a number:")
print(num)

a = 10 << 4
print(a)
