create database Projeto;

use Projeto;

create table Animais(

id	int primary key auto_increment,
nome 	varchar (60)	not	null,
data_nasc varchar(30)	not null,
peso decimal (6,2) 	check (peso>0),
cor	varchar(60),

id_especies	int references especies(id)
);

create table especies(

id 	int primary key auto_increment,
nome	varchar(60) unique not null


);

insert into especies value (null, "Cachorro");
insert into especies value (null, "Gatos");
insert into especies value (null, "Aves");
insert into especies value (null, "Roedores");

create table clientes(
id    int primary key auto_increment,
nome    varchar(60) not null,
cpf     varchar (14),
email    varchar(60),
telefone varchar(20),
endereco    varchar(60),
id_animal     int references Animais(id)




);

