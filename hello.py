# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
	user_agent = request.headers.get('User-Agent')
	return "<p>Your browser is %s</p>" % user_agent

if __name__ == '__main__':
	manager.run()
