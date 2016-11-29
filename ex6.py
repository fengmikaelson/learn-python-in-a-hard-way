#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-11-03 14:24:12
# @Last Modified by:   anchen
# @Last Modified time: 2016-11-07 11:00:50
import requests

DOWNLOAD_URL='http://movie.douban.com/top250'

def download_page(url):
    data=requests.get(url).content
    return data

def main():
    print (download_page(DOWNLOAD_URL))

if __name__=="__main__":
    main()