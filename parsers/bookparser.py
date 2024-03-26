import re
from locators.book_atributes import BookAtributeloacator 
class BookParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    def __init__(self,elem):
        self.parent = elem


    def __str__(self):
        return f'<Book {self.name} costing {self.price}$ with rating of ({self.rating} Stars>)\n'
    
    @property
    def link(self):
        locator = BookAtributeloacator.BOOK_NAME
        link = self.parent.select_one(locator)
        return link.attrs['href']


    @property
    def name(self):
        locator = BookAtributeloacator.BOOK_NAME      
        link =  self.parent.select_one(locator)
        return link.attrs['title']
    
    
    @property
    def price(self):
        locator = BookAtributeloacator.BOOK_PRICE
        price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\\.[0-9]+)'
        matcher = re.search(pattern, price)
        price = float(matcher.group(1))
        return price
    
    
    @property
    def rating(self):
        locator = BookAtributeloacator.BOOK_RATING
        star = self.parent.select_one(locator)
        classes = star.attrs['class']
        rating_class = [elem for elem in classes if elem !='star-rating' ]
        bookRating = BookParser.RATINGS.get(rating_class[0])
        return bookRating

    
    @property
    def instock(self):
        locator = BookAtributeloacator.BOOK_INSTOCK
        return self.parent.select_one(locator).string
    
