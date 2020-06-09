#!/usr/bin/python3

import requests
import redis
import time
from bs4 import BeautifulSoup


class GetBaidu:
    def __init__(self):
        self.redisdb = redis.Redis(host='redis', port=6379, db=0)

    def getTopContents(self,key):
        urls = 'https://www.baidu.com'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        strhtml = requests.get(urls, headers=headers)
        if strhtml.status_code == 200:
            soup = BeautifulSoup(strhtml.text, 'lxml')
            data = soup.select(
                "#hotsearch-content-wrapper > li > a > span.title-content-title")
        for i in data:
            t = i.contents[0]
            self.redisdb.lpush(rediskey, t)
            # print(__name__ ,"获取的内容:", t)

    def getTopLists(self, key):
        return self.redisdb.lrange(key, 0, -1)

if __name__ == "__main__":
    times = str(time.strftime("%y%d%m%H%M%S"))
    rediskey = 'top:'+times
    baidu = GetBaidu()
    baidu.getTopContents(rediskey) # 获取百度的top值
    lists = baidu.getTopLists(rediskey) # 获取redis的缓存
    for i in lists:
        print(i.decode('utf-8'))
