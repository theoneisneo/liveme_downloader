# -*- coding:utf-8 -*-
import sys
import json

import requests
import urllib.parse

import dl

# filename = 'ff039' # input
# userid = '927842472174813184' # input
# replay = 'https://www.liveme.com/live.html?videoid=15134898379897522543' # input

def real_links_of_replay(userid, replay, page_size=50, page_index=0):
    '''

    args:
        userid: userid of the replay owner. find yourself.
        replay: replay link.
        page_size: int, min = 1.
        page_index: int, min = 0.

    returns:
        urllist: the ts file links from m3u8 file.

    '''

    qstr = urllib.parse.urlparse(replay).query
    videoid = urllib.parse.parse_qs(qstr)['videoid'][0]

    replay_data_by_userid = 'http://live.ksmobile.net/live/getreplayvideos?userid=' + userid + '&page_size=' + str(page_size) + '&page_index=' + str(page_index)

    res1 = requests.get(replay_data_by_userid)
    replay_data = json.loads(res1.text)

    for i in range(len(replay_data['data']['video_info'])):
        if replay_data['data']['video_info'][i]['vid'] == videoid:
        # if replay_data['data']['video_info'][0]['vdoid'] == videoid: # store same value
            playlist = replay_data['data']['video_info'][i]['videosource']
            # playlist = replay_data['data']['video_info'][i]['hlsvideosource'] # store same value
            break

    # parse m3u8 playlist file to get video files(.ts)
    res2 = requests.get(playlist)
    res3 = res2.text.split('\n')

    real_links = []
    end = playlist.rfind('/')
    for s in res3:
        if not s.startswith('#') and len(s) != 0:
            real_links.append(playlist[:end + 1] + s)
    return real_links

if __name__ == '__main__':
    if len(sys.argv) == 4:
        filename, userid, replay = sys.argv[1:]
        real_links = real_links_of_replay(userid, replay)
        dl.downloader(real_links, filename + '.ts')
    else:
        raise TypeError('Enter suitable arguments.')
    