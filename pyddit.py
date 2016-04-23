import requests
import lxml.html
import sys
import time
from threading import Thread

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None

    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)

    def join(self):
        Thread.join(self)
        return self._return

class Request:

    def __init__(self):
        self.url = ''
        self.user_agent = {'user-agent': 'Mozilla/5.0 \
                            (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0)'}

    def request(self):
        r = requests.get(self.url, headers=self.user_agent)

        return r.text

def titleParse():
    tree = lxml.html.fromstring(r.request())
    titles = tree.xpath('//*/div[2]/p[1]/a/text()')

    return titles

def urlParse():
    tree = lxml.html.fromstring(r.request())
    urls = tree.xpath('//*/div[2]/p[1]/a/@href')

    print urls

def upVotes():
    tree = lxml.html.fromstring(r.request())
    votes = tree.xpath('//*/div[1]/div[3]/text()')

    print votes

if __name__ == '__main__':
    r = Request()
    r.url = 'https://www.reddit.com/r/all'
    t1 = ThreadWithReturnValue(target = titleParse); t2 = ThreadWithReturnValue(target=urlParse); t3 = ThreadWithReturnValue(target=upVotes)

    t1.start(); t2.start(); t3.start(); t2.join(); t3.join()

    for url in t1.join():
        print url
