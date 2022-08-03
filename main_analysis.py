"""
модуль статистики:

Новости с сайта https://dsm.ru уже прочитаны в модуле  'main_get_news.py'
и записаны в файл  'articles.json'

В этом модуле проводим анализ частотности текста новостей:
какие ключевые слова в последних новостях
встречаются чаще, чем в массиве предыдущих новостей.
"""
from txt_stat import *

# **********  читаем собранные новости   **********
with open('articles.json', 'r') as f:
    articles = json.load(f)

print('количество новостей:', len(articles))

# *******   создаем словарь    *******
# собираем все тексты в один
txt_all = ""
for art in articles:
    txt_all += art['text']

print('Статистический анализ всех текстов:')
mentioned_words(txt_all, 100)

# количество последних новостей для сравнения с предыдущими
last_news_number = 400
top_wrds = 75

print('\n\n', '*'*80)

print('Анализ последних', last_news_number, 'текстов по сравнению с предыдущими:')
txt_last = ""
for art in articles[:last_news_number]:
    txt_last += art['text']
last_wrds = mentioned_words(txt_last, top_wrds)

print('\n\n', '*'*80)
print('Предыдущие тексты:')
txt_prev = ""
for art in articles[last_news_number:]:
    txt_prev += art['text']
prev_wrds = mentioned_words(txt_prev, top_wrds)

#print(last_wrds)

# Новые слова в рейтинге:
last_wrds_lst = [wrd[0] for wrd in last_wrds]
prev_wrds_lst = [wrd[0] for wrd in prev_wrds]
print('\n\n\n ******    Новые слова в рейтинге:    ******')
for wrd in last_wrds_lst:
    if wrd not in prev_wrds_lst:
        print(wrd)

