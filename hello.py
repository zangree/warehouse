# -*- coding:utf-8 -*-

from flask import Flask, render_template
from flask import request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = "jajgaijgakg;1894412!!!"
manager = Manager(app)
bootstrap = Bootstrap(app)

class NameFrom(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route("/", methods=["GET", "POST"])
def index():
     name = None
     form = NameFrom()
     if form.validate_on_submit():
         name = form.name.data
         form.name.data = ''
     return render_template("index.html", form=form, name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    manager.run()
