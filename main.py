
from book import Book
from customer import Customer
from Library import Library
from loan import Loan
import funcs

library = Library()
book = Book()
customer = Customer()
loan = Loan()

is_one_file = False  # Save/Read all data in/from one file or in three different?
is_uid_get  = True   # Get uid for books from user?

library.read_from_file(is_one_file)


print('\n\nWelcome to simple manager of books library')

test = 0
        
while True:
    print('\n\t\t\t\tMENU:')
    print('''    
    [1]  Add a new customer           [7]  Display all loans 
    [2]  Add a new book               [8]  Display late loans 
    [3]  Loan a book                  [9]  Find book
    [4]  Return a book                [10] Find customer 
    [5]  Display all books            [11] Remove book 
    [6]  Display all customers        [12] Remove customer

    [S]  Save all                     [Q]  Save & Exit''')

    option=input("Go to: ")
    if   option=='1': # Add a new customer
        print('\n'*3)
        customer_id=input("enter customer ID please: ")
        customer_name=input("enter a name: ")
        customer_city=input("enter a city: ")
        customer_age=input("enter an age: ")
        funcs.new_customer(customer_id, customer_name, customer_city, customer_age, library)
        print('\n'*10)
    elif option=='2': # Add a new book
        print('\n'*3)
        book_id = '1'
        if is_uid_get:
            book_id=input("enter a book ID please: ")
        book_name=input("enter a name: ")
        book_author=input("enter an author: ")
        book_year_published=input("enter a year publishment: ")
        book_type=input("set a maximum loan time for the book\n [1] -up to 10 days\n [2] -up to 5 days\n [3] -up to 2 days\n enter here your option: ")
        funcs.new_book(is_uid_get, book_id, book_name, book_author, book_year_published, book_type, library)
        print('\n'*10)
    elif option=='3': # Loan a book
        print('\n'*3)
        book_name=input("enter a book name or id: ")
        print('\n'*3)
        customer_id=input("enter customer id or name please: ")
        funcs.open_loan(book_name, customer_id, library)
        print('\n'*10)
    elif option=='4': # Return a book 
        print('\n'*3)
        book_name=input("enter a book name or id: ")
        funcs.close_loan(book_name, library)
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
        funcs.search(input('Enter book name or id: '), 'books')
        print('\n'*3)
    elif option=='10':# Find customer
        print('\n'*3)
        funcs.search(input('Enter customer id or name: '), 'customers')
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
        library.save_to_file(is_one_file)
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
            funcs.new_customer('11', 'aa', 'customer city', '11', library)
            funcs.new_customer('12', 'aa', 'customer city', '11', library)
            funcs.new_customer('11', 'aa', 'customer city', '11', library)
        elif test == 2:                       # add books
            funcs.new_book(is_uid_get, '100', 'zz', 'book author', '11', '1', library)
            funcs.new_book(is_uid_get, '101', 'xx', 'book _author', '11', '2', library)
            funcs.new_book(is_uid_get, '101', 'xx', 'book _author', '11', '2', library)
        elif test == 3:                       # loan this books
            funcs.open_loan('zz', '11', library)
            funcs.open_loan('101', '11', library)
            funcs.open_loan('xx', '11', library)
        elif test == 4:                       # return book
            funcs.close_loan('xx', library)
        elif test == 5:
            funcs.open_loan('101', '11', library)
            library.remove_book('xx')
        test += 1
    elif option == 's':
        library.save_to_file(is_one_file)

    