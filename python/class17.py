# tuple has heterogeneous data and is immutable
a = (1,2,3,4,5,"hello", 1.2, True)
print(a) # (1, 2, 3, 4, 5, 'hello', 1.2, True)

# tuple unpacking

a,b,c = (10,20,30)
print(a) # 10
print(b) # 20
print(c) # 30

a = (1)
print(type(a)) # <class 'int'> it will not be a tuple because we have not used comma after 1

a = (10,20,30,40,50)
print(a[0]) # 10
print(a[1]) # 20
print(a[2]) # 30
print(a[3]) # 40

print(a[:3]) # (10, 20, 30)
print(a[2:]) # (30, 40, 50)
print(a[1:4]) # (20, 30, 40)
print(a[::2]) # (10, 30, 50)
print(a[::-1]) # (50, 40, 30, 20, 10)

a = [10,20,30,40,50]

new_tuple = tuple(a) # we are converting the list to tuple
print(new_tuple) # (10, 20, 30, 40, 50)

t = (10,20,30,40,50)

for i in t:
    print(i) # 10 20 30 40 50

for i in range(len(t)): 
    print(t[i]) # 10 20 30 40 50

# there are only two methods in tuple count and index

a = (10,20,30,40,40,40,50)

print(a.count(40)) # 3
print(a.index(40)) # 3