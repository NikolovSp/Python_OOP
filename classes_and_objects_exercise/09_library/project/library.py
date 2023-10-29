from project.user import User
from typing import List, Dict


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str:[list]] = {}  # {"J.K.Rowling": [Deadly Hallows, Rooms of Secrets]}
        self.rented_books: Dict[str:{str, int}] = {}  # {"Ivan": {Deadly Hallows: 10}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f'{book_name} successfully rented for the next {days_to_return} days!'

        # here we might have to iterate thorugh the list of rented books...
        # return (f'The book "{book_name}" is already '
                # f'rented and will be available in {self.rented_books[user.username][book_name]} days!')

        for data in self.rented_books.values():
            if book_name in data:
                return f'The book "{book_name}" is already rented and will be available in {data[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)

        else:
            return f"{user.username} doesn't have this book in his/her records!"
