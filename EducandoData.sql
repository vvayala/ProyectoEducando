USE Educando

-- Insertar datos en la tabla Usuarios
INSERT INTO Usuarios
VALUES 
('Moises1', 'samsung1', 'moises1@gmail.com'),
('Carlos1', 'samsung2', 'carlos1@gmail.com'),
('Gabriel1', 'samsung3', 'gabriel1@gmail.com'),
('Tania1', 'samsung4', 'tania1@gmail.com'),
('Vilic1', 'samsung5', 'vilic1@gmail.com');

-- Insertar datos en la tabla Lecciones
INSERT INTO Lecciones
VALUES 
('Cuento1', 'Contenido del cuento 1...'),
('Cuento2', 'Contenido del cuento 2...'),
('Cuento3', 'Contenido del cuento 3...'),
('Cuento4', 'Contenido del cuento 4...'),
('Cuento5', 'Contenido del cuento 5...');

--Insertar datos en la tabla Preguntas
INSERT INTO Preguntas
VALUES 
(1, '¿Cuál es el nombre del personaje principal?'),
(1, '¿Dónde ocurre la historia?'),
(2, '¿Qué descubre el personaje?'),
(3, '¿Quién acompaña al protagonista?'),
(4, '¿Qué sucede al final?');

--Insertar datos en la tabla Opciones
INSERT INTO Opciones
VALUES 
(1, 'Juan', 1),
(1, 'Pedro', 0), 
(1, 'Luis', 0),  
(2, 'En una ciudad', 1),
(2, 'En un bosque', 0),
(2, 'En una playa', 0),
(3, 'Un tesoro', 1),
(3, 'Un mapa', 0),
(3, 'Un libro', 0),
(4, 'Un perro', 1),
(4, 'Un gato', 0),
(4, 'Un pájaro', 0),
(5, 'El personaje se salva', 1),
(5, 'El personaje se pierde', 0),
(5, 'El personaje encuentra su hogar', 0);

-- Insertar datos en la tabla LeccionesCompletadas
INSERT INTO LeccionesCompletadas
VALUES 
(1, 1, '00:45:00',10, 5),
(1, 2, '01:00:00',4, 4),
(2, 3, '00:30:00',11, 6),
(3, 4, '00:40:00',10, 7),
(4, 5, '00:50:00',10, 8);
