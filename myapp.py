#!/usr/bin/python3

import os
from flask import Flask, request, render_template
import json
import sqlite3
from datetime import datetime


app = Flask(__name__)
app.debug = True

appDir = os.path.dirname(os.path.realpath(__file__))


@app.route('/')
def html_hw():

  now = datetime.now()
  curTime = now.strftime("%H:%M:%S")

  name = 'Welt'
  if "name" in request.args:
    name =  request.args['name']

  html_str = '<h2>Hallo %s' %name
  html_str += ' is is %s ' %curTime

  return html_str, 200 

if __name__ == "__main__":
  app.run('0.0.0.0')
