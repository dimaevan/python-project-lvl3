from page_loader.downloader import download
import requests_mock
import tempfile


def test_mock():
    temp = tempfile.TemporaryDirectory()
    name_td = temp.name

    with requests_mock.Mocker() as m:
        m.get('', text='data')
        sample = download('http://test.com', name_td)
        path = name_td + "/test-com.html"
        assert sample == path

        with open(sample, 'r') as file:
            content = file.read()
        assert content == 'data\n'


def test_no_dir():
    assert download('', 'dima/') is None


def test_status_code(tmp_path):
    with requests_mock.Mocker() as m:
        m.get('', status_code=400)
        assert download('http://123.ru', tmp_path) is None
