# coding:utf8
from . import admin
from flask import render_template, redirect, url_for, flash, session, request
from app.admin.forms import LoginForm, MusicForm, AdminForm
from app.models import Admin, songsave
from functools import wraps
from app import db, app
from werkzeug.utils import secure_filename
import datetime
import os


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


# 修改文件名称
def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + fileinfo[-1]
    return filename


@admin.route("/")
@admin_login_req
def index():
    return render_template("admin/index.html")


@admin.route("/login/", methods=["GET", "POST"])
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


@admin.route("/music/add/", methods=["GET", "POST"])
@admin_login_req
def music_add():
    form = MusicForm()
    if form.validate_on_submit():
        data = form.data
        file_url = secure_filename(form.url.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"], "rw")
        url = change_filename(file_url)
        form.url.data.save(app.config["UP_DIR"] + url)
        music = songsave(
            name=data["title"],
            link=url
        )
        db.session.add(music)
        db.session.commit()
        flash("添加电影成功！", "OK")
        return redirect(url_for('admin.music_add'))
    return render_template("admin/music_add.html", form=form)


@admin.route("/music/list/<int:page>/", methods=["GET"])
@admin_login_req
def music_list(page=None):
    if page is None:
        page = 1
    page_data = songsave.query.order_by(songsave.id.desc()).paginate(page=page, per_page=10)
    return render_template("admin/music_list.html", page_data=page_data)


# 删除电影
@admin.route("/music/del/<int:id>/", methods=["GET"])
@admin_login_req
def music_del(id=None):
    music = songsave.query.get_or_404(int(id))
    db.session.delete(music)
    db.session.commit()
    flash("删除电影成功！", "OK")
    return redirect(url_for('admin.music_list', page=1))


@admin.route("/role/add/", methods=["GET", "POST"])
@admin_login_req
def role_add():
    form = AdminForm()
    if form.validate_on_submit():
        data = form.data
        admin0 = Admin(
            name=data["name"],
            pwd=data["pwd"],
            is_super=0
        )
        db.session.add(admin0)
        db.session.commit()
        flash("添加管理员成功！", "OK")
    return render_template("admin/role_add.html", form=form)


@admin.route("/role/list/<int:page>",methods=["GET"])
@admin_login_req
def role_list(page=None):
    if page is None:
        page=1
    page_data=Admin.query.order_by(Admin.addtime.desc()).paginate(page=page,per_page=10)
    return render_template("admin/role_list.html",page_data=page_data)
