# Arithmetic operators 
# There are 7 types of arithmetic operators in Python: +, -, *, /, //, %, and **.

# python follows BODMAS rule which means that the order of operations is: Brackets, Orders (i.e. powers and square roots, etc.), Division and Multiplication, Addition and Subtraction.

a = 12
b = 24 
print(a + b) # addition
print(b - a) # subtraction
print(a * b) # multiplication
print(b / a) # division  the value will be a float because it is in fraction form
print(b // a) # floor division the value will be an integer because it is in whole
print(b ** a) # exponentiation 
print(b % a) # modulus the value will be the remainder of the division

# Assignment operators
# There are 7 types of assignment operators in Python: =, +=, -=, *=, /=, //=, and **=.
x = 10 
x += 5 # x = x + 5
print(x)
x -= 3 # x = x - 3
print(x)
x *= 2 # x = x * 2
print(x)
x /= 4 # x = x / 4
print(x)
x //= 2 # x = x // 2
print(x)
x **= 3 # x = x ** 3
print(x)

# strings also support the + operator for concatenation and the * operator for repetition.
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2) # concatenation
print(s1 * 3) # repetition