#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

#装饰器
@app.route('/')
def index():
'''
    a = 3
    b = 'c'
    d = 4
    return 'hello world'+'123'
print __name__
'''
    return redirect(url_for('url'))
@app.route('/url')
def url():
    return render_template('url.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)

