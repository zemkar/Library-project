class Book(object):
    # def __init__(self, book_id, name, author, year_published, type):
    #     self.__uid=book_id
    #     self.__name=name
    #     self.__author=author
    #     self.__year_published=year_published
    #     self.__type=type
    #     self.__loaner_id = ''
        
    def set_data(self, book_id, name, author, year_published, type, loaner_id):
        self.__uid=book_id
        self.__name=name
        self.__author=author
        self.__year_published=year_published
        self.__type=type
        self.__loaner_id = loaner_id
        

    def __str__(self):
        return f'{self.__uid}, {self.__name}, {self.__author}, {self.__year_published}, {self.__type}, {self.__loaner_id}'

    def print(self):
        print(str(self.__uid) + "_"*(6-len(str(self.__uid))), end='')
        print(self.__name + "_"*(25-len(self.__name)), end='')
        print(self.__author + "_"*(25-len(self.__author)), end='')
        print(self.__year_published + "_"*(6-len(self.__year_published)), end='')
        if self.__type == '3': print('__2_days', end='')
        elif self.__type == '2': print('__5_days', end='')
        elif self.__type == '1': print('_10_days', end='')
        


    def to_save(self):
        return f'{self.__uid}|-|{self.__name}|-|{self.__author}|-|{self.__year_published}|-|{self.__type}|-|{self.__loaner_id}\n'

    def get_uid(self):
        return self.__uid

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year_published

    def get_loaner_id(self):
        if self.__loaner_id == '':
            return False
        return self.__loaner_id

    def compare_uid(self, uid_to_compare):
        if self.__uid == uid_to_compare:
            return True
        return False

    def loan(self, customer_id):
        self.__loaner_id = customer_id

    def get_type(self):
        return self.__type

    def set_customer_id(self, customer_id):
        self.__loaner_id = customer_id

    def remove_customer_id(self):
        self.__loaner_id = ''
