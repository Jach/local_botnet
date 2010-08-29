from flask import Module
from flask import request, session, g, redirect, url_for, abort, render_template

admin = Module(__name__, url_prefix='')

@admin.route('/')
def index():
  return render_template('index.html',
                         swf=url_for('static', filename='AdminInterface'),
                         width='100%', height='100%',
                         title='Admin', version_major='6',
                         version_minor='0', version_revision='65')

@admin.route('/login/', methods=['POST'])
def login():
  pass

@admin.route('/logout/', methods=['POST'])
def logout():
  pass

