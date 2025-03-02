class BookNotFoundException(Exception):
    pass
class BookAlreadyBorrowedException(Exception):
    pass
class MemberLimitExceededException(Exception):
    pass
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book):
            if len(self.borrowed_books) >= 3:
                raise MemberLimitExceededException("You cannot borrow more than three books")
            if book.is_borrowed:
                raise BookAlreadyBorrowedException("this book is already borrowed, sorry")
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        
    def return_book(self, book):
            if book in self.borrowed_books:
                book.is_borrowed = False
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'")
            else:
                 print(f"{self.name} did not borrow '{book.title}'")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Member {name} added to the library.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException("Book not found")
            
    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise Exception("Member not found")
        
        try:
            book = self.find_book(book_title)
            member.borrow_book(book)
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise Exception("Member not found")

        try:
            book = self.find_book(book_title)
            member.return_book(book)
        except BookNotFoundException as e:
            print(e)

lib = Library()
lib.add_book("Harry Potter 1", "J.K. Rowling")
lib.add_book("The Great Gatsby", "F. Scott Fitzgerald")
lib.add_book("To Kill a Mockingbird", "Harper Lee")
lib.add_member("Muhammadsodiq")
lib.add_member("Oliver")

lib.borrow_book("Muhammadsodiq", "Harry Potter 1")
lib.borrow_book("Muhammadsodiq", "The Great Gatsby")
lib.borrow_book("Oliver", "To Kill a Mockingbird")
lib.return_book("Muhammadsodiq", "Harry Potter 1")