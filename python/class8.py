#There are only 2 loops in Python: for and while loops.

for i in range(11): # range(start, stop, step) the default value of start is 0 and the default value of step is 1
    print(i)

for i in range(10, 41, 1):
    print(i)

for i in range(-10, 21, 1):
    print(i)

for i in range(35,4, -1):
    print(i)

table = int(input("Enter the number for which you want to print the multiplication table: "))
for i in range(1, 11, 1): 
    print(f'{table} X {i} = {table * i}')

a = "Hello How are you doing?"

for i in a:
    print(i)

for i in range(0, len(a), 1):
    print(a[i])