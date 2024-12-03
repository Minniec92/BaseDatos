import mysql.connector

# Conexión a la base de datos MySQL
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='sistema_ventas',
            user='administrador', 
            password='admin1234'  
        )
        if connection.is_connected():
            print("Te conectaste correctamente a la base de datos de nuestro sistema :) ")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos, volvé a intentar porfa: {e}")
        return None

# Menú principal del CLI
def menu():
    print("\nBienvenido al Sistema de Ventas de los alumnos de la UTN B.Bca")
    print("1. Gestión de Productos")
    print("2. Gestión de Clientes")
    print("3. Procesamiento de Órdenes")
    print("4. Búsquedas Avanzadas")
    print("5. Reporte de productos más vendidos")
    print("6. Modificación de valor de un producto")
    print("7. Salir")

def gestionar_productos(connection):
    cursor = connection.cursor()
    print("\nGestión de Productos")
    print("1. Agregar Producto")
    print("2. Actualizar Producto")
    print("3. Ver Productos")
    print("4. Eliminar Producto")
    opcion = input("Elige una opción válida (del 1 al 4): ")

    if opcion == '1':
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción del producto: ")
        precio = float(input("Precio del producto: "))
        stock = int(input("Stock disponible: "))
        categoria_id = int(input("ID de la categoría: "))
        cursor.execute("INSERT INTO Producto (nombre, descripcion, precio, stock, categoria_id) VALUES (%s, %s, %s, %s, %s)",
                    (nombre, descripcion, precio, stock, categoria_id))
        connection.commit()
        print("Producto agregado exitosamente!")

    elif opcion == '2':
        cursor.callproc("obtener_productos")
        for producto in cursor.stored_results():
            productos = producto.fetchall()
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[3]}, Stock: {producto[4]}")
        product_id = int(input("ID del producto a actualizar: "))
        nuevo_precio = float(input("Nuevo precio: "))
        nueva_cantidad = int(input("Nuevo stock: "))
        cursor.callproc("actualizar_producto", (product_id, nuevo_precio, nueva_cantidad))  # Llamamos al procedimiento
        connection.commit()
        print("Producto actualizado exitosamente!")

    elif opcion == '3':
        cursor.callproc("obtener_productos")
        for producto in cursor.stored_results():
            productos = producto.fetchall()
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[3]}, Stock: {producto[4]}")
    
    elif opcion == '4':
        cursor.callproc("obtener_productos")
        for producto in cursor.stored_results():
            productos = producto.fetchall()
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}")
        product_id = int(input("ID del producto a eliminar: "))
        cursor.callproc("eliminar_producto", (product_id,))  # Llamamos al procedimiento
        connection.commit()
        print("Producto eliminado exitosamente!")
   
def gestionar_clientes(connection):
    cursor = connection.cursor()
    print("\nGestión de Clientes")
    print("1. Registrar Cliente")
    print("2. Actualizar Cliente")
    print("3. Ver Clientes")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        nombre = input("Nombre del cliente: ")
        email = input("Email del cliente: ")
        telefono = input("Teléfono del cliente: ")
        direccion = input("Dirección del cliente: ")
        
        cursor.execute("INSERT INTO Cliente (nombre, email, telefono, direccion) VALUES (%s, %s, %s, %s)",
                    (nombre, email, telefono, direccion))
        connection.commit()
        print("Cliente registrado exitosamente!")

    elif opcion == '2':
        cursor.execute("SELECT * FROM Cliente")
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}, Teléfono: {cliente[3]}, Dirección: {cliente[4]}")
        cliente_id = int(input("ID del cliente a actualizar: "))
        nuevo_telefono = input("Nuevo teléfono: ")
        nueva_direccion = input("Nueva dirección: ")
        
        cursor.execute("UPDATE Cliente SET telefono = %s, direccion = %s WHERE id_cliente = %s", 
                    (nuevo_telefono, nueva_direccion, cliente_id))
        connection.commit()
        print("Cliente actualizado exitosamente!")

    elif opcion == '3':
        cursor.execute("SELECT * FROM Cliente")
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}, Teléfono: {cliente[3]}, Dirección: {cliente[4]}")

def procesar_ordenes(connection):
    cursor = connection.cursor()
    print("\nProcesamiento de Órdenes")
    cliente_id = int(input("ID del cliente: "))
    fecha = input("Fecha de la orden (YYYY-MM-DD): ")
    total = float(input("Total de la orden: "))
    
    cursor.execute("INSERT INTO Orden (cliente_id, fecha, total) VALUES (%s, %s, %s)", (cliente_id, fecha, total))
    connection.commit()
    print("Orden procesada exitosamente!")

def reporte_productos_mas_vendidos(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT p.nombre, SUM(d.cantidad) AS cantidad_vendida
        FROM Producto p
        JOIN DetalleOrden d ON p.id_producto = d.producto_id
        GROUP BY p.id_producto
        ORDER BY cantidad_vendida DESC
        LIMIT 1
    """)
    producto = cursor.fetchone()
    print(f"\nProducto más vendido: {producto[0]}, Cantidad vendida: {producto[1]}")

# Modificar valor de productos (actualizar el stock de todos)
def modificar_valor_producto(connection):
    cursor = connection.cursor()
    cantidad_maxima = int(input("Cantidad máxima que se puede vender para todos los productos: "))
    
    cursor.execute("UPDATE Producto SET stock = %s", (cantidad_maxima,))
    connection.commit()
    print(f"Stock de todos los productos actualizado a {cantidad_maxima} exitosamente.")

# Función para realizar búsqueda avanzada
def busqueda_avanzada(connection):
    cursor = connection.cursor()
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
    cursor.execute("SELECT * FROM Producto WHERE nombre LIKE %s", ('%' + nombre_producto + '%',))
    productos = cursor.fetchall()
    if productos:
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[3]}, Stock: {producto[4]}")
    else:
        print("No se encontraron productos con ese nombre.")

def main():
    connection = connect_to_database()
    if connection is None:
        return

    while True:
        menu()
        option = input("Elige una opción: ")
        
        if option == '1':
            gestionar_productos(connection)
        elif option == '2':
            gestionar_clientes(connection)
        elif option == '3':
            procesar_ordenes(connection)
        elif option == '4':
            busqueda_avanzada(connection)  # Llamamos a la búsqueda avanzada
        elif option == '5':
            reporte_productos_mas_vendidos(connection)
        elif option == '6':
            modificar_valor_producto(connection)
        elif option == '7':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
    
    connection.close()

if __name__ == '__main__':
    main()
