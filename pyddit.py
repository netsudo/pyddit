import requests
import lxml.html
import sys
import time
from threading import Thread
from itertools import *
from multiprocessing import Process, Queue

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

def titleParse(url, que1):
    tree = lxml.html.fromstring(r.request())
    titles = tree.xpath('//*/div[2]/p[1]/a/text()')

    return titles

def urlParse(url, que2):
    tree = lxml.html.fromstring(r.request())
    urls = tree.xpath('//*/div[2]/p[1]/a/@href')

    return urls

def upVotes(url, que3):
    tree = lxml.html.fromstring(r.request())
    votes = tree.xpath('//*/div[1]/div[3]/text()')

    return votes

if __name__ == '__main__':
    r = Request()
    r.url = 'https://www.reddit.com/r/all'
    url = r.request()
    queue1=Queue(); queue2=Queue(); queue3=Queue()
    p1 = Process(target = titleParse, args=(url,queue1,)); p2= Process(target=urlParse, args=(url, queue2)); p3 = Process(target=upVotes, args=(url,queue3,))
    p1.start(); p2.start(); p3.start()

    #t1.start(); t2.start(); t3.start();t1.join();t2.join();t3.join()

    for title, url, votes in izip(queue1.get(), queue2.get(), queue3.get()):
        print votes + " " + title + " " + "\n" + url
        p1.join(); p2.join(); p3.join()
