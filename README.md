# YunMusic
集网易云音乐、QQ音乐以及多个音乐平台的在线一站式检索网站，如果所有平台都没有想搜索的歌曲的话，可以自己上传至服务器或者由管理员定期维护相应的歌曲。
<div style="float:left;border:solid 1px 000;margin:2px;"><img src="https://upload-images.jianshu.io/upload_images/7154520-6c533e2a89c7a23a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"  width="100" height="100" ></div>
<div style="float:left;border:solid 1px 000;margin:2px;"><img src="https://upload-images.jianshu.io/upload_images/7154520-b981ddcec494a6b8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="100" height="100" ></div>
<div style="float:left;border:solid 1px 000;margin:2px;"><img src="https://upload-images.jianshu.io/upload_images/7154520-5ff2df328498aae1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" width="100" height="100" ></div>

## UPDATE: 20190915 #Add video download
1.修复了一些api失效问题，并增加了异常处理
2.增加了视频下载功能，在搜索框直接输入想要下载的链接即可完成下载

### TODO
- [ ] 更改文件存储模式，以减小文件存储体积
- [ ] 重构前端的界面
- [ ] 完善后台管理员界面的功能，实现能够后台上传并在前端下载的功能
- [ ] 开辟多线程与锁机制，增快下载速度

## Cmd端   -------**Done!**

细节问题之后会细化，包括加入直接下载的功能，还有显示下载进度条的美化工作。

![TIM截图20181117215337.png](https://upload-images.jianshu.io/upload_images/7154520-c8f48ee00bc561b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![TIM截图20181117215930.png](https://upload-images.jianshu.io/upload_images/7154520-521a82011aa763f9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![TIM截图20181117215514.png](https://upload-images.jianshu.io/upload_images/7154520-96d467691067730a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## Web端 -----Done!

包括前台和后台两个部分，用户在前台可以通过搜索歌曲名称找到已提供的音乐平台上的歌曲链接(可在线听并下载)，所有这样的链接都会显示在网站列表中；点击"上传资源"则会跳至后台服务，此处需要管理员账号和密码才能登陆，上传的资源记录会保存到数据库中，并在相应的地方进行显示。

主要功能已经完成，后期如果需要修改的话，会放在扩展音乐平台资源与将后台上传的资源同样通过链接形式显示在前台服务中，再有就是一些细节上的优化。

![20181123092733.png](https://upload-images.jianshu.io/upload_images/7154520-527df50a81f56458.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123092758.png](https://upload-images.jianshu.io/upload_images/7154520-8eca1fb557a6214b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![20181123092822.png](https://upload-images.jianshu.io/upload_images/7154520-4ca8e281641498f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123092844.png](https://upload-images.jianshu.io/upload_images/7154520-a4c50318cb396871.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123092910.png](https://upload-images.jianshu.io/upload_images/7154520-0696a84d730aa0af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123092932.png](https://upload-images.jianshu.io/upload_images/7154520-e69f2cd2cead09a0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123093000.png](https://upload-images.jianshu.io/upload_images/7154520-12c74671aaadce57.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123093024.png](https://upload-images.jianshu.io/upload_images/7154520-ccdf6bd95edef38d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123093105.png](https://upload-images.jianshu.io/upload_images/7154520-863ebbfae7295fb3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123093117.png](https://upload-images.jianshu.io/upload_images/7154520-69bfe63e84aaa027.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123093129.png](https://upload-images.jianshu.io/upload_images/7154520-fb163b94351fb1e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123093208.png](https://upload-images.jianshu.io/upload_images/7154520-229a64bddfa0b978.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123093218.png](https://upload-images.jianshu.io/upload_images/7154520-cff89a37d13fcdeb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181123093248.png](https://upload-images.jianshu.io/upload_images/7154520-25430af9c3f2fe15.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![20181122134903.png](https://upload-images.jianshu.io/upload_images/7154520-d63c2b19077fdd04.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![404.png](https://upload-images.jianshu.io/upload_images/7154520-784829e13d711cb6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 主要功能介绍

利用爬虫对音乐平台上的歌曲进行爬取，将链接展现出来。

Web端是用python+flask进行完成。

Cmd端是普通的命令交互式界面。
