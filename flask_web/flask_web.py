from flask import Flask,request,render_template,redirect,url_for
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        return redirect('search')
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search_item.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


class NameForm(Form):
    name=StringField("Search song")
    submit=SubmitField("Submit")

if __name__ == '__main__':
    app.run(debug=True)
