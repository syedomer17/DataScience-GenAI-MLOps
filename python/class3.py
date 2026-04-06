a = "NATURE Beautiful"
print(a)

# string indexing
print(a[0])
print(a[5])
print(a[-1])
print(a[6])

b = "Sheryians Coding"
print(b[0:9:1]) # [start:stop:step]
print(b[::]) # it will print the whole string
print(b[:9:2]) # it will print every second character of the string

c = "hello I am Data Scientist"
print(c[0:5])
print(c[11:15])
print(c[16:])

# The strings are immutable in nature, which means we cannot change the value of a string once it is created.

d = "hzllo"
# d[1] = "e" # This will give an error because strings are immutable

print("Hello World") # This is a string literal

# formatting string 
name = "Omer"
age = 19 

print("Hello, my name is", name, "and I am", age, "years old.") # This is a formatted string using concatenation

print(f"Hello, my name is {name} and I am {age} years old.") # This is a formatted string using f-string

print(f"Hello my name is {name}\nand my age is {age}")
# The \n is used to create a new line in the string.
# The \t is used to create a tab space in the string.
# The \\ is used to create a backslash in the string.
# The \b is used to create a backspace in the string.

# raw string 
print(r"hello my name is Omer\b and my age is 19")

# Type conversion

x = 23 
print(type(x))
x = str(x) # converting integer to string
print(type(x))

# your can't convert a string to an integer or float if the string contains non-numeric characters
y = "23"
print(type(y))
y = int(y) # converting string to integer
print(type(y))

z = "23.5"
print(type(z))
z = float(z) # converting string to float
print(type(z))

# There are 7 falsy values in Python: False, None, 0, 0.0, 0j, '', and []. All other values are considered truthy.

w = "hello"
print(type(w))
w = bool(w) # converting string to boolean
print(type(w))

# Input statement ways 

name = input("Hello, what is your name? ")
print(f'Hi, my name is {name}')

age = int(input("What is your age? "))
print(f'I am {age} years old.')