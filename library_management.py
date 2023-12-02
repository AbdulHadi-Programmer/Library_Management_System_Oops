### Library Management:
# create a method that check both var lenth are same or not
# 
class Library:
    def __init__(self):
        self.books = [
            "To Kill a Mockingbird by Harper Lee",
            "1984 by George Orwell",
            "The Great Gatsby by F. Scott Fitzgerald",
            "Pride and Prejudice by Jane Austen",
            "The Catcher in the Rye by J.D. Salinger",
            "One Hundred Years of Solitude by Gabriel Garcia Marquez",
            "The Hobbit by J.R.R. Tolkien",
            "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
            "The Da Vinci Code by Dan Brown",
            "The Hitchhiker's Guide to the Galaxy by Douglas Adams"
            ]
        self.numofbooks = int(len(self.books))
        # self.numofbooks = 10
        
    def show_books(self):
        print('List of all Books:')
        for num, i in enumerate(self.books, start=1):
            print(f'{num}. {i}')
    
    def add(self):
        self.b = input("Enter the book: ")
        self.books.append(self.b)
        self.numofbooks = len(self.books)
    
    # Arrange The function, this function can be written in 3-4 lines remove this existing
    def count(self):
        print(f'The Library has {len(self.books)} books. The no of book in the list is {self.numofbooks}')
        if len(self.books) != self.numofbooks:
            print("Both list are different. They have different Length")
        else:
            print('All books in book list and numofbooks is same')
            
    def remove_book(self):
        lib.show_books()
        self.r = int(input('Enter the book num to remove: ')) - 1
        self.a = self.books.pop(self.r)
        self.numofbooks = len(self.books)
        print(f"The book '{self.a}' has been removed")

lib = Library()


while True:
    choice = int(input('\nWelcome to Library Management System\n1) Add Books\n2) Show Books\n3) Remove Books\n4) Count the Book List and Length of books\n5) Exit\nEnter the option:- '))
    if choice == 1:
        lib.add()
    elif choice == 2:
        lib.show_books()
    elif choice == 3:
        lib.remove_book()
    elif choice == 4:
        lib.count()
    elif choice == 5:
        break
    else:
        print('Invalid Input')
        choice = int(input('\nWelcome to Library Management System\n1) Add Books\n2) Show Books\n3) Remove Books\n4) Count the Book List and Length of books\n5) Exit\nEnter the option:- '))
        