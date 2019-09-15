import re
import os
import requests


class kugou():
    def __init__(self):
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
        self.search_url = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery191034642999175022426_1489023388639&keyword={}&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1489023388641'
        self.hash_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}'

    def search(self,songname):
        #songname = "动物世界"
        res = requests.get(self.search_url.format(songname), headers=self.headers).text
        filehashs = re.findall('"FileHash":"(.*?)"', res)
        temp_names = re.findall('"SongName":"(.*?)"', res)
        download_names = []
        download_urls = []
        for filehash in filehashs:
            res = requests.get(self.hash_url.format(filehash))
            paly_url = re.findall('"play_url":"(.*?)"', res.text)[0]
            download_url = paly_url.replace("\\", "")
            download_names.append(temp_names[len(download_urls)])
            download_urls.append(download_url)

        for i in range(len(download_urls)):
            print(temp_names[i] + ":" + download_urls[i])

        return temp_names, download_urls


