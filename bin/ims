#!/usr/bin/env python

import os
import sys

import requests
from bs4 import BeautifulSoup

DEBUG = False


def test_system():
    """Runs few tests to check if npm and peerflix is installed on the system."""
    if os.system('npm --version') != 0:
        print 'NPM not installed installed, please read the Readme file for more information.'
        exit()
    if os.system('peerflix --version') != 0:
        print 'Peerflix not installed, installing..'
        os.system('npm install -g peerflix')


def get_input():
    """Gets the input from user and formats it."""
    try:
        query = ' '.join(sys.argv[1:])
        cat = query.split()[0]
        movie_name = ' '.join(query.split()[1:])
        if cat == 'movie':
            query = (movie_name + ' category:movies').replace(' ', '%20')
        elif cat == 'tv':
            query = (movie_name + ' category:tv').replace(' ', '%20')
        else:
            print 'Invalid format, please specify if its a movie or tv series.'
            exit()
    except Exception as e:
        print e
        exit()
    return query


def get_torrent_url(search_url):
    """Grabs the best matched torrent URL from the search results."""
    search_request_response = requests.get(search_url, verify=False)
    soup = BeautifulSoup(search_request_response.text, 'html.parser')
    movie_page = 'https://kat.cr' + (soup.find_all("a", class_="cellMainLink")[0].get('href'))

    search_url = requests.get(movie_page, verify=False)
    soup = BeautifulSoup(search_url.text, 'html.parser')
    torrent_url = 'https:' + soup.find_all('a', class_='siteButton')[0].get('href')
    return torrent_url


test_system()
movie = get_input()
url = 'https://kat.cr/usearch/' + movie
if DEBUG:
    print url
torrent_url = ''
try:
    print 'Searching....'
    torrent_url = get_torrent_url(url)
except Exception as e:
    print e
    exit()
if torrent_url:
    print ('Streaming Torrent: ' + torrent_url)
    os.system('peerflix ' + torrent_url + ' -a --vlc')
else:
    print 'No results found'
