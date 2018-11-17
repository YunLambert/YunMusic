#coding:utf8
from . import home

@home.route("/")
def index():
    return "templates/home/index.html"