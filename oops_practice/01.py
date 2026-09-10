# class and objects
# question 1: create a class named book which stores book name author name and price of the book


class book:
    book_name = "Enter Your Book Name:\n"
    book_author = "Enter Your Book author:\n"
    book_price = "Enter Your Book price:\n"

    def details_book(self):
        print(
            f'The "{self.book_name}" is written by {self.book_author},\nthe best book under {self.book_price}'
        )


a = book()
a.book_name = "venice"
a.book_author = "shakespeare"
a.book_price = "400 /-"
a.details_book()
