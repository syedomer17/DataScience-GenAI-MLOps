n = int(input("Enter the number of times you want to print : "))

for i in range(n): 
    print(f"{i+1}:Hello World")

n = int(input('Enter the number of numbers you want to print : '))

# n --> 100 --> 99 --> 100

for i in range(1, n+1,1): 
    print(i)

n = int(input('Enter the number of numbers you want to print : '))

for i in range(n, 0, -1): 
    print(i)

n = int(input('Enter the number of numbers you want to print : '))

s = 0 
# n --> 2 --> 1 --> n + 1 --> 2 
# n --> 2 --> n + 1 --> 3 --> 2 --> print 2 
for i in range(1, n + 1, 1):
    s = s + i

print(f"The sum of first {n} natural numbers is : {s}")

n = int(input("Enter a number for the factorial :- "))

fact = 1

for i in range(1, n+1, 1):
    fact = fact * i

print(f"The factorial of {n} is : {fact}")

n = int(input("Enter your range:"))

even_sum = 0
odd_sum = 0



for i in range(1, n+1, 1): 
    if i % 2 == 0: 
        even_sum += i 
    else: 
        odd_sum += i

n =  int(input("Enter the number to get factors:"))

for i in range(1, n+1, 1): 
    if n % i == 0: 
        print(i)

n = int(input("Enter the number of the factors you want to sum:"))

factor_sum = 0
for i in range(1, n+1, 1): 
    if n % i == 0: 
        factor_sum += i

print(f"The sum of the factors of {n} is : {factor_sum}")

a = int(input("Enter the value:"))
b = int(input("Enter your exponent:"))
power = a 
for i in range(b-1):
    power *= a

print(f"{a} raised to the power {b} is : {power}")

n = int(input("enter your number: (prime check):"))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

n = int(input("enter your number: (prime check):"))

for i in range(2, n ): 
    if n % i == 0: 
        print(f"{n} is not a prime number.")
        break
else:
    print(f"{n} is a prime number.")