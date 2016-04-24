import requests
import lxml.html
import sys
import time
from multiprocessing.dummy import Pool as ThreadPool

class Request:

    pool = ThreadPool(4)
    xpaths = ['//*/div[2]/p[1]/a/text()', '//*/div[2]/p[1]/a/@href',\
    '//*/div[1]/div[3]/text()']

    def __init__(self):
        self.url = ''
        self.user_agent = {'user-agent': 'Mozilla/5.0 \
                            (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0)'}

    def request(self):
        r = requests.get(self.url, headers=self.user_agent)

        return r.text

    def titleParse(self):
        tree = lxml.html.fromstring(self.request())

        results = self.pool.map(tree.xpath, self.xpaths)
        for title, url, votes in zip(results[0], results[1], results[2]):
            print votes + " " + title + " " + "\n" + url
        self.pool.close()
        self.pool.join()

if __name__ == '__main__':
    r = Request()
    r.url = 'https://www.reddit.com/r/all'
    r.titleParse()
