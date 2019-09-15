# coding:utf8
from . import home
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from flask_wtf import Form
from wtforms import StringField, SubmitField
from ..platforms import kugou, qqmusic, netease, getVideo
from flask.signals import _signals
from app import app
import logging
import re
import os
import threading

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
DOWNLOAD_FILE = "./Files_temp/"


@home.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home/index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        NameSaved.name = name

        # Add 判断name是歌曲名还是url，如果是url则会引导至视频下载页面
        if re.match(r'^https?:/{2}\w.+$', name):
            print("Video Search...")
            return redirect(url_for('home.searchv2', name=name))
        print("Audio Search...")
        return redirect(url_for('home.search', name=name))
    # return render_template('home/index.html')


@home.route('/searchv2', methods=['GET'])
def searchv2():
    url = NameSaved.name
    print(url)

    file = getVideo.you_get_download(url, DOWNLOAD_FILE)
    print("over")
    dirPath = os.path.join(app.root_path, 'Files_temp')
    files = os.listdir(dirPath)
    data = []
    try:
        for i in range(len(files)):
            temp = {
                "id": i + 1,
                "name": files[i],
                "url": "/downloadfile/?filename="+app.root_path+"Files_temp/"+files[i],
            }
            data.append(temp)
    except Exception as e:
        logging.error("Download File error: ----->next")
        logging.error(e)
    return render_template('home/searchv2_item.html', data=data)


@home.route('/search', methods=['GET'])
def search():
    songname = NameSaved.name
    print(songname)
    print("开始下载......")
    data1 = []
    data2 = []

    try:
        name_qq, url_qq = qqmusic.qq().search(songname)
        for (i, j) in zip(name_qq, url_qq):
            data1.append(i)
            data2.append(j)
    except Exception as e:
        logging.info("QQ Music Download error: ----->next")
        logging.error(e)
        print("Error on QQ Music")

    try:
        name_wy, url_wy = netease.wangyiyun().get(songname)
        for (i, j) in zip(name_wy, url_wy):
            data1.append(i)
            data2.append(j)
    except Exception as e:
        logging.info("Netease Download error: ----->next")
        logging.error(e)
        print("Error on NetEase")

    try:
        name_kg, url_kg = kugou.kugou().search(songname)
        for (i, j) in zip(name_kg, url_kg):
            data1.append(i)
            data2.append(j)
    except Exception as e:
        logging.info("kugou Download error: ----->next")
        logging.error(e)
        print("Error on kugou")

    data = []
    for i in range(len(data1)):
        temp = {
            "id": i + 1,
            "name": data1[i],
            "url": data2[i]
        }
        data.append(temp)

    return render_template('home/search_item.html', name=songname, data=data)
    # return u'the search is:%s' % name


@home.route('/contacts', methods=['GET'])
def contacts():
    return render_template('home/contacts.html')


class NameForm(Form):
    name = StringField("Search song")
    submit = SubmitField("Submit")


class NameSaved():
    name = ' '


@app.route('/downloadfile/<path:filename>', methods=['GET', 'POST'])
def downloadfile(filename):
    dirpath = os.path.join(app.root_path, 'Files_temp')
    return send_from_directory(dirpath, filename, as_attachment=True)
