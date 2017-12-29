# -*- coding:utf-8 -*-
import sys

import requests
import urllib.parse

import dl

filename = 'tryshortvideo' # input
shortvideo = 'http://www.liveme.com/media/shortvideo/?videoid=347736292784247217481318422000' # input

def real_link_of_shortvideo(shortvideo):
    '''
    get real link from original shortvideo link.

    args:
        shortvideo: the link of shortvideo.

    returns:
        real_link: the real link, just 1 string.
    '''
    qstr = urllib.parse.urlparse(shortvideo).query
    videoid = urllib.parse.parse_qs(qstr)['videoid'][0]
    real_link = 'http://hg.ksmobile.net/' + videoid + 'x.mp4'
    return real_link

if __name__ == '__main__':
    if len(sys.argv) == 3:
        filename, shortvideo = sys.argv[1:]
        real_link = real_link_of_shortvideo(shortvideo)
        dl.downloader([real_link], filename + 'x.mp4')
    else:
        raise TypeError('Enter suitable arguments.')

