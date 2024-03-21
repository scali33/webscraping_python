import requests
from pages.booksPage import BookPage

print('all the books that have a rating of greater than 4')


page_content = requests.get(f'https://books.toscrape.com/catalogue/page-{1}.html').content
page = BookPage(page_content)

books = page.books
for page_num in range(50):
    url = f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    page = BookPage(page_content)
    books.extend(page.books)