CREATE TABLE Usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

CREATE TABLE CO2_Emisiones (
    id_emision SERIAL PRIMARY KEY,
    provincia VARCHAR(100) NOT NULL,
    anio INT NOT NULL,
    cantidad DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Preguntas (
    id_pregunta SERIAL PRIMARY KEY,
    pregunta TEXT NOT NULL,
    respuesta_correcta TEXT NOT NULL,
    respuesta_opcion1 TEXT NOT NULL,
    respuesta_opcion2 TEXT NOT NULL,
    respuesta_opcion3 TEXT NOT NULL
);

CREATE TABLE Puntajes (
    id_puntaje SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuarios(id_usuario),
    puntaje INT NOT NULL,
    fecha DATE NOT NULL
);

CREATE TABLE Respuestas_Trivia (
    id_respuesta SERIAL PRIMARY KEY,
    id_pregunta INT REFERENCES Preguntas(id_pregunta),
    id_usuario INT REFERENCES Usuarios(id_usuario),
    respuesta_seleccionada TEXT NOT NULL,
    fecha DATE NOT NULL
);

-- Relación entre Puntajes y Usuarios
ALTER TABLE Puntajes
ADD CONSTRAINT fk_puntajes_usuarios
FOREIGN KEY (id_usuario)
REFERENCES Usuarios(id_usuario);

-- Relación entre Respuestas_Trivia y Usuarios
ALTER TABLE Respuestas_Trivia
ADD CONSTRAINT fk_respuestas_usuarios
FOREIGN KEY (id_usuario)
REFERENCES Usuarios(id_usuario);

-- Relación entre Respuestas_Trivia y Preguntas
ALTER TABLE Respuestas_Trivia
ADD CONSTRAINT fk_respuestas_preguntas
FOREIGN KEY (id_pregunta)
REFERENCES Preguntas(id_pregunta);

-- Insertar registros para las 24 provincias, en el rango de 3 años
INSERT INTO CO2_Emisiones (provincia, anio, cantidad)
VALUES
('Azuay', 2021, 1800000), ('Azuay', 2022, 1930000), ('Azuay', 2023, 2050000),
('Bolívar', 2021, 650000), ('Bolívar', 2022, 700000), ('Bolívar', 2023, 750000),
('Cañar', 2021, 700000), ('Cañar', 2022, 750000), ('Cañar', 2023, 800000),
('Carchi', 2021, 600000), ('Carchi', 2022, 650000), ('Carchi', 2023, 700000),
('Chimborazo', 2021, 1200000), ('Chimborazo', 2022, 1300000), ('Chimborazo', 2023, 1400000),
('Cotopaxi', 2021, 1100000), ('Cotopaxi', 2022, 1200000), ('Cotopaxi', 2023, 1300000),
('El Oro', 2021, 2200000), ('El Oro', 2022, 2400000), ('El Oro', 2023, 2600000),
('Esmeraldas', 2021, 1800000), ('Esmeraldas', 2022, 1950000), ('Esmeraldas', 2023, 2100000),
('Galápagos', 2021, 250000), ('Galápagos', 2022, 300000), ('Galápagos', 2023, 350000),
('Guayas', 2021, 10000000), ('Guayas', 2022, 10800000), ('Guayas', 2023, 11500000),
('Imbabura', 2021, 1000000), ('Imbabura', 2022, 1080000), ('Imbabura', 2023, 1200000),
('Loja', 2021, 950000), ('Loja', 2022, 1000000), ('Loja', 2023, 1100000),
('Los Ríos', 2021, 2500000), ('Los Ríos', 2022, 2700000), ('Los Ríos', 2023, 2900000),
('Manabí', 2021, 4800000), ('Manabí', 2022, 5100000), ('Manabí', 2023, 5400000),
('Morona Santiago', 2021, 450000), ('Morona Santiago', 2022, 500000), ('Morona Santiago', 2023, 550000),
('Napo', 2021, 400000), ('Napo', 2022, 450000), ('Napo', 2023, 500000),
('Orellana', 2021, 600000), ('Orellana', 2022, 650000), ('Orellana', 2023, 700000),
('Pastaza', 2021, 500000), ('Pastaza', 2022, 550000), ('Pastaza', 2023, 600000),
('Pichincha', 2021, 8000000), ('Pichincha', 2022, 8600000), ('Pichincha', 2023, 9000000),
('Santa Elena', 2021, 1800000), ('Santa Elena', 2022, 1900000), ('Santa Elena', 2023, 2000000),
('Santo Domingo', 2021, 2200000), ('Santo Domingo', 2022, 2400000), ('Santo Domingo', 2023, 2600000),
('Sucumbíos', 2021, 800000), ('Sucumbíos', 2022, 850000), ('Sucumbíos', 2023, 900000),
('Tungurahua', 2021, 1500000), ('Tungurahua', 2022, 1600000), ('Tungurahua', 2023, 1700000),
('Zamora Chinchipe', 2021, 400000), ('Zamora Chinchipe', 2022, 450000), ('Zamora Chinchipe', 2023, 500000);

-- Insertar preguntas
INSERT INTO Preguntas (pregunta, respuesta_correcta, respuesta_opcion1, respuesta_opcion2, respuesta_opcion3)
VALUES 
('¿Cuál es la provincia con mayor emisión de CO2 en el año 2021?', 'Guayas', 'Pichincha', 'Manabí', 'Esmeraldas'),
('¿Cuál fue la cantidad promedio de CO2 emitido en 2022 por todas las provincias?', '950,000 toneladas', '800,000 toneladas', '1,100,000 toneladas', '1,200,000 toneladas'),
('En 2023, ¿qué provincia tuvo la menor emisión de CO2?', 'Galápagos', 'Carchi', 'Bolívar', 'Imbabura'),
('¿Cuántas provincias emitieron más de 1,000,000 toneladas de CO2 en 2021?', '10 provincias', '8 provincias', '12 provincias', '14 provincias'),
('¿En qué año la emisión total de CO2 en Ecuador fue la mayor?', '2023', '2021', '2022', 'Son iguales en todos los años');
