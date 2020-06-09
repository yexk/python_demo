#!/usr/bin/python3

import requests
import sys
import os
import errno
from bs4 import BeautifulSoup


def get_filename(url):
    filename = os.path.basename(url)
    return filename


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def download_img(dir, img_url):
    mkdir_p(dir)
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        open(dir+'/'+get_filename(img_url), 'wb').write(r.content)  # 将内容写入图片
        print("done")
    del r


if __name__ == "__main__":
    url = 'https://fei788.com/artdetail-12631.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    strhtml = requests.get(url, headers=headers)
    if strhtml.status_code == 200:
        soup = BeautifulSoup(strhtml.text, 'lxml')
        data = soup.select(
            "body > div:nth-child(7) > div > div.content center p img")

        for i in data:
            url = i.get('src')
            print(__name__, "获取的内容:", url)
            download_img("aa/sdsd", url)
            # print(__name__ ,"获取的内容:", i.img.get('src'))

    else:
        print(("other error : %d") % strhtml.status_code)
