
create database cr;
use cr;
GRANT ALL PRIVILEGES ON cr.* TO pentesterlab@'localhost' IDENTIFIED BY 'pentesterlab';
create table users ( login VARCHAR(50) not null  primary key , password VARCHAR(50));

INSERT INTO `users` (login,password) VALUES ('admin','bcd86545c5903856961fa21b914c5fe4');



