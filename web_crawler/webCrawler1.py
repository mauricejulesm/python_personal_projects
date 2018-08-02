
import requests
from bs4 import BeautifulSoup


def panda_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.boredpanda.com/people-who-dont-give-a-duck/?page_numb=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text   # everything we crawl will be stored in this variable plain text

        soup = BeautifulSoup(plain_text)    # store the info here in soup variable
        for link in soup.findAll('a', {'class': 'open-list-header'}):
            href = link.get('href')
            print(href)
        page += 1
panda_spider(1)







