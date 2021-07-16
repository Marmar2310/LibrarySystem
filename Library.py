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
    return "added book" + name + "by" + author

def add_list_books(arr_book):
    for x in arr_book:
        temp_book = Book()
        temp_book.name = x[0]
        temp_book.author = x[1]
        temp_book.ID = get_next_avail_ID()
        temp_book.taken = False
        book_list.append(temp_book)
        print("added" + x[0] + "by" + x[1])

def take_book(name):
    for x in book_list:
        if x.name == name:
            x.taken = True
    return "took book" + name

def return_book(name):
    for x in book_list:
        if x.name == name:
            x.taken = False
    return "returned book" + name

def list_author_books(author):
    for x in book_list:
        if x.author == author:
            print(x.name)

def get_next_avail_ID():
    return len(book_list)

def list_avail_books():
    for x in book_list:
        if not x.taken:
            print(x.name)
            print(x.ID)
    return None
