CREATE DATABASE IF NOT EXISTS todo_list;
USE todo_list;

CREATE TABLE IF NOT EXISTS usuarios(
    id INT (25) AUTO_INCREMENT  NOT NULL,
    nombre VARCHAR (100),
    apellido VARCHAR  (255),
    email VARCHAR (255) NOT NULL,
    contrasena VARCHAR (255) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE (email)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS notas(
    id INT (25) AUTO_INCREMENT NOT NULL,
    usuarios_id INT (25) NOT NULL,
    titulo VARCHAR (255) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha DATE NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY (id),
    CONSTRAINT fk_notas_usuarios FOREIGN KEY (usuarios_id) REFERENCES usuarios(id) 
)ENGINE=InnoDb;

ALTER TABLE `notas` ADD `realizada` TINYINT NOT NULL AFTER `fecha`;