import bs4
import requests

'''basic_url = 'https://books.toscrape.com/catalogue/page-{}.html'
for p in range(1,11):
    print(basic_url.format(p))'''


'''basic_url = 'https://books.toscrape.com/catalogue/page-{}.html'
result = requests.get(basic_url.format('1'))
soup = bs4.BeautifulSoup(result.text,'html.parser')
print(soup.select('.product_pod'))
print(len(soup.select('.product_pod')))'''


'''basic_url = 'https://books.toscrape.com/catalogue/page-{}.html'
result = requests.get(basic_url.format('1'))
soup = bs4.BeautifulSoup(result.text,'html.parser')
books = soup.select('.product_pod')
example = books[0].select('.star-rating.Three')
print(example)
print(books)
example1 = books[0].select('a')[1]['title']
print(example1)'''
