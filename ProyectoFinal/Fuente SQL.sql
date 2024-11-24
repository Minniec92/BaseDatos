CREATE DATABASE sistema_ventas;
USE sistema_ventas;

CREATE TABLE Categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE Producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id_categoria) ON DELETE SET NULL
);

CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    direccion TEXT NOT NULL
);

CREATE TABLE Orden (
    id_orden INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id_cliente) ON DELETE CASCADE
);

CREATE TABLE DetalleOrden (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    orden_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (orden_id) REFERENCES Orden(id_orden) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES Producto(id_producto) ON DELETE RESTRICT
);

-- Insertar categorías iniciales (se podrían agregar más)
INSERT INTO Categoria (nombre) VALUES 
    ('Celulares'),
    ('Belleza'),
    ('Textil'),
    ('Baño'),
    ('Jardín'),
    ('Hogar'),
    ('Deportes'),
    ('Electrónica'),
    ('Oficina'),
    ('Juguetes');


INSERT INTO Producto (nombre, descripcion, precio, stock, categoria_id) VALUES
    ('Celular', 'Iphone 16 pro max', 2599.99, 100, 1),
    ('Notebook', 'Computadora portátil con procesador i7', 7999.99, 50, 1),
    ('Camiseta', 'Camiseta de la selección argentina', 2119.99, 200, 2),
    ('Pantalón', 'Pantalón de lino de damam', 29.99, 150, 2),
    ('Lámpara', 'Lámpara LED moderna', 49.99, 75, 3),
    ('Balón de fútbol', 'Balón oficial para jugar fútbol', 29.99, 120, 4),
    ('Raqueta de tenis', 'Raqueta ligera de fibra de carbono', 149.99, 60, 4),
    ('Muñeca', 'Muñeca para niñas', 15.99, 250, 5),
    ('Juego de construcción', 'Juego de bloques tipo LEGO', 39.99, 180, 5);


INSERT INTO Cliente (nombre, email, telefono, direccion) VALUES
    ('Juan Ramirez', 'juan.raminnez@gmail.com', '35446578', 'Calle Av Alemm 123'),
    ('Ana Gómez', 'ana.gomez@hotmail.com', '0987654321', 'Av. Libertad 456'),
    ('Carlos Rodríguez', 'carlos.rodriguez@yahoo.com.ar', '1122334455', 'Calle Real 789'),
    ('María López', 'maria.lopez@email.com', '2233445566', 'Calle Secundaria 321'),
    ('Laura Martínez', 'laura.martinez@email.com', '3344556677', 'Av. Central 654'),
    ('Pedro Sánchez', 'pedro.sanchez@email.com', '4455667788', 'Calle Nueva 987'),
    ('Lucía Torres', 'lucia.torres@email.com', '5566778899', 'Calle del Sol 159'),
    ('José Fernández', 'jose.fernandez@email.com', '6677889900', 'Calle del Río 357'),
    ('Sofía Pérez', 'sofia.perez@email.com', '7788990011', 'Av. del Mar 753'),
    ('Miguel Díaz', 'miguel.diaz@email.com', '8899001122', 'Calle Verde 246');

-- Insertar órdenes iniciales
INSERT INTO Orden (cliente_id, fecha, total) VALUES
    (1, '2024-11-01', 7599.99),
    (2, '2024-11-14', 1499.99),
    (3, '2024-12-03', 269.98),
    (4, '2024-08-04', 8449.99),
    (5, '2024-11-09', 179.97);

-- Insertar detalles de las órdenes iniciales
INSERT INTO DetalleOrden (orden_id, producto_id, cantidad, precio_unitario) VALUES
    (1, 1, 1, 599.99),
    (2, 2, 1, 999.99),
    (3, 3, 2, 19.99),
    (4, 5, 1, 399.99),
    (5, 9, 3, 15.99);
