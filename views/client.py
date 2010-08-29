from flask import Module

client = Module(__name__, url_prefix='')

@client.route('/receive_commands/<ip>/')
def receive_commands(ip):
  pass
