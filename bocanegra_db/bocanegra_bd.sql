CREATE DATABASE IF NOT EXISTS bocanegra_bd;
USE bocanegra_bd;

-- Tabla Aula
CREATE TABLE aula (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(5) NOT NULL,
    planta TINYINT NOT NULL DEFAULT 1,
    situacion ENUM('DISPONIBLE', 'OCUPADA', 'EN MANTENIMIENTO') NOT NULL DEFAULT 'DISPONIBLE'
);

-- Tabla Estudiante
CREATE TABLE estudiante (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    numero_matricula VARCHAR(20) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(100) NOT NULL
);

-- Tabla Asignatura
CREATE TABLE asignatura (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    ciclo ENUM('I', 'II', 'III') NOT NULL DEFAULT 'I',
    descripcion VARCHAR(255) NOT NULL
);

-- Tabla Estudia (relación entre estudiante y asignatura)
CREATE TABLE estudia (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    estudiante_id BIGINT UNSIGNED NOT NULL,
    asignatura_id BIGINT UNSIGNED NOT NULL,
    hora TIME NOT NULL DEFAULT '08:00:00',
    FOREIGN KEY (estudiante_id) REFERENCES estudiante(id),
    FOREIGN KEY (asignatura_id) REFERENCES asignatura(id)
);

DELIMITER //

CREATE PROCEDURE InsertarAula(IN numero VARCHAR(5), IN planta TINYINT, IN situacion ENUM('DISPONIBLE', 'OCUPADA', 'EN MANTENIMIENTO'))
BEGIN
    INSERT INTO aula (numero, planta, situacion) VALUES (numero, planta, situacion);
END //

CREATE PROCEDURE ConsultarAula(IN aula_id BIGINT)
BEGIN
    SELECT * FROM aula WHERE id = aula_id;
END //

CREATE PROCEDURE ConsultarAulas()
BEGIN
    SELECT * FROM aula;
END //

CREATE PROCEDURE ActualizarAula(IN aula_id BIGINT, IN numero VARCHAR(5), IN planta TINYINT, IN situacion ENUM('DISPONIBLE', 'OCUPADA', 'EN MANTENIMIENTO'))
BEGIN
    UPDATE aula SET numero = numero, planta = planta, situacion = situacion WHERE id = aula_id;
END //

CREATE PROCEDURE EliminarAula(IN aula_id BIGINT)
BEGIN
    DELETE FROM aula WHERE id = aula_id;
END //

DELIMITER ;

