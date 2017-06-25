#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from flask import Flask

app = Flask(__name__)

#装饰器
@app.route('/')
def index():
    a = 3
    b = 'c'
    d = 4
    return 'hello world'+123
print __name__
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)

