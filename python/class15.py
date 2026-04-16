a = []
print(type(a))

# list have an behavior of heterogeneous data types your can store any type of data in list 

# list can have duplicate values
b = [1, 1, 1, 2, 2 ,3 ,4]

# list are mutable data types you can change the value of list after creating it
c = [1, 2, 3, 4]
c[0] = 10
print(c) # [10, 2, 3, 4]

# list are ordered data types you can access the elements of list by their index
d = ["omer", "ali", "veli"]
print(d[0]) # omer
print(d[1]) # ali
print(d[-1]) # veli

# slicing in list
e = [10,20,30,40,50]
print(e[0:3])

# deep copy and shallow copy in list
f = [1,2,3,4]
g = f # deeep copy we are creating a new variable g that points to the same list as f means g and f are pointing to the same list in memory
g[0] = 10 # we are changing the value of g but it will affect f because g and f are pointing to the same list in memory
print(f) # [10, 2, 3, 4]
print(g) # [10, 2, 3, 4]

h = f.copy() # shallow copy we are creating a new variable h that points to a new list in memory that has the same values as f
h[0] = 20 # we are changing the value of h but it will not affect f because h is a shallow copy of f
print(f) # [10, 2, 3, 4]
print(g) # [10, 2, 3, 4]
print(h) # [20, 2, 3, 4]

# deep copy in list
import copy
i = copy.deepcopy(f) # deep copy we are creating a new variable i that points to a new list in memory that has the same values as f
i[0] = 30 # we are changing the value of i but it will not affect f because i is a deep copy of f
print(f) # [10, 2, 3, 4]
print(g) # [10, 2, 3, 4]
print(h) # [20, 2, 3, 4]
print(i) # [30, 2, 3, 4]

# list traversal
# method 1
j = [1, 2, 3, 4, 5]
for i in j: 
    print(i)

# method 2
for i in range(len(j)):
    print(j[i])

# to now more about list you can use a in built funcation help(list) to know more about list and its methods
help(list)

a = [1, 2, 3, 4, 5, 5]
a.append(6) # append method is used to add an element at the end of the list
print(a) # [1, 2, 3, 4, 5, 6]

# to clear the list you can use clear method
a.clear() # clear method is used to remove all the elements from the list
print(a) # []

# to count the number of occurrences of an element in the list you can use count method
a.count(5) # count method is used to count the number of occurrences of an element in the list
print(a.count(5)) # 0

# to find the index of an element in the list you can use index method
a.index(3) # index method is used to find the index of an element in the list
print(a.index(3)) # 2

a.insert(2, 12) # insert method is used to insert an element at a specific index in the list

# to remove an element from the list you can use pop  method
a.pop() # pop method is used to remove the last element from the list by default it remove last element but you can also specify the index of the element you want to remove
print(a) # [1, 2, 12, 3, 4, 5]

# to sort the list you can use sort method
a.sort() # sort method is used to sort the list in ascending order by default but you can also specify the order of sorting by using the reverse parameter
print(a) # [1, 2, 3, 4, 5, 12]