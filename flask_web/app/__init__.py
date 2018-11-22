# coding:utf8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/YunMusic"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']="12345678"
app.debug = True
db = SQLAlchemy(app)



from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('home/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('home/500.html'), 500