# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, ValidationError,EqualTo
from app.models import Admin


class LoginForm(FlaskForm):
    # 管理院登陆表单
    account = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号!",
            "required": "required"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": "required"
        }
    )
    submit = SubmitField(
        '登陆',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )


def validate_account(self, field):
    account = field.data
    admin = Admin.query.filter_by(name=account).count()
    if admin == 0:
        raise ValidationError("账号不存在!")


class MusicForm(FlaskForm):
    title = StringField(
        label="歌名",
        validators=[
            DataRequired("请输入歌名!")
        ],
        description="歌名",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入歌名！"
        }
    )
    url = FileField(
        label="文件",
        validators=[
            DataRequired("请上传文件!")
        ],
        description="文件",
    )
    submit = SubmitField(
        '上传',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )


class AdminForm(FlaskForm):
    name=StringField(
        label="管理员名称",
        validators=[
            DataRequired("请输入管理员名称！")
        ],
        description="管理员名称",
        render_kw={
            "class":"form-control",
            "placeholder":"请输入管理员名称!"
        }
    )
    pwd=PasswordField(
        label="管理员密码",
        validators=[
            DataRequired("请输入管理员密码！")
        ],
        description="管理员密码",
        render_kw={
            "class":"form-control",
            "placeholder":"请输入管理员密码！",
        }
    )

    repwd = PasswordField(
        label="管理员重复密码",
        validators=[
            DataRequired("请重复输入密码！"),
            EqualTo('pwd',message="两次密码不一致！")
        ],
        description="管理员重复密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请重复输入密码！",
        }
    )

    submit = SubmitField(
        '添加',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )
