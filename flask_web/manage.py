from app import app
from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField



# app = Flask(__name__)
# app.config["SECRET_KEY"] = "12345678"

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
