# !/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from bs4 import BeautifulSoup
    import mechanize
except ImportError:
    no_third_libraries = True


WIKI_PAGE = 'http://es.wikipedia.org/Zamora'


def crawler(url, limit=5):
    import re
    import urllib
    count = 0
    end = False
    regex = re.compile(r'<p(.+)')
    while count < 3 and not end:
        try:
            page = urllib.urlopen(url).read()
        except Exception:
            count += 1
        else:
            end = True
            hits = regex.findall(page)
            for hit in hits[:limit]:
                yield hit
    raise StopIteration


def get_browser():
    return mechanize.Browser()


def get_paragraph(browser):
    try:
        page = browser.open(WIKI_PAGE)
    except Exception:
        return None

    soup = BeautifulSoup(page, 'html.parser') # No aparezca el aviso
    elements = soup(attrs={
        'id': 'mw-content-text'
    })
    return unicode(elements[0].findAll('p', limit=1)[0])


def main():
    if not no_third_libraries:
        br = get_browser()
        paragraph = get_paragraph(br)
        print paragraph if paragraph else 'Ha habido un error'

    craws = crawler(WIKI_PAGE, 1)
    for c in craws:
        p = '<p' + c
        print p
    else:
        raise Exception('Ha habido un error')


if __name__ == '__main__':
    main()
