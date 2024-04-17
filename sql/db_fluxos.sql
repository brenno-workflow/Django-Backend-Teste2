use curriculum42;

create table if not exists db_fluxos (
id int not null auto_increment,
name varchar (45) not null,
db_process_id int,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
primary key (id),
foreign key (db_process_id) references db_process(id)
) default charset = utf8mb4;

drop table db_fluxos;

insert into db_fluxos values 
(default, 'teste', 1, default, default);

INSERT INTO db_fluxos (name, db_services_id, db_modules_id, db_process_id, db_subprocess_id) VALUES ('web_simpliss_piracicaba_login', 6, 5, 1, 1);

update db_fluxos set name = 'web_simpliss_piracicaba_login' where id = 20;

DELETE FROM db_fluxos WHERE id = 8;

select * from db_fluxos;