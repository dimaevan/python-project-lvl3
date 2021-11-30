from bs4 import BeautifulSoup
from page_loader.searcher import search_for_tag

with open('tests/fixtures/simple.html') as file:
    res = file.read()
    soup = BeautifulSoup(res, 'html.parser')

with open('tests/fixtures/simple_edit.html') as file:
    res2 = file.read()
    soup_edit = BeautifulSoup(res2, 'html.parser')


def test_searcher():
    search_for_tag(soup, 'http://www.dima.com', 'www-dima-com_files/', 'img')
    assert soup == soup_edit
