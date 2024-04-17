use curriculum42;

create table if not exists db_control (
id int not null auto_increment,
name varchar (45) not null,
path varchar (300) not null,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
primary key (id)
) default charset = utf8mb4;

drop table db_control;

insert into db_control values 
(default, 'teste', 'teste', default, default);

INSERT INTO db_control (name, url) VALUES ('sid_cliente_workflow', 'https://sid.catagua.com.br/cliente/workflow.php');

update db_control set url = 'http://onbasehomolog.catagua.com.br/' where id = 3;

select * from db_control;