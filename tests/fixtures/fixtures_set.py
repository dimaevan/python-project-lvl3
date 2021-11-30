domains = (
    ('http://www.yandex.ru', 'www.yandex.ru'),
    ('http://www.habr.com', 'www.habr.com'),
    ('http://www.google.com', 'www.google.com'),
    ('google.com', ''),
)

domains_not = (
    ('http://www.yandex.ru', 're.yandex.ru'),
    ('http://www.habr.com', 'h.habr.com'),
    ('http://www.google.com', 'google.com'),
    ('https://r.google.com', 'rw.google.com'),
)

subdomains = [
    'http://dima.ru',
    'http://go.dima.ru',
    'http://this.dima.ru/assert/icon.png'
]

src = [
    ['/assets/icon.png', 'http://www.dima.ru/', 'http://www.dima.ru/assets/icon.png'], # noqa
    ['/assets/icon.png', 'http://www.dima.ru', 'http://www.dima.ru/assets/icon.png'], # noqa
    ['assets/icon.png', 'http://www.dima.ru', 'http://www.dima.ru/assets/icon.png'], # noqa
    ['/icon.png', 'http://www.dima.ru/', 'http://www.dima.ru/icon.png'], # noqa
    ['http://www.dima.ru/asset/icon.png', 'http://www.dima.ru/', 'http://www.dima.ru/asset/icon.png'], # noqa
    ['http://www.dima.ru/asse/icon.png', 'http://www.dima.ru/', 'http://www.dima.ru/asse/icon.png'], # noqa
    ['http://www.dima.ru/ass/icon.png', 'http://www.dima.ru/', 'http://www.dima.ru/ass/icon.png'], # noqa
    ['http://ru.dimas.ru/assets/icon.png', 'http://www.dima.ru/', False], # noqa
]

renames = (
    ('ru.hexlet.io/courses', 'ru-hexlet-io-courses'),
    ('ru.hexlet.io/courses', 'ru-hexlet-io-courses'),
)
