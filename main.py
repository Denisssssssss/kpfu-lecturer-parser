import requests
import collections
import pprint
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    html = r.text
    return BeautifulSoup(html, 'html.parser')


page = 0
prev_size = -1
flag = True
dictionary = collections.defaultdict()
while prev_size < len(dictionary):
    prev_size = len(dictionary)
    try:
        soup = get_html('https://kpfu.ru/main_page?p_sub=7860&p_id=10857&p_order=' + str(page))
        lecturers = soup.find_all('table')[0].find_all_next('span')
    except TypeError:
        continue
    page += 1

    for lecturer in lecturers:
        try:
            a = lecturer.a
            link = a['href']
            name = a.text
            dictionary[name] = link
        except TypeError:
            continue

for lecturer in dictionary.items():
    link = lecturer[1]
    lecturer_data = get_html(link)
    info = lecturer_data.find_all('li')[150].find_all_next('li')[0]
    articles = lecturer_data.find('div', {'class': 'right_width right_block'}).find('ul', {'class': 'menu_list_left'}).find('a', text='Статьи')
    try:
        articles_data = get_html(articles['href']).find('div', {'class': 'left_width'}).find_all('li', {'class': 'li_spec'})
    except TypeError:
        continue
    refs = list()
    for article in articles_data:
        try:
            ref = article.a
            refs.append(ref['href'])
        except TypeError:
            continue
    dictionary[lecturer[0]] = refs

pprint.pprint(dictionary)
