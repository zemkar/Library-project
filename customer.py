class Customer(object):
    # def __init__(self, uid, name, city, age):
    #     self.__uid=uid
    #     self.__name=name
    #     self.__city=city
    #     self.__age=age
    #     self.__books = ['']

    def set_data(self, uid, name, city, age, books):
        self.__uid=uid
        self.__name=name
        self.__city=city
        self.__age=age
        self.__books = books

    def __str__(self):
        return f'{self.__uid}, {self.__name}, {self.__city}, {self.__age}, {self.__books}'    

    def print(self):
        print(self.__uid + "_"*(10-len(self.__uid)), end='')
        print(self.__name + "_"*(25-len(self.__name)), end='')
        print(self.__city + "_"*(15-len(self.__city)), end='')
        print(self.__age + "_"*(4-len(self.__age)), end='')  

    def to_save(self):
        str_books = ''
        for i in range(len(self.__books)):
            if i < len(self.__books)-1:
                str_books+=self.__books[i]+'|*|'
            else:
                str_books+=self.__books[i]
        return f'{self.__uid}|-|{self.__name}|-|{self.__city}|-|{self.__age}|-|{str_books}\n'

    def get_uid(self):
        return self.__uid

    def get_name(self):
        return self.__name

    def loan_book(self, book_id):
        self.__books.append(str(book_id))

    def return_book(self, book_id):
        self.__books.remove(str(book_id))

    def get_books(self):
        return self.__books

    def compare_uid(self, uid_to_compare):
        if self.__uid == uid_to_compare:
            return True
        return False
