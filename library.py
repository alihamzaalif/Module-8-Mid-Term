class Library:
    book_list = []
    def __init__(self):
        pass
    
    def entry_book(self,book):
        Library.book_list.append(book)

    @classmethod
    def list_books(self):
        print('Library Books:')
        for book in Library.book_list:
            print(book.view_book_info)
        print()
    
    def borrow(self, book_id):
        borrow = False
        for book in Library.book_list:
            if int(book.book_id) == book_id:
                borrow = True
                if book.book_availability:
                    book.borrow_book()
                    print(f'Book {book.book_title} borrowed successfully')
                    break
                else:
                    print(f'Book {book.book_title} is Not Available')

        if not borrow:
            print(f'Book with ID {book_id} is not in our library')   
    
    def ret(self, book_id):
        borrow = False
        for book in Library.book_list:
            if book.book_id == book_id:
                borrow = True
                if not book.book_availability:
                    book.return_book()
                    print(f'Book {book.book_title} returned successfully')
                    borrow = True
                else:
                    print(f'Book {book.book_title} is already in the library')
        if not borrow:
            print(f'Book with ID {book.book_title} is not in our library')   


class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    @property
    def book_availability(self):
        return self.__availability
    
    @property
    def book_title(self):
        return self.__title
            
    @property
    def book_id(self):
        return int(self.__book_id)
    
    def borrow_book(self):
        self.__availability = False
    
    def return_book(self):
        self.__availability = True
        
    @property
    def view_book_info(self):
        return f'ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {'Available' if self.__availability else 'Not Available'}'
    
library = Library()

library.entry_book(Book(101, 'Python Programming', 'John Dee', True))
library.entry_book(Book(102, 'Data Science Essentials', 'Jane Smith', True))
library.entry_book(Book(103, 'Machine Learning', 'Alan Turing', True))
library.entry_book(Book(104, 'Artificial Intelligence', 'Marvin Minsky', True))
library.entry_book(Book(105, 'Deep Learning', 'Yann LeCun', False))
library.entry_book(Book(106, 'Natural Language Processing', 'Christopher Manning', True))
library.entry_book(Book(107, 'Statistics For Data Science', 'David C. Hsu', True))
library.entry_book(Book(108, 'Python for Data Analysis', 'Wes McKinney', True))


while(True):
    print("""-----Welcome to the Library-----
1. View All Books
2. Borrow Book
3. Return Book
4. Exit
""")
    print()
    c = int(input('Enter your choice: '))
    print()
    if(c==4):
        break
    elif(c==1):
        library.list_books()
    elif(c==2):
        print()
        id = int(input('Enter book ID to borrow: '))
        library.borrow(id)
        print()
    elif(c==3):
        print()
        id = int(input('Enter book ID to return: '))
        library.ret(id)
        print()
    else:
        print('Sorry, Invalid input. Input between 1-4')
        print()

