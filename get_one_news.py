import requests
from bs4 import BeautifulSoup


def get_one_dsm_news(url):
    """
    Функция возвращает новость с домена DSM.RU
    :param url: - индивидуальная ссылка новости
    :return: словарь с полями: 'title', 'time', 'text'
    """

    response = requests.get(url)
    print(url, 'код от сервера:', response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')

    one_news = {}

    # получаем заголовок новости
    one_news_title_obj = soup.find('meta', property="og:title")
    if one_news_title_obj:
        one_news['title'] = one_news_title_obj['content']

    # получаем дату новости в текстовом формате
    one_news_time_obj = soup.find('time')
    if one_news_time_obj:
        one_news['time'] = one_news_time_obj['datetime']

    # получаем текст новости:
    one_news_article_obj = soup.find('article')
    if one_news_article_obj:
        one_news_article_txt = one_news_article_obj.get_text()
        # оставляем только текст новости без ссылок на источник,
        #     лишних пробелов и перевода строк
        txt_ref_position = one_news_article_txt.find('Подробная версия:')
        if txt_ref_position > 0:
            one_news_article_shrt_txt = one_news_article_txt[:txt_ref_position]
        else:
            one_news_article_shrt_txt = one_news_article_txt
        if one_news_article_shrt_txt:
            trash = ['\n', '\r', '\t', '\xa0']
            for tr in trash:
                one_news_article_shrt_txt = one_news_article_shrt_txt.replace(tr, ' ')
            one_news_article_shrt_txt = one_news_article_shrt_txt.strip()
            one_news['text'] = one_news_article_shrt_txt

    return one_news
