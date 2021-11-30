from page_loader.tools import rename, check_src, find_extension
from urllib.parse import urlparse


def search_for_tag(html, url, folder, tag):
    """Search chosen tag in html page. Return list"""
    attribute = {'img': 'src', 'link': 'href', 'script': 'src'}[tag]
    result = []
    domain = urlparse(url).netloc
    links = html.find_all(tag)
    filtered = list(filter(lambda c: c.get(attribute), links))

    for link in filtered:
        src = link[attribute]
        if not check_src(src, url):
            continue
        # Full url 4 download
        full_url = check_src(src, url)
        path_url = str(urlparse(full_url).path)
        name_src = urlparse(full_url).netloc + urlparse(full_url).path
        ext = find_extension(name_src)

        if not ext:
            file_name = rename(domain) + rename(path_url) + '.html'
        else:
            path = name_src.replace(ext, '')
            file_name = rename(path) + ext

        link[attribute] = folder + file_name
        result.append((full_url, file_name))

    return result
