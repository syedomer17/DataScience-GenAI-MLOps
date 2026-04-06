# comparison operators 
# There are 6 types of comparison operators in Python: ==, !=, >, <, >=, and <=.

# comparison operators are used to compare two values and return a boolean value (True or False) based on the comparison.

a = 12 
b = 45 
print(a > b)
print(a == b)
print(a != b)
print(a < b)
print(a >= b)
print(a <= b) 
print((12 == 12) == True) # this will return True because 12 is equal to 12

# logical operators
# There are 3 types of logical operators in Python: and, or, and not.

# And operator returns True if both operands are True, otherwise it returns False.
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# Or operator returns True if at least one of the operands is True, otherwise it returns False.
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# Not operator returns True if the operand is False, and returns False if the operand is True.
print(not True) # False
print(not False) # True