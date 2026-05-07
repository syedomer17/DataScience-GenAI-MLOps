# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))

# print(f"Addition: {a +b} \nSubtraction: {a - b} \nMultiplication: {a * b} \nDivision: {float(a / b)})")

# num = int(input("Enter a number:"))

# if num % 2 == 0: 
#     print(f"{num} is an even number")
# else: 
#     print(f"{num} is an odd number")

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# print(f"Before swapping: a = {a}, b = {b}")
# a = a + b 
# b = a - b
# a = a - b
# print(f"After swapping: a = {a}, b = {b}")

# num = int(input("Enter a number: "))

# print(f"remainder of this {num} by 7 is { num % 7 }")

# c = int(input("Enter the celsius temperature: "))

# f = c * 9 / 5 + 32 
# print(f"{c} degrees Celsius is equal to {f} degrees Fahrenheit")


# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# if a > 0 and b > 0: 
#     print(True)
# else: 
#     print(False)

# a = int(input("Enter a number: "))

# if a % 3 == 0 and a % 5 == 0: 
#     print(True)
# else: 
#     print(False)

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# c = a / b
# print(f"by dividing {a} by {b} we get {c}")

# d = a // b
# print(f"by floor dividing {a} by {b} we get {d}")

# print(2 ** 10)

# # Read a 3-digit number (like `345`) and print the sum of its three digits (`3 + 4 + 5 = 12`)

# # num = int(input("Enter a 3-digit number: "))
# # hundreds = num // 100 
# # tens = (num % 100) // 10 
# # ones = num % 10 

# # print(f"The sum of the digits is {num} is {hundreds + tens + ones}")

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# print((a > b) * a + (a <= b) * b)

# year  = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 != 0): 
#     print(True)
# else:     
#     print(False)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

#read a positive number. Print `True` if it is a power of 2 (1, 2, 4, 8, 16, ...).

a = int(input("Enter a positive number: "))

if a & (a - 1) == 0: 
    print(True)
else: 
    print(False)

