-- == CREACION DE TABLAS == --

CREATE TABLE marca (

    id_marca INTEGER PRIMARY KEY AUTOINCREMENT,
    -- INTEGER = valor entero
    -- PRIMARY KEY = llave principal
    -- AUTOINCREMENT = incremento automático

    nombre_marca TEXT,
    -- TEXT = cadena de texto

    nacionalidad TEXT

);

CREATE TABLE producto (

    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_producto TEXT,
    descripcion TEXT,
    precio NUMERIC,

    id_marca INTEGER,
    FOREIGN KEY (id_marca) REFERENCES marca(id_marca)

);

--== INSERTAR DATOS == --

INSERT INTO marca (nombre_marca, nacionalidad) VALUES
    ('Samsung', 'Corea'),
    ('Redmi', 'China');

INSERT INTO producto (nombre_producto, descripcion, precio, id_marca) VALUES
    ('Monitor', '24" 8K', 1000, 1),
    ('Portatil', 'Ryzen 7 7500U', 1300, 1),
    ('Celular', 'Redmi Note 15 Pro', 1100, 2),
    ('Audifonos', 'Redmi Buds 4', 1100, 2);

-- == CONSULTAS == --

SELECT * FROM marca;

SELECT * 
FROM producto AS p
INNER JOIN marca AS m 
ON p.id_marca = m.id_marca;

-- == ACTUALIZAR == --

UPDATE marca
SET nombre_marca = nombre_marca || ' *';

UPDATE marca set nacionalidad = 'Estados Unidos' where id_marca = 2;

/* eliminar */
delete from producto where id_producto = 4;