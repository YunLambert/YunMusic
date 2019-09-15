import sys
import you_get
import time

def you_get_download(url, path):
    print("outputting you-get....")
    print(url)
    print(path)
    file_name = time.strftime("%Y%m%d-%H%M%S") + ".mp4"
    print(file_name)
    sys.argv = ['you-get', '-o', path, '-O', file_name, url]
    you_get.main()

    return file_name