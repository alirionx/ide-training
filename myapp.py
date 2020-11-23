#!/usr/bin/python3

import os
from flask import Flask, request, render_template
import json
import sqlite3


app = Flask(__name__)
app.debug = True

appDir = os.path.dirname(os.path.realpath(__file__))


@app.route('/hallowelt')
def html_hw():

  name = 'Welt'
  if "name" in request.args:
    name =  request.args['name']

  html_str = '<h2>Hallo %s</h2>' %name

  return html_str, 200 

if __name__ == "__main__":
  app.run('0.0.0.0')
