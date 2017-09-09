#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

url = 'http://a.qidian.com/'

def get_page_index(url):
    try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        print('请求失败')
        return None

def main():
    print(get_page_index(url))