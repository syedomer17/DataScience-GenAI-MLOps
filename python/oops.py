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

class Animal: 
    name = "lion" # this is a class attribute
    gender = "male" # this is a class attribute

    def __init__(self,name,age):
        self.name = name # this are the instance attributes of the class Animal
        self.age = age # this are the instance attributes of the class Animal
        

    def info(self): # this is a method of the class Animal
        print("This is an method of the class Animal")

    @classmethod # this is a class method of the class Animal. It can be called using the class name or the object name
    def clmMethod(cls): 
        print(f"{cls.gender} {cls.name}") # this will print the value of the class attributes
    
    @staticmethod # this is a static method of the class Animal. It can be called using the class name or the object name
    def hello(): 
        print("hello i am static method of the class Animal") # this is a static method of the class Animal. It can be called using the class name or the object name

obj = Animal("Lion",12) # this is an instance of the class Animal

print(obj.name) # this will print the value of the instance attribute name of the object obj
print(obj.age) # this will print the value of the instance attribute age of the object obj
print(obj.info()) # this will call the method info of the object obj
print(Animal.clmMethod()) # this will call the class method clmMethod of the class Animal
print(obj.clmMethod()) # this will call the class method clmMethod of the object obj
print(Animal.hello()) # this will call the static method hello of the class Animal
print(obj.hello()) # this will call the static method hello of the object obj

class Regestration: 
    def __init__(self,name,age,number,blood):
        self.name = name
        self.age = age
        self.number = number
        self.blood = blood

    def show(self): 
        print(f"Name: {self.name}\nAge: {self.age}\nNumber: {self.number}\nBlood Group: {self.blood}")
student1 = Regestration("John",20,1234567890,"A+")
student1.show()
student2 = Regestration("Jane",22,9876543210,"B+")
student2.show()
student3 = Regestration("Doe",19,5555555555,"O+")
student3.show()

# inheritance in python 
# inheritance is a feature of object oriented programming that allows a new class to inherit the properties and methods of an existing class. The new class is called the child class or subclass and the existing class is called the parent class or superclass.

class Animal: 
    def __init(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Human(Animal): # this is a child class that inherits from the parent class Animal
    def __init(self, name, age, number, blood):
         super().__init(name, age) 
         self.number = number
         self.blood = blood
        
    def info(self): # this is a method of the class Human that overrides the method info of the class Animal
        print(f"Name: {self.name}\nAge: {self.age}\nNumber: {self.number}\nBlood Group: {self.blood}")

class Robot(Human): # this is a child class that inherits from the parent class Human
    def __init__(self, name, age, number, blood, model):
        super().__init__(name, age, number, blood)
        self.model = model

    def info(self): # this is a method of the class Robot that overrides the method info of the class Human
        print(f"Name: {self.name}\nAge: {self.age}\nNumber: {self.number}\nBlood Group: {self.blood}\nModel: {self.model}")

obj = Animal("Lion",12)
obj2 = Human("John",20,1234567890,"A+")
obj3 = Robot("R2D2",10,0000000000,"C+","R2D2")

print(obj.name) # this will print the value of the instance attribute name of the object obj
print(obj.age) # this will print the value of the instance attribute age of the object obj
print(obj.info()) # this will call the method info of the object obj
print(obj2.name) # this will print the value of the instance attribute name of the object obj2
print(obj2.age) # this will print the value of the instance attribute age of the object obj2
print(obj2.info()) # this will call the method info of the object obj2
print(obj3.name) # this will print the value of the instance attribute name of the object obj3
print(obj3.age) # this will print the value of the instance attribute age of the object obj3
print(obj3.info()) # this will call the method info of the object obj3

# types of inheritance in python
# 1. single inheritance: when a child class inherits from a single parent class
# 2. multiple inheritance: when a child class inherits from multiple parent classes
# 3. multilevel inheritance: when a child class inherits from a parent class and the parent class inherits from another parent class
# 4. hierarchical inheritance: when multiple child classes inherit from a single parent class
# 5. hybrid inheritance: when a child class inherits from multiple parent classes and the parent classes have a common ancestor class

class Animal: 
    name = "Lion"

class Human: 
    name = "John"

class Robots(Human, Animal): # this is a child class that inherits from multiple parent classes
    def info(self):
        print(f"Name: {self.name}") # this will print the value of the instance attribute name of the object obj3

class Animal: 
    pass 

class Human(Animal):
    pass

class Robots(Animal):
    pass

# Encapsulation in python
# Encapsulation is a feature of object oriented programming that allows you to restrict access to certain components of an object and protect the data from unauthorized access. It is achieved by using access modifiers such as private, protected and public.

# there asre three types of access modifiers in python
# 1. public: when an attribute or method is declared as public, it can be accessed from anywhere in the program. It is the default access modifier in python.
# 2. protected: when an attribute or method is declared as protected, it can be accessed from within the class and its subclasses. It is denoted by a single underscore (_) before the attribute or method name.
# 3. private: when an attribute or method is declared as private, it can only be accessed from within the class. It is denoted by a double underscore (__) before the attribute or method name.

class Animal: 
    __name = "lion" # this is a private attribute of the class Animal

    def _speak(self): # this is a protected method of the class Animal
        print("I am a lion and I can speak")

class Human(Animal): 
    def info(self):
        print(f"Name: {super().__name}") # this will raise an error because name is a private attribute of the class Animal and cannot be accessed from the subclass Human
        self._speak() # this will call the protected method speak of the class Animal

obj = Animal()
print(obj.__name) # this will raise an error because name is a private attribute of the class Animal and cannot be accessed from outside the class
obj._speak() # this will call the protected method speak of the object obj
obj2 = Human()
obj2.info() # this will call the info method of the object obj2 and will print the name and will call the protected method speak of the class Animal

# polymorphism in python
# Polymorphism is a feature of object oriented programming that allows you to use a single interface to represent different types of objects. It is achieved by using method overriding and method overloading.

class Animal: 
    name = "lion"
    def speak(self): 
        print("I am an animal and I can speak")

class Bird:
    name = "parrot"
    def speak(self): 
        print("I am a bird and I can speak")

# Example of polymorphism
animals = [Animal(), Bird()]
for animal in animals:
    animal.speak()

# there are two types of polymorphism in python
# 1. compile time polymorphism: when a method is overloaded, it is called compile time polymorphism. It is achieved by defining multiple methods with the same name but different parameters in the same class.
# 2. runtime polymorphism: when a method is overridden, it is called runtime polymorphism. It is achieved by defining a method in the child class with the same name and same parameters as the method in the parent class. The method in the child class will override the method in the parent class and will be called at runtime when the method is called using an object of the child class.

class Animal:
    name = "lion"
    def speak(self):
        print("I am an animal and I can speak")

class Human(Animal):
    name = "John"
    def speak(self):
        print("I am a human and I can speak")
    
# Abstraction in python
# Abstraction is a feature of object oriented programming that allows you to hide the implementation details of a class and only expose the necessary features to the user. It is achieved by using abstract classes and abstract methods.

from abc import ABC, abstractmethod

class Animal(ABC): 
    @abstractmethod
    def sound(self):
        pass 

class Dog(Animal): 
    def sound(self): # we alwasy neeed to make this method in the child class otherwise we will get an error because the method sound is an abstract method and it must be implemented in the child class
        print("Woof")