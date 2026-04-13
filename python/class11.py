a = int(input("Enter a number: ")) 

while a > 0: 
    print(a % 10)
    a //= 10

a = int(input("Enter a number: "))

sum = 0 

while a > 0: 
    sum += a % 10
    a //= 10

print("The sum of the digits is: ", sum)


a = int(input("Enter a number: "))
rev = 0 

while a > 0: 
    rev *= 10 + a % 10 
    a //= 10 
print("The reverse of the number is: ", rev)

a = int(input("Enter a number: "))

square = a ** 2 
dup = a
count =  0 

while a > 0: 
    count += 1 
    a //= 10

print("The number of digits is: ", count)
extract = square % (10 ** count)

if extract == dup:
    print("The number is an automorphic number.")
else:
    print("The number is not an automorphic number.")