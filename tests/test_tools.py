from page_loader.tools import rename
from page_loader.tools import netloc
from page_loader.tools import check_src
from page_loader.tools import find_extension
from page_loader.tools import get_from_url
from tests.fixtures.fixtures_set import domains, src, domains_not, renames
import requests_mock


def test_rename():
    for _ in renames:
        assert rename(_[0]) == _[1]


def test_fetch_domain():
    for x, y in domains:
        assert netloc(x) == y


def test_fetch_domain_negative():
    for x, y in domains_not:
        assert netloc(x) != y


def test_check_src():
    for el in src:
        assert check_src(el[0], el[1]) == el[2]


def test_find_ext():
    word = 'https://site.com/blog/about'
    assert find_extension(word) is False


def test_get_from_url():
    with requests_mock.Mocker() as m:
        m.get('', text='Test')
        assert get_from_url('http://localhost') is not None
        assert get_from_url('http://localhost').text == 'Test'

    with requests_mock.Mocker() as m:
        m.get('', status_code=300, text='Test')
        assert get_from_url('http://localhost').text == 'Test'


def test_get_from_url_negative():
    with requests_mock.Mocker() as m:
        m.get('', status_code=400, text='Test')
        assert get_from_url('http://localhost') is None
