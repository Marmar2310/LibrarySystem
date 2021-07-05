from collections import deque

book_list = deque()
availID = 0
print("Library my guy!")

class Book:
    name = None
    author = None
    ID = None
    taken = False

def add_book(name, author):
    temp_book = Book()
    temp_book.name = name
    temp_book.author = author
    temp_book.ID = get_next_avail_ID()
    temp_book.taken = False

    book_list.append(temp_book)

def take_book(name):
    for x in book_list:
        if x.name == name:
            x.taken = True
    return 0

def return_book(name):
    for x in book_list:
        if x.name == name:
            x.taken = False
    return 0

def get_next_avail_ID():
    return len(book_list)

def list_avail_books():
    for x in book_list:
        if not x.taken:
            print(x.name)
            print(x.ID)
    return None
