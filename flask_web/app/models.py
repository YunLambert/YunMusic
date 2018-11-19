from datetime import datetime
from app import db


class songsave(db.Model):
    __tablename__ = "Song"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    link = db.Column(db.String)


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def check_pwd(self, pwd):
        return self.pwd == pwd

# if __name__=="__main__":
#     db.create_all()
#     song1=songsave(
#         id=1,
#         name="动物世界",
#         link="http://www/baidu.com"
#     )
#     db.session.add(song1)
#     db.session.commit()
