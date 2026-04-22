# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. and if it is empty it type is not set it is a empty dectionary 
s = {10,20,30,40,50}
print(hash("hello"))
print(hash(10)) 

print(type(s)) # <class 'set'>

a = [12,12,12,34,34,6,7,7,8,8,9,9,9]
s = set(a)
print(s) # {34, 6, 7, 8, 9, 12} it will remove the duplicate values and it will not maintain the order of the elements

s = {10,20,30,40,50}

for i in s:
    print(i) # 10 20 30 40 50 it will not maintain the order of the elements

s.add(70) # it will add the element to the set
print(s)
s.clear() # it will remove all the elements from the set
print(s) # set() it will print an empty set
s.copy() # it will return a copy of the set
print(s) # set() it will print an empty set

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.difference(s2)) # {10, 20, 30} it will return the elements which are present in s1 but not in s2
print(s2.difference(s1)) # {60, 70, 80} it will return the elements which are present in s2 but not in s1

s1.discard(10) # it will remove the element from the set if it is present otherwise it will do nothing
print(s1) # {20, 30, 40, 50}

print(s1 & s2) # {40, 50} it will return the common elements between s1 and s2
print(s1 | s2) # {20, 30, 40, 50, 60, 70, 80} it will return all the elements from both sets without duplicates
print(s1 ^ s2) # {20, 30, 60, 70, 80} it will return the elements which are present in s1 or s2 but not in both

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.issubset(s2)) # False it will return True if s1 is a subset of s2
print(s2.issuperset(s1)) # False it will return True if s2 is a superset of s1
s1.pop() # it will remove and return an arbitrary set element. Raises KeyError if the set is empty.
print(s1) # it will print the set after removing an arbitrary element