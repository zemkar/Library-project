from customer import Customer
from book import Book
from loan import Loan
from datetime import date, timedelta

class Library:
    def __init__(self):
        self.__customers=[]
        self.__books=[]
        self.__loans=[]
    
    def __str__(self):
        return f'CUSTOMERS:\n{self.__customers}\n\nBOOKS:\n{self.__books}\n\nLOANS:\n{self.__loans}\n'

    def add_book_from_file(self, uid, name, author, year_published, type, loaner_id):
        book = Book()
        book.set_data(uid, name, author, year_published, type, loaner_id)
        self.__books.append(book)

    def add_customer_from_file(self, uid, name, city, age, books):
        customer = Customer()
        customer.set_data(uid, name, city, age, books)
        self.__customers.append(customer)

    def add_customer(self, uid, name, city, age, books):
        customer = Customer()
        customer.set_data(uid, name, city, age, books)
        self.__customers.append(customer)
        input('customer added\nPress Enter to back in menu ')
        return customer

    def add_book(self, name, author, year_published, type):
        book = Book()
        book.set_data(self.get_uid_for_book(), name, author, year_published, type, '')
        self.__books.append(book)
        input('book added\nPress Enter to back in menu ')
        return book

    def read_loan(self, customer_id, book_id, loan_date, return_date):
        loan=Loan()
        loan.open(customer_id, book_id, loan_date, return_date)
        self.__loans.append(loan)
        
    def open_loan(self, customer, book):
        loan=Loan()

        if book.get_type() == '3':
            return_date = (date.today() + timedelta(days=2)).strftime('%d/%m/%Y')
        elif book.get_type() == '2':
            return_date = (date.today() + timedelta(days=5)).strftime('%d/%m/%Y')
        elif book.get_type() == '1':
            return_date = (date.today() + timedelta(days=10)).strftime('%d/%m/%Y')

        loan.open(customer.get_uid(), book.get_uid(), (date.today()).strftime('%d/%m/%Y'),return_date)
        book.set_customer_id(customer.get_uid())
        customer.loan_book(book.get_uid())

        self.__loans.append(loan)
        input('loan opened\nPress Enter to back in menu ')
        return loan

    def save_to_file(self):
        with open('library.txt', 'w') as lib:
            lib.write('[***]|-|Customers:\n')
            for customer in self.__customers:
                lib.write(customer.to_save())
            lib.write('[***]|-|Books:\n')
            for book in self.__books:
                lib.write(book.to_save())
            lib.write('[***]|-|Loans:\n')
            for loan in self.__loans:
                lib.write(loan.to_save())
        print('All data saved\n')

    def read_from_file(self):
        part = 0
        with open('library.txt', 'r+') as lib:
            for line in lib:
                line = line[:-1]
                line = line.split('|-|')
                if line[0] == '[***]':
                    part += 1
                    continue
                elif part == 1: 
                    line[4]= line[4].split("|*|")
                    self.add_customer_from_file(line[0],line[1],line[2],line[3],line[4])
                elif part == 2:
                    self.add_book_from_file(line[0],line[1],line[2],line[3],line[4],line[5])
                elif part == 3:
                    self.read_loan(line[0],line[1],line[2],line[3])

    def check_uid(self, new_customer_id):
        for customer in self.__customers:
            if customer.compare_uid(new_customer_id):
                return False
        return True

    def get_uid_for_book(self):
        uid = 1
        for book in self.__books:
            if uid <= int(book.get_uid()):
                uid = int(book.get_uid()) + 1
        return str(uid)

    def find_by(self, uid_or_name, where_search):
        match = []
        if where_search == 'customers':
            for customer in self.__customers:
                if (not uid_or_name.isnumeric()) and customer.get_name() == uid_or_name or customer.get_uid() == uid_or_name:
                    match.append(customer)
            return match        
        elif where_search == 'books':
            for book in self.__books:
                if (not uid_or_name.isnumeric()) and book.get_name() == uid_or_name or book.get_uid() == uid_or_name:
                    match.append(book)
            return match
        elif where_search == 'loans':
            for loan in self.__loans:
                if loan.compare_uid(uid_or_name[1], uid_or_name[0]): #customer_id, book_id
                    match.append(loan)
            return match

    def check_book(self, name, author, year):
        for book in self.__books:
            if name == book.get_name() and author == book.get_author() and year == book.get_year():
                return True
        return False

    def choice_book(self, book_name, is_get):
        books = self.find_by(book_name, 'books')
        for i in range(len(books)):
            print(f'[#{i+1}] ', end='')
            books[i].print()
            print()
        confirm = input('Confirm your choice by entering the line number\nor press enter to return: ')
        if confirm.isdigit() and int(confirm)-1 in range(len(books)):
            confirm = int(confirm) - 1
            if not is_get and books[confirm].get_loaner_id():
                customer = self.find_by(uid_or_name=books[confirm].get_loaner_id(), where_search='customers' )[0]
                print(f'This book already loaned by ')
                customer.print()
                input('\nPress enter to return ')
                return False
            else:
                return books[confirm]
        else: 
            return False

    def choice_customer(self, customer_id):
        customer = self.find_by(customer_id, 'customers')
        if customer == []:
            return False    
        customer = customer[0]
        customer_books = customer.get_books()
        lates = 0
        if customer_books != ['']:
            for book_id in customer_books[1:]:
                loan = self.find_by([book_id, customer_id], 'loans')
                if loan == []:
                    return False
                loan = loan[0]
                if not loan.is_late():
                    lates += 1
        if lates == 0:
            return customer
        else:
            if input('This customer have overdue loans\nare you sure want loan this book? (y/n) ') in ('y', 'Y', 'yes', 'Yes'):
                return customer
            return False

    def close_loan(self, customer_id, book_id): 
        for loan in self.__loans:
            if loan.compare_uid(customer_uid_to_compare=customer_id, book_uid_to_compare=book_id):
                self.__loans.remove(loan)
                self.find_by(book_id, 'books')[0].remove_customer_id()
                self.find_by(customer_id, 'customers')[0].return_book(book_id)
                print('book returned')
            
    def remove_customer(self, customer_id): 
        #customer = Customer()
        customer = self.find_by(customer_id, 'customers')[0]
        if len(customer.get_books()) > 1:
            books = customer.get_books()
            if input('This customer has unreturned books. \nReturn those books? ') in ('y', 'Y', 'yes', 'Yes'):
                for book in books[1:]:
                    self.close_loan(customer.get_uid(), book)
            elif input('Remove thos books? ') in ('y', 'Y', 'yes', 'Yes'):
                for book in books[1:]:
                    self.remove_book(book)
            else:
                print('Canseled.')
                return
        self.__customers.remove(customer)

    def remove_book(self, book_name):
        book = self.find_by(book_name, 'books')[0]
        if book.get_loaner_id():
            self.close_loan(book.get_loaner_id(), book.get_uid())
        self.__books.remove(book)
        print('Book removed.')

    def print_data(self, data_type, is_debug):
        if data_type == 'customers':
            customer = Customer()
            print(data_type+':\n id       Customer name            City           Age    Loan')
            for customer in self.__customers:
                if is_debug: print(customer)
                else: 
                    customer.print()
                    if len(customer.get_books()) > 1: print('___'+str(len(customer.get_books())-1)+' book(s)', end='')
                    else: print('___0 books', end='')
                    print()
        elif data_type == 'books':
            book = Book()
            print(data_type+':\n id   Book name                Author                   Year   Loan time    Return date')
            for book in self.__books:
                if is_debug: print(book)
                else: 
                    book.print()
                    if book.get_loaner_id():
                        return_date = self.find_by([book.get_uid(), book.get_loaner_id()], 'loans')[0].get_return_date()
                        print('______'+return_date, end='')
                    print()
        elif data_type == 'loans':
            loan = Loan()
            print(data_type)
            for loan in self.__loans:
                if is_debug: print(loan)
                else: 
                    loan.print()
                    print()
        elif data_type == 'overdue':
            loan = Loan()
            print(data_type)
            for loan in self.__loans:
                if not loan.is_late():
                    loan.print()
                    print(loan.overdue())
                    

# TODO options