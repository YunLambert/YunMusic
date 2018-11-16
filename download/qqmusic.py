import urllib
import re
import requests
import time
import os


# class qq():
#     def __init__(self):
#         self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'}
#         self.search_url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=34725291680541638&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}&g_tk=5381&jsonpCallback=MusicJsonCallback703296236531272&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
#         self.download_format_url = 'http://dl.stream.qqmusic.qq.com/{}.m4a?vkey={}&guid=8208467632&uin=0&fromtag=66'
#
#     def download(self,download_url,savepath):
#         if not os.path.exists(savepath):
#             os.mkdir(savepath)
#
#     def search(self,songname):
#         res = requests.get(self.search_url.format(songname), headers=self.headers).text
#         print(res)

class qq():
    def init(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        self.search_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=34725291680541638&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}&g_tk=5381&jsonpCallback=MusicJsonCallback703296236531272&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
        self.fcg_url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback9239412173137234&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback9239412173137234&uin=0&songmid={}&filename={}.m4a&guid=8208467632'
        self.download_format_url = 'http://dl.stream.qqmusic.qq.com/{}.m4a?vkey={}&guid=8208467632&uin=0&fromtag=66'
        self.listen_url = 'http://ws.stream.qqmusic.qq.com/C100{}.m4a?fromtag=0&guid=126548448'

    def search(self):
        songname = "动物世界"
        res = requests.get(self.search_url.format(songname), headers=self.headers).text
        media_mid_temp = re.findall('"media_mid":"(.*?)"', res)
        songmids = re.findall('"lyric_hilight":".*?","mid":"(.*?)","mv"', res)
        temp_names = re.findall('},"name":"(.*?)","newStatus"', res)
        media_mids = []
        for i in range(len(media_mid_temp)):
            media_mids.append('C400' + media_mid_temp[i])
        download_names = []
        download_urls = []
        for i in range(len(media_mids)):
            fcg_res = requests.get(self.fcg_url.format(songmids[i], media_mids[i]), headers=self.headers)
            vkey = re.findall('"vkey":"(.*?)"', fcg_res.text)[0]
            download_names.append(temp_names[i].replace("\\", "").replace("/", "").replace(" ", "").replace('.', ''))
            download_urls.append(self.download_format_url.format(media_mids[i], vkey))
        for i in range(len(songmids)):
            print(temp_names[i] + ":" + self.listen_url.format(songmids[i]))
