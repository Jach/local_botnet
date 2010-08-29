#!/usr/bin/env python
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort
from contextlib import closing

from views.admin import admin
from views.client import client

from config import *

app = Flask(__name__)
app.config.from_object(__name__)
app.register_module(admin)
app.register_module(client)

def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

def init_db():
  with closing(connect_db()) as db:
    with app.open_resource('schema.sql') as f:
      db.cursor().executescript(f.read())
    db.commit()
    with open('config.py', 'a') as f:
      f.write('DB_HAS_LOADED = True\n')

if 'DB_HAS_LOADED' not in globals() or not DB_HAS_LOADED:
  print 'Loading initial database...'
  init_db()

@app.before_request
def before_request():
  g.db = connect_db()

@app.after_request
def after_request(response):
  g.db.close()
  return response

if __name__ == '__main__':
  app.run()
