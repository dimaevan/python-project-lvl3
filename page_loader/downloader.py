#!usr/bin/env python3
from page_loader.searcher import search_for_tag
from page_loader.tools import get_from_url, beauty_path
from page_loader.tools import rename, download_file
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import logging
import os


def download(link, path=os.getcwd()):
    """ Download html-page from url """
    if not os.path.isdir(path):
        logging.error('Directory is not exist')
        return
    full_path = os.path.abspath(path)
    os.chdir(full_path)

    html = get_from_url(link)
    if not html:
        return

    domain = urlparse(link).netloc
    url_path = urlparse(link).path
    clean_url = (domain + beauty_path(url_path))

    name_html = rename(clean_url) + '.html'
    name_folder = rename(clean_url) + '_files/'

    soup = BeautifulSoup(html.text, 'html.parser')
    # Create dir 4 downloads
    try:
        os.mkdir(name_folder)
    except FileExistsError:
        pass

    os.chdir(name_folder)
    # Load files
    for _ in ('img', 'script', 'link'):
        resources = search_for_tag(soup, link, name_folder, _)
        x = download_file(resources, _)
        print(f'Download {x} {_}')

    os.chdir(full_path)
    with open(name_html, 'w') as file:
        file.write(str(soup.prettify()))
    return os.path.abspath(name_html)


if __name__ == "__main__":
    print(download('https://www.portent.com/tools/title-maker/'))
