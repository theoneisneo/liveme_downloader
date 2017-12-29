# -*- coding:utf-8 -*-
import sys

import requests

def downloader(urllist, filename):
    '''
    download files and cominbe to one file.

    args:
        urllist: type should be list.
        filename: the name want to save as.
    
    returns:
        none.

    '''
    f = open(filename, 'wb')
    l = len(urllist)
    i = 1
    print('Downloading')
    for link in urllist:
        r = requests.get(link, stream=True)
        print(str(i) + '/' + str(l))
        i += 1
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    f.close()