from urllib.parse import urlparse, urljoin
from progress.bar import Bar
import requests
import logging
import re


def rename(word):
    """ Удаляет ненужные символы из URL """
    return re.sub(r'\W', '-', word)


def netloc(word):
    """ Fetch domain name from URL """
    url = urlparse(word).netloc
    return url


def check_src(src, url):
    """ Validate src and return full url """
    if src == url:
        return False
    elif netloc(src) == '':
        return urljoin(url, src)
    elif netloc(src) == netloc(url):
        return src
    else:
        return False


def find_extension(word):
    try:
        ext = re.findall(r'\.\w*$', str(word))
        if ext:
            return ext[0]
        return False
    except TypeError:
        return False


def download_file(links, type_of_file=None):
    count = 0
    bar = Bar(f'Downloading {type_of_file}', max=len(links))
    for link, name in links:
        file = get_from_url(link)
        if file:
            save_file(file.content, name)
            count += 1
        bar.next()
    bar.finish()
    return count


def get_from_url(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.142 Safari/537.36 '
    }
    try:
        obj = requests.get(link, headers=headers)
        if not str(obj.status_code).startswith('4'):
            return obj
    except requests.RequestException:
        logging.error(f'Сan`t download {link} ')


def save_file(obj, name):
    if obj:
        try:
            with open(name, 'wb') as file:
                file.write(obj)
        except IOError:
            logging.error(f'Can`t save file {name}')


def beauty_path(path):
    word = str(path)
    if word.endswith('/'):
        return word[:-1]
    return word
