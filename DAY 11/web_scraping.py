import bs4
import requests

result = requests.get('https://www.videoschool.com/')

# print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text, 'html.parser')
# print(soup)
# print(soup.select('title'))
# print(soup.select('p'))
# print(len(soup.select('p')))
# print(soup.select('h1'))
# print(soup.select('title')[0])
# print(soup.select('title')[0].getText())
# my_p= soup.select('p')[6].getText()
# print(my_p)


# central_block = soup.select('.fusion-text.fusion-text-1')
# central_block1 = soup.select('.fusion-text.fusion-text-1 h5')
# central_block2 = soup.select('.fusion-text.fusion-text-1 h5')[0]
# print(central_block)
# print("\n")
# print(central_block1)
# print("\n")
# print(central_block2)
# print("\n")
#
# for h in central_block:
#    print(h.getText())
# print("\n")
#
# for h in central_block1:
#    print(h.getText())
# print("\n")
#
# for h in central_block2:
#    print(h.getText())
# print("\n")


images = soup.select('img')
print(images)
print("\n")

images1= soup.select('.img-responsive')
for im in images1:
    print(im)

print("\n")

images3 = soup.select('.img-responsive')[0]['src']
print(images3)
print("\n")

images4 = requests.get(images3)
print(images4)
print("\n")

f = open('my_image.jpg','wb')
f.write(images4.content)
f.close()
