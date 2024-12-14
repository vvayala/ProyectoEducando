CREATE DATABASE Educando;
USE Educando;

CREATE TABLE Usuarios (
    IDUsuario INT IDENTITY(1,1) PRIMARY KEY,
    Usuario NVARCHAR(50) NOT NULL,
    Contrasena NVARCHAR(255) NOT NULL,
    Email NVARCHAR(100) UNIQUE,
);

CREATE TABLE Lecciones (
    IDLeccion INT IDENTITY(1,1) PRIMARY KEY,
    NombreLeccion NVARCHAR(255) NOT NULL,
    Contenido NVARCHAR(MAX),
);

CREATE TABLE LeccionesCompletadas (
    IDCompletado INT IDENTITY(1,1) PRIMARY KEY,
    IDUsuario INT NOT NULL,
    IDLeccion INT NOT NULL,
    Inicio TIME,
	Fin TIME,
	TotalPreguntas INT,
    RespuestasCorrectas INT,
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario),
    FOREIGN KEY (IDLeccion) REFERENCES Lecciones(IDLeccion)
);

CREATE TABLE Preguntas (
    IDPregunta INT IDENTITY(1,1) PRIMARY KEY,
    IDLeccion INT NOT NULL,
    Pregunta NVARCHAR(MAX),
    FOREIGN KEY (IDLeccion) REFERENCES Lecciones(IDLeccion)
);

CREATE TABLE Opciones (
    IDOpcion INT IDENTITY(1,1) PRIMARY KEY,
    IDPregunta INT NOT NULL,
    Opcion NVARCHAR(255),
    EsCorrecta BIT,
    FOREIGN KEY (IDPregunta) REFERENCES Preguntas(IDPregunta)
);


