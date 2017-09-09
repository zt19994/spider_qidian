#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import pprint


def get_page(url):
    try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        if res.status_code == 200:
            return res.text
    except RequestException:
        print('请求失败')
        return None


def parser_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    books = []
    for i in range(20):
        book = {}
        book['title'] = soup.select(' h4 a')[i].text
        book['author'] = soup.select('a.name ')[2:][i].text
        book['type'] = soup.select('a.go-sub-type ')[i].text
        book['words'] = soup.select('.update span')[i].text.rstrip('万字')
        books.append(book)
    return books

def get_next_page(page_number):
    url = 'http://a.qidian.com?orderId=&style=1&pageSize=20&siteid=1&hiddenField=0&page={}'.format(page_number)
    return url



def main():
    for i in range(20):
        url = get_next_page(i)
        html = get_page(url)
        pprint.pprint(parser_page(html))


if __name__ == '__main__':
    main()