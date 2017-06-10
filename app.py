#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flask AJAX call example

2017
Xaratustrah
"""
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import subprocess

app = Flask(__name__)
Bootstrap(app)


def run_cmd(cmd_string):
    try:
        p = subprocess.Popen(cmd_string.split(),
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ok = p.wait()
        out, err = p.communicate()
    except FileNotFoundError:
        out = b''
        err = b''
        ok = True

    return ok, out, err


@app.route('/_get_date', methods=['GET', 'POST'])
def _get_date():
    ok, out, err = run_cmd('date')
    return jsonify(result=out.decode('utf-8'))


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('view.html')


if __name__ == '__main__':
    app.run()
