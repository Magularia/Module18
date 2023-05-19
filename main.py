# import requests
#
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
# print(r.content)

# import requests
# import json
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
#
# r = json.loads(r.content)

# print(r[0])

import requests
import lxml.html
from lxml import etree

# html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python
#
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath(
#     '/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())


ul = tree.findall("/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li")
# создаём цикл? в котором будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a') # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
    print(a.text) # из этого тега забираем текст — это и будет нашим названием

# print(title)  # выводим полученный заголовок страницы
