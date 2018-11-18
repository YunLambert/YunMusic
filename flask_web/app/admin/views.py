# coding:utf8
from . import admin
from flask import render_template,redirect,url_for


@admin.route("/")
def index():
    return render_template("admin/index.html")

@admin.route("/login/")
def login():
    return render_template("admin/login.html")

@admin.route("/logout/")
def logout():
    return redirect(url_for("admin.login"))

@admin.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@admin.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

