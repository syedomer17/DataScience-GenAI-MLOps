import json 
import random 
import string 
from pathlib import Path 
from datetime import datetime 

class Library: 

    database = "Library.json"
    data = {
        "books": [],
        "members": [],
    }

    # load existing data to json or create new json file if it doesn't exist

    if Path(database).exists(): 
        with open(database, "r") as fs: 
            content = fs.read().strip() # strip remove unnecessary spaces and newlines
            if content: 
                data = json.loads(content)
    else: 
        with open(database, "w") as fs: 
            json.dump(data, fs, indent=4)
    
    @classmethod
    def save_data(cls): 
        with open(cls.database, 'w') as fs: 
            json.dump(cls.data, fs, indent=4)


    def generate_id( prefix = "B"): 
        random_id = ""
        for i in range(5): 
            random_id += random.choice(string.ascii_uppercase + string.digits)
        
        return prefix +"-" + random_id
    
    def add_book(self): 
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        copies = int(input("Enter number of copies: "))

        book = {
            "id": Library.generate_id(),
            "title": title,
            "author": author,
            "copies": copies,
            "available_copies": copies,
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        Library.data["books"].append(book)
        Library.save_data()
    
    def list_books(self): 
        if not Library.data["books"]: 
            print("No books available.")
            return

        for b in Library.data["books"]: 
            print(f"{b["id"]:12} {b['title'][:24]:25} {b['author'][:19]:20} {b['available_copies']}/{b['copies']:>3}")

    def add_member(self): 
       name = input("Enter member name: ")
       email = input("Enter member email: ")

       member = {
           "id": Library.generate_id(prefix="M"),
           "name": name, 
           "email": email,
           "borrowed": [],
       }

       Library.data["members"].append(member)
       Library.save_data()
       print("Member added successfully.")
    
    def list_members(self): 
        if not Library.data["members"]: 
            print("No members found.")
            return
        
        for m in Library.data["members"]: 
            print(f"{m['id']:12} {m['name'][:24]:25} {m['email'][:29]:30} Borrowed: {len(m['borrowed'])}")

    def borrow_book(self): 
        member_id = input("Enter member ID: ").strip()
        members = [m for m in Library.data["members"] if m ["id"] == member_id]

        if not members: 
            print("Member not found.")
            return

        member = members[0]

        book_id = input("Enter book ID: ").strip()
        books = [ b for b in Library.data["books"] if b ["id"] == book_id]

        if not books: 
            print("Book not found.")
            return 
        
        book = books[0]

        if book["available_copies"] <= 0: 
            print('Sorry, No copies available for this book.')
            return 
        
        borrow_entry = {
            "book_id": book["id"],
            "title": book["title"],
            "borrowed_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        member["borrowed"].append(borrow_entry)
        book["available_copies"] -= 1
        Library.save_data()

        print("Book borrowed successfully.")
    
    def return_book(self): 
        member_id = input("Enter member ID: ").strip()
        members = [m for m in Library.data["members"] if m ["id"] == member_id]

        if not members: 
            print("Member not found.")
            return

        member = members[0]

        if not member["borrowed"]: 
            print("No borrowed books found for this member.")
            return 
        
        print("Borrowed Books:")
        for i, b in enumerate(member["borrowed"], start = 1): 
            print(f"{i}. {b["title"]} {b["book_id"]}")

        try: 
            choice = int(input("Enter the number to return: "))

            selected = member["borrowed"].pop(choice - 1)

        except Exception as err: 
            print("Invalid choice.", err)
            
        books = [b for b in Library.data["books"] if b["id"] == selected["book_id"]]

        if books: 
            books[0]["available_copies"] += 1

        Library.save_data()
        print("Book returned successfully.")
    
    def exit(self): 
        print("Exiting...")
        exit(0)
        

hello = Library()

print("="*50)
print("Welcome to the Library Management System")
print("="*50)

while True: 
    print("1. Add Book")
    print("2. List Books")
    print("3. Add Member")
    print("4. List Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("0. Exit")

    print("-"*50)

    choice = input("Enter your choice: ")

    match choice: 
        case "1": 
            hello.add_book()
        case "2": 
            hello.list_books()
        case "3":         
            hello.add_member()
        case "4":         
            hello.list_members()
        case "5":         
            hello.borrow_book()
        case "6":         
            hello.return_book()
        case "0":         
            hello.exit()