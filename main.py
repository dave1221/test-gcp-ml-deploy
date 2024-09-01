#!/usr/bin/env python
# coding: utf-8
"""
Created on 2024/9/1 21:10
@author: Zhu Jiang
"""


from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("I am inside hello world")
    return "Hello, World! CDC 2024"

@app.route('/echo/<name>')
def echo(name):
    print(f"this was placed in the url: new-{name}")
    return jsonify({'new-name': name})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
