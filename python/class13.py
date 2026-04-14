def Greet(): 
    print("Hello, World!")

Greet()

def add(a, b): 
    return a + b

result = add(5,3)
print("The sum of 5 and 3 is:", result)

def pallindrome(x):
     rev = 0 
     while x > 0: 
        rev = rev * 10 + x % 10
        x = x // 10
    return rev

num = int(input("Enter a number: "))
if num == pallindrome(num):
    print(num, "is a pallindrome.")
else: 
    print(num, "is not a pallindrome.") 