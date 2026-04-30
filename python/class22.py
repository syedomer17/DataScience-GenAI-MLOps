# Exception Handling 
# try: 
#     # Code that might raise an exception
# except ExceptionType:
#     # Code to handle the exception
# else:
#     # Code to run if no exception occurred
# finally:
#     # Code to run regardless of whether an exception occurred

a =  int(input("Enter a number: ")) # it will take input from the user and convert it to an integer
b =  int(input("Enter another number: ")) # it will take input from the user and convert it to an integer

try: 
    print(a/b) # it will try to divide a by b and print the result
except Exception as err: 
    print("An error occurred: ", err) # it will print the error message if an exception occurred
else: 
    print("There was no error") # it will print this message if no exception occurred
finally: 
    print(a+b) # it will print the sum of a and b regardless of whether an exception occurred or not

try: 
    age = int(input("Enter your age: ")) # it will take input from the user and convert it to an integer
    if age < 18: 
        raise Exception("You are not old enough to vote") # it will raise an exception if the age is less than 18
    else: 
        print("You are old enough to vote") # it will print this message if the age is 18 or greater
except Exception as err: 
    print("An error occurred: ", err) # it will print the error message if an exception occurred