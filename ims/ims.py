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
        movie_name = ' '.join(query.split()[0:])
        return movie_name
    except Exception as e:
        print e
        exit()
    return query

def get_magnet_link(movie_name = 'harry potter'):

    URL = 'https://www.skytorrents.in/search/all/ed/1/?q='+movie_name.replace(' ', '+')

    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, 'html.parser')

    movie_page = soup.find_all("a")

    for each in movie_page:
        if 'magnet:' in each.get('href'):
            return each.get('href')

def main():
    test_system()
    movie = get_input()
    try:
        print ('Streaming Torrent')
        command = 'peerflix "'+get_magnet_link(movie)+'" --vlc'
        os.system(command)
    except Exception as e:
        print e
        exit()

if __name__ == '__main__':
    main()