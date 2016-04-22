import requests
import lxml.html
import sys
import time

class Request:

    def __init__(self):
        self.url = ''
        self.user_agent = {'user-agent': 'Mozilla/5.0 \
                            (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0)'}

    def request(self):
        r = requests.get(self.url, headers=self.user_agent)

        return r.text

    def titleParse(self):
        tree = lxml.html.fromstring(self.request())
        titles = tree.xpath('//*/div[2]/p[1]/a/text()')

        return titles

    def urlParse(self):
        tree = lxml.html.fromstring(self.request())
        urls = tree.xpath('//*/div[2]/p[1]/a/@href')

        return urls

    def upVotes(self):
        tree = lxml.html.fromstring(self.request())
        votes = tree.xpath('//*/div[1]/div[3]/text()')

        return votes

r = Request()
r.url = 'https://www.reddit.com/r/all'
print r.titleParse()
t1 = Thread(target = r.titleParse); t2 = Thread(target=r.urlParse); t3 = Thread(target=r.upVotes)

t1.start(); t2.start(); t3.start(); t1.join(); t2.join(); t3.join()
#r.titleParse(); r.urlParse(); r.upVotes()
#for title, url, votes in zip(t1.start(), t2.start(), t3.start()):
#    print votes + " " + title + "\n" + url
