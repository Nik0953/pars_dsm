""""
Модуль для скачивания всех новостей
с сайта https://dsm.ru
"""

# import requests
# from bs4 import BeautifulSoup
from get_one_news import *
import pprint
import time
import json

domain = 'https://dsm.ru'

next_page_ref = '/news'
# для отладки    next_page_ref = '/news/2363?PAGEN_2=136'

# список адресов всех статей
news_all_ref = []

# цикл по всем страницам с новостями - получаем url новостей
while next_page_ref:

    url = f'{domain}{next_page_ref}'

    time.sleep(3)
    print(url)

    response = requests.get(url)

    print('код от сервера:', response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')

    # получаем все разделы со ссылками на новости на текущей странице
    news_div_on_page = soup.find_all('a', class_='inner')
    # cсоздаем массив относительных ссылок на новости на текущей странице
    news_ref_on_page = [n_div.get('href') for n_div in news_div_on_page]

    news_all_ref += news_ref_on_page

    # Находим ссылку на следующую страницу новостей
    next_page_ref = ''
    next_page_li = soup.find('li', class_='next')
    #pprint.pprint(next_page_li)
    if next_page_li:
        if next_page_li.find('a'):
            next_page_ref = next_page_li.find('a').get('href')

    print('Поиск страниц с блоками новостей:', next_page_ref)


# ********* по полученным ссылкам читаем новости и сохраняем их в файл   *********

#список из словарей-новостей
news = []

for news_ref in news_all_ref:
    url = f'{domain}{news_ref}'
    news.append(get_one_dsm_news(url))
    time.sleep(3)

# Сохранение в файл
    output_file_name = 'articles.json'
    with open(output_file_name, 'w') as f:
        json.dump(news, f, ensure_ascii=False)


