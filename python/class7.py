a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b: 
    print(f"{a} is greater than {b}") 
elif b > a: 
    print(f"{b} is greater than {a}")
else: 
    print(f"{a} and {b} are equal")

gen = input("Enter your gender (M/F): ")

if gen == 'm' or gen == 'M': 
    print("You are a male")
elif gen == 'f' or gen == 'F':
    print("You are a female")
else: 
    print("Invalid input")

num = int(input("Enter a number: "))

if num % 2 == 0: 
    print(f"{num} is an even number")
else: 
    print(f"{num} is an odd number")

age = int(input("Enter your age: "))

if age >= 18:  
    print("You are an adult.")
else: 
    print("You are a minor.")

day = int(input("Enter the day of the week (1-7): "))

if day == 1: 
    print("Monday")
elif day == 2: 
    print("Tuesday")
elif day == 3: 
    print("Wednesday")
elif day == 4: 
    print("Thursday")
elif day == 5: 
    print("Friday")
elif day == 6: 
    print("Saturday")
elif day == 7: 
    print("Sunday")
else: 
    print("Invalid input")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if n1 == n2 and n1 == n3: 
    print("All numbers are equal")
elif n1 == n2 or n1 == n3 or n2 == n3: 
    print("Two numbers are equal")  
elif n1 > n2 and n1 > n3: 
    print(f"{n1} is the greatest")
elif n2 > n1 and n2 > n3: 
    print(f"{n2} is the greatest")
else: 
    print(f"{n3} is the greatest")


year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 != 0 and year % 4 == 0:
    print(f"{year} is a leap year")
else: 
    print(f"{year} is not a leap year") 

bill = int(input("Enter the bill amount: "))

if bill >= 1000 and bill <= 4999: 
    print(f"You get a 10% discount the final bill amount is :{(bill * 90) / 100}")

elif bill >=  5000: 
    print(f"You get a 20% discount the final bill amount is :{(bill * 80) / 100}")

else: 
    print(f"You get a 5% discount the final bill amount is :{(bill * 95) / 100}")

char = input("Enter a character: ")

if char in "aeiouAEIOU": 
    print(f"{char} is a vowel")
else: 
    print(f"{char} is a consonant")