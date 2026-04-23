# dictionary is a collection which is unordered, changeable and indexed. No duplicate members. it is represented by curly braces {} and it is a key-value pair.

d = {
    1: 10,
    2: 20,
    3: 30,
}

print(d[1])

d[1] = 100 # it will update the value of the key 1 to 100
print(d[1]) # 100
d[4] = 40 # it will add a new key-value pair to the dictionary
print(d) # {1: 100, 2: 20, 3: 30, 4: 40}

c = {
    "name": ["omer","aayan","rayyan"]
}
print(c["name"]) # ['omer', 'aayan', 'rayyan']

d = dict(name="omer", age=20, city="Hyderabad") # it will create a dictionary with the given key-value pairs
print(d) # {'name': 'omer', 'age': 20, 'city': 'Hyderabad'}

d = dict([("name", "omer"), ("age", 20), ("city", "Hyderabad")]) # it will create a dictionary with the given key-value pairs
print(d) # {'name': 'omer', 'age': 20, 'city': 'Hyderabad'}

a = {
    "name": "omer",
    "age": 20,
    "city": "Hyderabad",
}

for i in a:
    print(i) # it will print the keys of the dictionary
    print(a[i]) # it will print the values of the dictionary
    print(f"{i}: {a[i]}") # it will print the key-value pairs of the dictionary in the format "key: value"

for i in a.keys():
    print(i) # it will print the keys of the dictionary

for i in a.values():
    print(i) # it will print the values of the dictionary

for i in a.items():
    print(i) # it will print the key-value pairs of the dictionary as tuples
    print(f"{i[0]}: {i[1]}") # it will print the key-value pairs of the dictionary in the format "key: value"

help(dict) # it will print the documentation of the dictionary class

a = {
    "name": "omer",
    "age": 20,
    "city": "Hyderabad",
}
print(a.get("name")) # it will return the value of the key "name"
print(a.items()) # it will return a view object that displays a list of a dictionary's key-value tuple pairs
print(a.keys()) # it will return a view object that displays a list of all the keys in the dictionary
print(a.values()) # it will return a view object that displays a list of all the values in the dictionary
print(a.pop("name")) # it will remove the key "name" and return its value
print(a) # {'age': 20, 'city': 'Hyderabad'}
print(a.popitem()) # it will remove the last key-value pair and return it as a tuple
print(a) # {'age': 20}
print(a.setdefault("name", "omer")) # it will return the value of the key "name" if it is in the dictionary, otherwise it will insert the key "name" with the value "omer" and return "omer"
print(a) # {'age': 20, 'name': 'omer'}
print(a.update({"age": 30, "city": "Karachi"})) # it will update the value of the key "age" to 30 and add a new key-value pair "city": "Karachi" to the dictionary
print(a) # {'age': 30, 'name': 'omer', 'city': 'Karachi'}