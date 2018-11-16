from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# app = from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = "mysql://root@localhost"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
db = SQLAlchemy(app)

class songsave(db.Model):
    __tablename__="Song"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    link=db.Column(db.String)


class admin(db.Model):
    pass

if __name__=="__main__":
    db.create_all()
    song1=songsave(
        id=1,
        name="动物世界",
        link="http://www/baidu.com"
    )
    db.session.add(song1)
    db.session.commit()

