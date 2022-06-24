
from book import Book
from customer import Customer
import funcs
from Library import Library
from loan import Loan

library = Library()
book = Book()
customer = Customer()
loan = Loan()

library.read_from_file()


if __name__=='__main__':

    print("GREETINGS! ENTER YOUR SELLECTED OPTION BELLOW")


while True:
    print("[1] Add a new customer")
    print("[2] Add a new book")
    print("[3] Loan a book")
    print("[4] Return a book")
    print("[5] Display all books")
    print("[6] Display all customers")
    print("[7] Display all loans")
    print("[8] Display late loans")
    print("[9] Find book by name")
    print("[10] Find customer by name")
    print("[11] Remove book")
    print("[12] Remove customer")
    print("[Q] for quit")

    option=input("enter here your sellected option: ")
    if option=='1':   # Add a new customer
        customer_id=input("enter customer ID please: ")
        if not library.check_uid(customer_id):
            print("This ID is already taken.")
            input('Press Enter to back in menu ')
            continue
        customer_name=input("enter a name: ")
        customer_city=input("enter a city: ")
        customer_age=input("enter an age: ")
        customer = library.add_customer(customer_id, customer_name, customer_city, customer_age, [''])
    elif option=='2': # Add a new book
        #book_id=input("enter a book ID please: ")
        book_name=input("enter a name: ")
        book_author=input("enter an author: ")
        book_year_published=input("enter a year publishment: ")
        if library.check_book(book_name, book_author, book_year_published):
            if not input('The library already has the same book, do you still want to add it? (y/n) ') in ('y', 'Y', 'yes', 'Yes'):
                continue
        book_type=input("set a maximum loan time for the book\n [1] -up to 10 days\n [2] -up to 5 days\n [3] -up to 2 days\n enter here your option: ")
        book = library.add_book(book_name, book_author, book_year_published, book_type)
    elif option=='3': # Loan a book
    # choice book
        book_name=input("enter a book name: ")
        book = library.choice_book(book_name, True)
        if not book:
            continue
    # choice customer
        customer_id=input("enter customer ID please: ")
        customer = library.choice_customer(customer_id)
        if not customer:
            continue
    # registration in loans
        loan = library.open_loan(customer, book)
    elif option=='4': # Return a book 
    # choice book
        book_name=input("enter a book name: ")
        book = library.choice_book(book_name, True)
        if not book:
            continue
        if book.get_loaner_id():
            library.close_loan(book.get_loaner_id(), book.get_uid())
        else:
            print('This book not loaned')
        input('Press Enter to continue ')
    elif option=='5':#  Display all books")
        library.print_data('books', False)
        input('Press enter to continue')
    elif option=='6':#  Display all customers")
        library.print_data('customers', False)
        input('Press enter to continue')
    elif option=='7':#  Display all loans")
        library.print_data('loans', False)
        input('Press enter to continue')
    elif option=='8':#  Display late loans")
        library.print_data('overdue', False)
        input('Press enter to continue')

    elif option=='9':#  Find book by name")
        pass
    elif option=='10':# Find customer by name")
        pass
    elif option=='11':# Remove book")
        pass
    elif option=='12':# Remove customer")
        pass
    elif option=='Q':#  for quit")
        break



# TEST OPTIONS ------------------------------------------------------------     
#    
    elif option=='t':
        library.print_data('customers', True)
        print()
        library.print_data('books', True)
        print()
        library.print_data('loans', True)
    elif option == 's':
        library.save_to_file()

    