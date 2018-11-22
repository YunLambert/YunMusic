# coding:utf8
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import pymysql

from datetime import datetime
from app import db


# app=Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/YunMusic"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# db = SQLAlchemy(app)

class songsave(db.Model):
    __tablename__ = "song"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    link = db.Column(db.String(200))

    def __repr__(self):
        return "<Music Name %r>" % self.name


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        return self.pwd == pwd

# if __name__=="__main__":
# db.create_all()

# song1=songsave(
#     id=1,
#     name="动物世界",
#     link="http://www/baidu.com"
# )
#
# admin=Admin(
#     name="root",
#     pwd="root",
#     is_super=0,
# )
#
# db.session.add(admin)
# db.session.commit()
