from book import Book
from customer import Customer
from Library import Library
from loan import Loan

library = Library()
book = Book()
customer = Customer()
loan = Loan()

def new_customer(customer_id, customer_name, customer_city, customer_age, library):
    if not customer_id.isnumeric():
        input("customer id can't contain letters. ")
        return False
    if not library.check_uid(customer_id):
        print("This id is already taken.")
        input('Press Enter to back in menu ')
        return False
    if library.check_uid(customer_id):
        library.add_customer(customer_id, customer_name, customer_city, customer_age, [''])
        return library
    return False

def new_book(is_uid_get, uid, book_name, book_author, book_year_published, book_type, library):
    if not uid.isnumeric():
        input('Book id must be a number. \nPress Enter to  back in menu')
        return False
    if not (uid := library.get_uid_for_book(is_uid_get, uid)):
        input('This ID is already taken.\nPress Enter to  back in menu')
        return False
    if library.check_book(book_name, book_author, book_year_published):
        if not input('The library already has the same book, do you still want to add it? (y/n) ') in ('y', 'Y', 'yes', 'Yes'):
            return False
    book = library.add_book(is_uid_get, uid, book_name, book_author, book_year_published, book_type)
    return library

def open_loan(book_name, customer_id, library):
    book = library.choice_book(book_name, False)
    if not book:
        return False
    customer = library.choice_customer(customer_id)
    if not customer:
        return False
    loan = library.open_loan(customer, book)

    return library

def close_loan(book_name, library):
    book = library.choice_book(book_name, True)
    if not book:
        return False
    if book.get_loaner_id():
        library.close_loan(book.get_loaner_id(), book.get_uid())
    else:
        print('This book not loaned')
    input('Press Enter to continue ')

    return library

def search(uid_or_name, where_search):
    if (data := library.find_by(uid_or_name, where_search)):
        data.print()