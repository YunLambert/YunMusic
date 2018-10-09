import re
import os
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
search_url = 'http://songsearch.kugou.com/song_search_v2?keyword={}&page=1&pagesize=30'
hash_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}'
songname="动物世界"
res = requests.get(search_url.format(songname), headers=headers).text
filehashs = re.findall('"FileHash":"(.*?)"', res)
temp_names = re.findall('"SongName":"(.*?)"', res)
download_names = []
download_urls = []
for filehash in filehashs:
    res = requests.get(hash_url.format(filehash))
    paly_url = re.findall('"play_url":"(.*?)"', res.text)[0]
    download_url = paly_url.replace("\\", "")
    download_names.append(temp_names[len(download_urls)])
    download_urls.append(download_url)

for i in range(len(download_urls)):
    print(temp_names[i]+":"+download_urls[i])




