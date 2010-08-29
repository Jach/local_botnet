drop table if exists admins;
create table admins (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name STRING NOT NULL,
  password CHAR(40) NOT NULL
);

drop table if exists bots;
create table bots (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ip STRING NOT NULL
);
