use curriculum42;

create table if not exists db_credentials (
id int not null auto_increment,
name varchar (45) not null,
login varchar (45) not null,
password varchar (45) not null,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
primary key (id)
) default charset = utf8mb4;

drop table db_credentials;

insert into db_credentials values 
(default, 'teste', 'teste', 'teste', default, default);

INSERT INTO db_credentials (name, login, password) VALUES ('mail', 'leonardo.vinci@catagua.com.br', 'BI.ctg2024');

update db_credentials set diretorio = 'Desktop' where id = 1;

select * from db_credentials;