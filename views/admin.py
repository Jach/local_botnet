from flask import Module, jsonify
from flask import request, session, g, redirect, url_for, abort, render_template

admin = Module(__name__, url_prefix='')

# Admin specific functions
@admin.route('/')
def index():
  return render_template('index.html',
                         swf=url_for('static', filename='AdminInterface'),
                         width='100%', height='100%',
                         title='Admin', version_major='6',
                         version_minor='0', version_revision='65')

@admin.route('/login/', methods=['POST'])
def login():
  user = g.query_db('select id from admins where name = ? and password = ?',
      (request.form['username'], g.sha1(request.form['password'])), True)
  suc = user is not None
  return jsonify({'success': suc})


# Bot-command oriented functions (could be its own view)
@admin.route('/bots/get_bots/', methods=['GET'])
def get_bots():
  return jsonify({'bots': []})

@admin.route('/bots/commands/', methods=['GET'])
def get_commands():
  # Note: jsonify() does not allow top-level arrays due to
  # a security risk.
  commands = g.query_db('select id, name from commands')
  return jsonify({'commands': commands})

@admin.route('/bots/commands/send/', methods=['POST'])
@admin.route('/bots/commands/send/<int:command_id>/<users>', methods=['GET'])
def send_command(command_id=None, users=None):
  if command_id is None or users is None:
    command_id = int(request.form['command_id'])
    users = map(int, request.form['users'].split(','))
  for user_id in users:
    q = 'insert into bot_command_queue (bot_id, command_id) VALUES (?, ?)'
    g.db.cursor().execute(q, (user_id, command_id))
  g.db.commit()
  return jsonify({'success': True})


