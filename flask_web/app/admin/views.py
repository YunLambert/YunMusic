# coding:utf8
from . import admin
from flask import render_template, redirect, url_for, flash, session, request
from app.admin.forms import LoginForm
from app.models import Admin
from functools import wraps

def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login",next=request.url))
        return f(*args,**kwargs)
    return decorated_function


@admin.route("/")
@admin_login_req
def index():
    return render_template("admin/index.html")


@admin.route("/login/", methods=["GET", "POST"])
@admin_login_req
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误！")
            return redirect(url_for("admin.login"))
        session["admin"] = data["account"]
        return redirect(request.args.get("next") or url_for(admin.index))
    return render_template("admin/login.html", form=form)


@admin.route("/logout/")
@admin_login_req
def logout():
    session.pop("admin", None)
    return redirect(url_for("admin.login"))


@admin.route("/pwd/")
@admin_login_req
def pwd():
    return render_template("admin/pwd.html")


@admin.route("/music/add/")
@admin_login_req
def music_add():
    return render_template("admin/music_add.html")


@admin.route("/music/list/")
@admin_login_req
def music_list():
    return render_template("admin/music_list.html")


@admin.route("/role/add/")
@admin_login_req
def role_add():
    return render_template("admin/role_add.html")


@admin.route("/role/list/")
@admin_login_req
def role_list():
    return render_template("admin/role_list.html")
