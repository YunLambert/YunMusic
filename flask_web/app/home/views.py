# coding:utf8
from . import home
from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField


@home.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home/index.html')
    if request.method == 'POST':
        name=request.form.get('name')
        NameSaved.name=name
        return redirect(url_for('home.search',name=name))
    return render_template('home/index.html')


@home.route('/search', methods=['GET'])
def search():
    name=NameSaved.name
    print(name)
    return render_template('home/search_item.html',name=name)
    #return u'the search is:%s' % name

@home.errorhandler(404)
def page_not_found(e):
    return render_template('home/404.html'), 404


@home.errorhandler(500)
def internal_server_error(e):
    return render_template('home/500.html'), 500

@home.route('/contacts', methods=['GET'])
def contacts():
    return render_template('home/contacts.html')

class NameForm(Form):
    name = StringField("Search song")
    submit = SubmitField("Submit")

class NameSaved():
    name='hell0'
