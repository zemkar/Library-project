from datetime import date, datetime


class Loan(object):
    # def __init__(self, customer_id, book_id, loan_date, return_date):
    #     self.__customer_id=customer_id
    #     self.__book_id=book_id
    #     self.__loan_date=loan_date
    #     self.__return_date=return_date

    def open(self, customer_id, book_id, loan_date, return_date):
        self.__customer_id=customer_id
        self.__book_id=book_id
        self.__loan_date=loan_date
        self.__return_date=return_date
        
    def to_save(self):
        return f'{self.__customer_id}|-|{self.__book_id}|-|{self.__loan_date}|-|{self.__return_date}\n'

    def compare_uid(self, customer_uid_to_compare, book_uid_to_compare):
        if self.__book_id == book_uid_to_compare and self.__customer_id == customer_uid_to_compare:
            return True
        return False

    def is_late(self):
        if datetime.strptime(self.__return_date, '%d/%m/%Y') < datetime.today():
            return False
        return True

    def get_return_date(self):
        return self.__return_date

    def __str__(self):
        return f'{self.__customer_id}, {self.__book_id}, {self.__loan_date}, {self.__return_date}'

    def print(self):
        print(f'{self.__customer_id}, {self.__book_id}, {self.__loan_date}, {self.__return_date}', end='')
        
    def overdue(self):
        late = (datetime.strptime(self.__return_date, '%d/%m/%Y') - datetime.today()).days + 1
        if late >= 0:
            return f',  last {late} days'
        else:
            return f',  late {abs(late)} days'