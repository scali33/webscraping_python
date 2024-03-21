from bs4 import BeautifulSoup

from locators.book import Book_location
from parsers.bookparser import BookParser

class BookPage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')
    @property
    def books(self):
        locator = Book_location.BOOK_LOCAL
        books_tags = self.soup.select(locator)
        return [BookParser(book) for book in books_tags]