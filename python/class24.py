from pathlib import Path 
import shutil

def create_folder(): 
    try:
        folder_name = input("Enter the name of the folder you want to create: ")
        p = Path(folder_name)
        Path.mkdir(p)
        print("Folder created successfully")
    except Exception as err:
        print("An error occurred: ", err)

def read_file_folder(): 
    try: 
        p = Path(".") # current directory
        items = list(p.rglob("*")) # get all files and folders in the current directory
        for index, value in enumerate(items): 
            print(f"{index + 1}. {value}") # print the index and the name of the file or folder
    except Exception as err:
        print("An error occurred: ", err)
    
def update_folder():
    try: 
        read_file_folder() # read the files and folders to get the index of the file or folder to update
        old_name = input("Enter the name of the folder you want to update: ")
        p = Path(old_name)
        if p.exists() and p.is_dir(): 
            new_name = input("Enter the new name of the folder: ")
            p.rename(new_name) # rename the folder
            print("Folder updated successfully")
        else: 
            print("Folder does not exist") # print this message if the folder does not exist
    except Exception as err:
        print("An error occurred: ", err)

def delete_file_folder():
    try: 
        read_file_folder() # read the files and folders to get the index of the file or folder to delete
        name = input("Enter the name of the file or folder you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir(): 
                shutil.rmtree(p) # delete the folder
                print("Folder deleted successfully")
            else: 
                p.unlink(p) # delete the file
                print("File deleted successfully")
        else: 
            print("File or folder does not exist") # print this message if the file or folder does not exist
    except Exception as err:
        print("An error occurred: ", err)

def create_file(): 
    try: 
        read_file_folder() # read the files and folders to get the index of the folder to create the file in
        name = input("Enter the name of the file you want to create: ")
        p = Path(name)
        if not p.exists(): 
            with open(name, "w") as fs: 
                data = input("Enter the data you want to write to the file: ")
                fs.write(data) # write the data to the file
            print("File created successfully")
        else: 
            print("File already exists") # print this message if the file already exists
    except Exception as err:
        print("An error occurred: ", err)

def read_file():
    try: 
        read_file_folder() # read the files and folders to get the index of the file to read
        name = input("Enter the name of the file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file(): 
            with open(name, "r") as fs: 
                data = fs.read() # read the data from the file
                print(data) # print the data
        else: 
            print("File does not exist") # print this message if the file does not exist
    except Exception as err:
        print("An error occurred: ", err)

def update_file(): 
    try: 
        read_file_folder() # read the files and folders to get the index of the file to update
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file(): 
            print("Options: ")
            print("1. Rename the file")
            print("2. Append data to the file")
            print('3. Overwrite the file')
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_name = input("Enter the new name of the file: ")
                new_name_path = Path(new_name)
                if not new_name_path.exists():
                    p.rename(new_name)
                    print("File renamed successfully")
                else:
                    print("A file with that name already exists")
            elif choice == 2:
                with open(name, "a") as fs: 
                    data = input("Enter the data you want to append to the file: ")
                    fs.write(data) # append the data to the file
                print("File updated successfully")
            elif choice == 3:
                with open(name, "w") as fs: 
                    data = input("Enter the data you want to write to the file: ")
                    fs.write(data) # overwrite the data in the file
                print("File updated successfully")
            else:
                print("Invalid choice")
        else: 
            print("File does not exist") # print this message if the file does not exist
    except Exception as err:
        print("An error occurred: ", err)

def delete_file(): 
    try: 
        read_file_folder() # read the files and folders to get the index of the file to delete
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file(): 
            p.unlink() # delete the file
            print("File deleted successfully")
        else: 
            print("File does not exist") # print this message if the file does not exist
    except Exception as err:
        print("An error occurred: ", err)

def exit_program():
    print("Exiting the program")
    exit()

print("Options: ")
print("1. Create a new folder")
print("2. Read files and folders")
print("3. Update a file or folder")
print("4. Delete a file or folder")
print("5. Creation of a new file")
print("6. Read a file")
print("7. Update a file")
print("8. Delete a file")
print("0. Exit")

choice = int(input("Enter your choice: "))

while True: 
    if choice == 1: 
        create_folder()
    elif choice == 2: 
        read_file_folder()
    elif choice == 3:
        update_folder()
    elif choice == 4:
        delete_file_folder()
    elif choice == 5:
        create_file()
    elif choice == 6:
        read_file()
    elif choice == 7:
        update_file()
    elif choice == 8:
        delete_file()
    elif choice == 0:
        exit_program()
    else:
        print("Invalid choice")