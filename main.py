
from book import Book
from customer import Customer
from Library import Library
from loan import Loan

library = Library()
book = Book()
customer = Customer()
loan = Loan()

library.read_from_file()


if __name__=='__main__':

    print("GREETINGS! ENTER YOUR SELLECTED OPTION BELLOW")

test = 0
        
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
    if   option=='1': # Add a new customer
        print('\n'*3)
        customer_id=input("enter customer ID please: ")
        customer_name=input("enter a name: ")
        customer_city=input("enter a city: ")
        customer_age=input("enter an age: ")
        if not customer_id.isnumeric():
            if not input('This id contain letters. Are you sure want to use it? (y/n) ') in ('y', 'Y', 'yes', 'Yes'):
                continue
        if not library.check_uid(customer_id):
            print("This ID is already taken.")
            input('Press Enter to back in menu ')
            continue
        if not customer_name.isalpha() or not customer_city.isalpha() or not customer_age.isnumeric():
            print("Input error. Name and city can only contain letters, and age must be a number\n ")
            input('Press Enter to back in menu ')
            continue
        customer = library.add_customer(customer_id, customer_name, customer_city, customer_age, [''])
        print('\n'*10)
    elif option=='2': # Add a new book
        print('\n'*3)
        #book_id=input("enter a book ID please: ")
        book_name=input("enter a name: ")
        book_author=input("enter an author: ")
        book_year_published=input("enter a year publishment: ")
        book_type=input("set a maximum loan time for the book\n [1] -up to 10 days\n [2] -up to 5 days\n [3] -up to 2 days\n enter here your option: ")
        if not book_author.isalpha() or not book_year_published.isnumeric() or not book_type in ('1', '2','3'):
            print("Input error. Name of author can only contain letters, and year must be a number\n ")
            input('Press Enter to back in menu ')
            continue
        if library.check_book(book_name, book_author, book_year_published):
            if not input('The library already has the same book, do you still want to add it? (y/n) ') in ('y', 'Y', 'yes', 'Yes'):
                continue
        book = library.add_book(book_name, book_author, book_year_published, book_type)
        print('\n'*10)
    elif option=='3': # Loan a book
        print('\n'*3)
    # choice book
        book_name=input("enter a book name or id: ")
        book = library.choice_book(book_name, False)
        if not book:
            continue
    # choice customer
        print('\n'*3)
        customer_id=input("enter customer id or name please: ")
        customer = library.choice_customer(customer_id)
        if not customer:
            continue
        loan = library.open_loan(customer, book)
        print('\n'*10)
    elif option=='4': # Return a book 
        print('\n'*3)
        book_name=input("enter a book name or id: ")
        book = library.choice_book(book_name, True)
        if not book:
            continue
        if book.get_loaner_id():
            library.close_loan(book.get_loaner_id(), book.get_uid())
        else:
            print('This book not loaned')
        input('Press Enter to continue ')
        print('\n'*10)
    elif option=='5': # Display all books
        print('\n'*3)
        library.print_data('books', False)
        input('Press enter to continue')
        print('\n'*10)
    elif option=='6': # Display all customers
        print('\n'*3)
        library.print_data('customers', False)
        input('Press enter to continue')
        print('\n'*10)
    elif option=='7': # Display all loans
        print('\n'*3)
        library.print_data('loans', False)
        input('Press enter to continue')
        print('\n'*10)
    elif option=='8': # Display late loans
        print('\n'*3)
        library.print_data('overdue', False)
        input('Press enter to continue')
        print('\n'*10)
    elif option=='9': # Find book
        print('\n'*3)
        books = library.find_by(input('Enter book name or id: '), 'books')
        for book in books:
            book.print()
            print()
        input('Press enter to continue')
        print('\n'*3)
    elif option=='10':# Find customer
        print('\n'*3)
        customers = library.find_by(input('Enter customer id or name: '), 'customers')
        for customer in customers:
            customer.print()
            print()
        input('Press enter to continue')
        print('\n'*3)
    elif option=='11':# Remove book
        print('\n'*3)
        book_name = input('Enter book id or name: ')
        library.remove_book(book_name)
        print('\n'*10)
    elif option=='12':# Remove customer
        print('\n'*3)
        customer_id = input('Enter customer id or name: ')
        library.remove_customer(customer_id)
        input('Press enter to continue')
        print('\n'*10)
    elif option in ('q','Q'): # for quit
        library.save_to_file()
        print('\n'*10)
        break



# TEST OPTIONS ------------------------------------------------------------     
#    
    elif option=='t':
        library.print_data('customers', True)
        print()
        library.print_data('books', True)
        print()
        library.print_data('loans', True)
        if test  == 1: # add customer
            customer = library.add_customer('11', 'aa', 'customer_city', '11', [''])
        elif test == 2:                       # add books
            book = library.add_book('zz', 'book_author', '11', '1')
            book = library.add_book('xx', 'book_author', '11', '2')
        elif test == 3:                       # loan this books
            book = library.choice_book('zz', False)
            customer = library.choice_customer('11')
            loan = library.open_loan(customer, book)

            book = library.choice_book('219', False)
            customer = library.choice_customer('11')
            loan = library.open_loan(customer, book)

            book = library.choice_book('xx', False)
            customer = library.choice_customer('11')
            if customer and book:
                loan = library.open_loan(customer, book)
        elif test == 4:                       # return book
            book = library.choice_book('xx', True)
            library.close_loan(book.get_loaner_id(), book.get_uid())
        elif test == 5:
            book = library.choice_book('219', False)
            customer = library.choice_customer('11')
            loan = library.open_loan(customer, book)

            library.remove_book('xx')
        test += 1
    elif option == 's':
        library.save_to_file()

    