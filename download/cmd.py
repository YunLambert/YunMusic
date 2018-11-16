from download import kugou, qqmusic
from download import progressbar_test


def cmd(options):
    for option in options:
        print('*' + option)
    print('-' * 81)
    choice = input('请输入平台号(1-%d):' % len(options))
    if choice == 'q' or choice == 'Q':
        print('Bye...')
        exit(-1)
    choice_range = [str(i) for i in range(1, len(options) + 1)]
    if choice not in choice_range:
        print('[Error]: 平台号输入错误，必须在(1-%d)之间...' % len(options))
        return

    songname=input('请输入歌曲名')
    if songname == 'q' or songname == 'Q':
        print('Bye...')
        exit(-1)

    # if choice=='1':
    #     try:
    #         kugou.kugou().
    #     except:
    #         print('Error:下载失败！')
    #         return False
    # elif choice=='2':
    #     try:
    #         qqmusic.qq().
    #     except:
    #         print("Error:下载失败！")
    #         return False


if __name__ == '__main__':
    print("*************YunMusic Cmd测试端***************")
    options = ["1.kugou","2.qqmusic"]
    while True:
        try:
            cmd(options)
        except KeyboardInterrupt:
            print('Goodbye!')
            exit(-1)
