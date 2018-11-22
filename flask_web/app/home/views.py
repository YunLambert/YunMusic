# coding:utf8
from . import home
from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField
from ..platforms import kugou, qqmusic, netease


@home.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home/index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        NameSaved.name = name
        return redirect(url_for('home.search', name=name))
    return render_template('home/index.html')


@home.route('/search', methods=['GET'])
def search():
    songname = NameSaved.name
    print(songname)

    data1= []
    data2=[]
    name_qq, url_qq = qqmusic.qq().search(songname)
    for (i, j) in zip(name_qq, url_qq):
        data1.append(i)
        data2.append(j)

    name_wy, url_wy = netease.wangyiyun().get(songname)
    for (i, j) in zip(name_wy, url_wy):
        data1.append(i)
        data2.append(j)

    name_kg, url_kg = kugou.kugou().search(songname)
    for (i, j) in zip(name_kg, url_kg):
        data1.append(i)
        data2.append(j)

    return render_template('home/search_item.html', name=songname, data1=data1,data2=data2)
    # return u'the search is:%s' % name


@home.route('/contacts', methods=['GET'])
def contacts():
    return render_template('home/contacts.html')


class NameForm(Form):
    name = StringField("Search song")
    submit = SubmitField("Submit")


class NameSaved():
    name = ' '
