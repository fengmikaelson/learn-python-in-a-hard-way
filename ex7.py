#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-11-07 11:04:27
# @Last Modified by:   anchen
# @Last Modified time: 2016-11-07 15:17:26
from bs4 import BeautifulSoup

def parse_html(html):
    soup=BeautifulSoup(html)

    movie_list_soup=soup.find('ol',attrs={'class':'grid_view'})

    movie_name_list=[]

    for movie_li in movie_list_soup.find_all('li'):
        detail=movie_li.find('div',attrs={'class':'hd'})
        movie_name=detail.find('span',attrs={'class':'title'}).getText()
        
        movie_name_list.append(movie_name)
    next_page=soup.find('span',attrs={'class':'netx'}).find('a')
    if next_page:
        return movie_name_list,DOWNLOAD_URL+next_page['href']
    return movie_name_list,None