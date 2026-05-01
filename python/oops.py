# difference between functional programming and object oriented programming and imperative programming

# functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. 

# object oriented programming is a programming paradigm that uses objects and classes to organize code and data.

# imperative programming is a programming paradigm that uses statements that change a program's state. It focuses on describing how a program operates, rather than what it does.
# example 

# functional programming
def add(x, y):
    return x + y
# object oriented programming
class Calculator:
    def add(self, x, y):
        return x + y
# imperative programming
x = 5
y = 10
result = x + y
print(result)

# to make an class in python we use the class keyword followed by the name of the class and a colon
class Factory: # the first letter of the class name is capitalized by convention
    a = 12 # this is an attribute of the class Factory
    def hello(): # this is a method of the class Factory
        print("hello world") # this is a method of the class Factory
    print("I am getting initialized") # this is a statement that will be executed when the class is defined
print(Factory) # this will print the class Factory

print(Factory.a) # this will print the value of the attribute a of the class Factory
Factory.hello() # this will call the method hello of the class Factory

# what is an object in python
# an object is an instance of a class. It is a collection of data and methods that operate on that data. An object is created from a class and can have its own unique state and behavior.

# to create an object of a class we use the class name followed by parentheses

class Fac: 
    a = "Hello I am an attribute of the class Fac"
    def hello(): 
        print("Hello I am a method of the class Fac")

obj = Fac() # this creates an object of the class Fac
print(obj.a) # this will print the value of the attribute a of the object obj
obj.hello() # this will call the method hello of the object obj

class Fact: 
    def __init__(self): # this is the constructor method of the class Fact. It is called when an object of the class Fact is created
        print("I wil run no matter what when an object of the class Fact is created")

Fact() # this will create an object of the class Fact and will run the __init__ method

class BackFactory: 
    def __init__(self, material, zips, pockets): # this is the constructor method of the class BackFactory 
        print("I am a constructor method and I will run when an object of the class BackFactory is created")

        self.material = material # this is an instance variable that will be unique to each object of the class BackFactory
        self.zips = zips # this is an instance variable that will be unique to each object of the class BackFactory
        self.pockets = pockets # this is an instance variable that will be unique to each object of the class BackFactory

        def show_details(self): # this is a method of the class BackFactory
            print(self.material) # this will print the value of the instance variable material of the object
            print(self.zips) # this will print the value of the instance variable zips of the object
            print(self.pockets) # this will print the value of the instance variable pockets of the object


object1 = BackFactory("leather",3,3) # this will create an object of the class BackFactory and will run the __init__ method
print(object1.material) # this will print the value of the instance variable material of the object object1
print(object1.zips) # this will print the value of the instance variable zips of the object object1
print(object1.pockets) # this will print the value of the instance variable pockets of the object object1
        
print(object1.show_details()) # this will call the method show_details of the object object1 and will print the details of the object object1

