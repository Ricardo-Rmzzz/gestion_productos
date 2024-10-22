productos = []

def añadir_producto():
    while True:
        nombre = input("Nombre del producto: ")
        if all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
            break
        else:
            print("El nombre debe contener solo caracteres alfabéticos. Inténtalo nuevamente")
    
    while True:
        try:
            precio = int(input("Precio del producto: "))
            if precio > 0:  
                break
            else:
                print("El precio debe ser un número entero positivo.")
        except ValueError:
            print("Error: El precio debe ser un número entero. Inténtalo nuevamente")
    
    while True:
        cantidad = input("Cantidad disponible: ").strip()
        if cantidad.isdigit() and int(cantidad) >= 0:
            break
        else:
            print("La cantidad debe ser un número entero positivo. Inténtalo nuevamente")
    
    producto = {'nombre': nombre.strip(), 'precio': int(precio), 'cantidad': int(cantidad)}
    productos.append(producto)
    print(f"Producto '{producto['nombre']}' añadido exitosamente.")

def ver_productos():
    if not productos:
        print("No hay productos en el sistema.")
        return
    
    print("\nLista de productos:")
    for idx, producto in enumerate(productos, start=1):
        print(f"{idx}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    ver_productos()
    if not productos:
        return
    
    try:
        indice = int(input("Selecciona el número del producto que quiere actualizar: ")) - 1
        
        if 0 <= indice < len(productos):
            print("Deja el campo en blanco si no deseas cambiar el valor.")
            
            nombre = input(f"Nuevo nombre ({productos[indice]['nombre']}): ")
            precio = input(f"Nuevo precio ({productos[indice]['precio']}): ")
            cantidad = input(f"Nueva cantidad ({productos[indice]['cantidad']}): ")

            if nombre.strip():
                productos[indice]['nombre'] = nombre.strip()
            if precio.strip():
                while not precio.replace('.', '', 1).isdigit():
                    precio = input("El precio debe ser un número. Ingresa el nuevo precio: ").strip()
                productos[indice]['precio'] = int(precio)
            if cantidad.strip():
                while not cantidad.isdigit():
                    cantidad = input("La cantidad debe ser un número. Ingresa la nueva cantidad: ").strip()
                productos[indice]['cantidad'] = int(cantidad)
            
            print("El producto se actualizó exitosamente.")
        else:
            print("El número de producto no es válido.")
    except ValueError:
        print("Entrada no válida. Asegúrate de ingresar un número.")

def eliminar_producto():
    ver_productos()
    if not productos:
        return
    
    try:
        indice = int(input("Por favor seleccione el número del producto que deseas eliminar: ")) - 1
        
        if 0 <= indice < len(productos):
            eliminado = productos.pop(indice)
            print(f"Producto '{eliminado['nombre']}' eliminado exitosamente.")
        else:
            print("Número de producto no válido.")
    except ValueError:
        print("Entrada no válida. Asegúrate de ingresar un número.")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}\n")
    print("Datos guardados en 'productos.txt'.")
    
def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:  # Asegurarse de que haya 3 elementos
                    nombre = datos[0].strip()
                    precio = int(datos[1].strip())  # Cambié a float para mantener el tipo correcto
                    cantidad = int(datos[2].strip())
                    productos.append({
                        'nombre': nombre,
                        'precio': precio,
                        'cantidad': cantidad
                    })
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt'. Se creará al guardar.")
    except ValueError:
        print("Error en el formato de datos en 'productos.txt'. Asegúrate de que estén correctamente formateados.")

def menu():
    cargar_datos()  # Cargar datos al iniciar el programa
    while True:
        print("\n    SISTEMA GESTION DE PRODUCTOS    ")
        print("Lista de opciones")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Ingrese el número de la opción que desea operar: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida (del 1 al 5).")

# Ejecutar el menú
menu()