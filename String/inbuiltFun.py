#usning inbuilt function
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

#removing white space
#The strip() method removes any whitespace from the beginning or the end:
a = "            Hello, World! ,SAm,GAdge                                          "
print(a.strip()) # returns "Hello, World!"

#replace string
a = "Hello, World!"
print(a.replace("H", "J"))

#split string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#The casefold() method returns a string where all the characters are lower case.

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#The count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt = "My name is Ståle"
x = txt.encode()
print(x)

#The format() method formats the specified value(s) and insert them inside the string's placeholder.
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

#The index() method finds the first occurrence of the specified value
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#he isdigit() method returns True if all the characters are digits, otherwise False.
txt = "50800"
x = txt.isdigit()
print(x)

#concatination
a = "Hello"
b = "World"
c = a + b
print(c)

#string format
age = 36
txt = "My name is John, I am " ,age
print(txt)

#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)





