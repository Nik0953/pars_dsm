"""
Модуль для анализа частотности употребления слов в новостях
"""

import json

def mentioned_words(txt, words_in_rating):
    """
    Функция принимает текст,
    печатает статистику количества слов, возвращает
        words_in_rating кортежей самых упоминаемых слов по убыванию
    :param txt: текст для анализа
    :param words_in_rating: количество возвращаемых кортежей
    :return: список [words_in_rating кортежей самых упоминаемых слов по убыванию c их количеством]
    """
    # все слова - маленькими буквами
    txt = txt.lower()

    # делим на слова
    wrds_lst = txt.split()
    print('всего слов в текстах:', len(wrds_lst))

    # делаем список только с длинными словами только из букв
    min_wrd_len = 4
    lng_wrds_lst = [w for w in wrds_lst if len(w)>=min_wrd_len and w.isalpha()]
    print('всего длинных слов в текстах, длиной больше', min_wrd_len, ':', len(lng_wrds_lst))

    # набор уникальных слов
    wrds_dict = set(lng_wrds_lst)
    print('количество уникальных слов:', len(wrds_dict))

    # словарь с количеством слов - инициализация
    dict_freq ={}
    for wrd in wrds_dict:
        dict_freq[wrd] = 0

    # подсчет количества вхождений для каждого слова
    for wrd in lng_wrds_lst:
        dict_freq[wrd] += 1

    # Сортировка словаря = список кортежей: (слово, количество вхождений)
    mentioned_words = sorted(dict_freq.items(), key=lambda x: x[1], reverse=True)

    print('_____  рейтинг слов:  _____')
    for i in range(words_in_rating):
        print(i, mentioned_words[i][0],mentioned_words[i][1])

    return mentioned_words[:words_in_rating]



