
def agregar_producto(inventario):
    """Solicita datos al usuario y agrega un producto validado al inventario."""
    
    while True:
        nombre = input("Nombre: ")
        if not nombre.strip() or not nombre.replace(" ", "").isalpha():
            print("El nombre solo puede contener letras y no puede estar vacío.")
            continue
        break

    while True:
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                print("El precio debe ser positivo.")
                continue
            break
        except ValueError:
            print("Ingrese un precio válido.")

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad < 0:
                print("La cantidad debe ser positiva.")
                continue
            break
        except ValueError:
            print("Ingrese una cantidad válida.")

    # Agregar al inventario
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado exitosamente.\n")


def mostrar_inventario(inventario):
    print("\n---Productos en el inventario---\n")
    
    if not inventario:            
        print("No hay productos en el inventario.")
    else: 
        for item in inventario:
            print(f"Nombre: {item['nombre']} | Precio: {item['precio']} | Cantidad: {item['cantidad']}")
    
def buscar_producto(inventario, name): 

    for item in inventario:
        if item['nombre'] == name:
             print(f"\nProducto encontrado: Nombre: {item['nombre']} | Precio: {item['precio']} | Cantidad: {item['cantidad']}")
             break
    else:
        print("\nNo se encontró el producto")
         

def actualizar_producto(inventario):
    """Actualiza un producto existente solicitando datos validados al usuario."""
    
    nombre_buscar = input("\nIngrese el nombre del producto a actualizar: \n")

    for item in inventario:
        if item['nombre'].lower() == nombre_buscar.lower():

            # Nuevo precio
            while True:
                try:
                    nuevo_precio = float(input(f"Nuevo precio para {item['nombre']}: "))
                    if nuevo_precio < 0:
                        print("El precio debe ser positivo.")
                        continue
                    break
                except ValueError:
                    print("Ingrese un precio válido.")

            # Nueva cantidad
            while True:
                try:
                    nueva_cantidad = int(input(f"Nueva cantidad para {item['nombre']}: "))
                    if nueva_cantidad < 0:
                        print("La cantidad debe ser positiva.")
                        continue
                    break
                except ValueError:
                    print("Ingrese una cantidad válida.")

            # Actualizar
            item['precio'] = nuevo_precio
            item['cantidad'] = nueva_cantidad
            print(f"Producto {item['nombre']} actualizado: Precio = {nuevo_precio}, Cantidad = {nueva_cantidad}\n")
            return  # Fin de la función al actualizar

    print("No se encontró el producto.\n")

def eliminar_producto(inventario, name = None):
    """Elimina un producto del inventario usando while True para validar el nombre."""

    while True:
        if not name:
            name = input("Ingrese el nombre del producto a eliminar: ")

        # Validación: no vacío y solo letras y espacios
        if not name.strip() or not name.replace(" ", "").isalpha():
            print("El nombre solo puede contener letras y no puede estar vacío.")
            name = None
            continue  # Repite la entrada
        break  # Nombre válido, salir del bucle

    # Buscar y eliminar
    for item in inventario:
        if item['nombre'].lower() == name.lower():
            inventario.remove(item)
            print(f"El producto '{item['nombre']}' se eliminó correctamente.\n")
            return
    print("No se encontró el producto.\n")
        

def calcular_estadisticas(inventario):
        #Valida si hay productos
        if not inventario :
            print("No hay datos con los cuales hacer las estadísticas.")
            return {} #Regresa un diccionario vacío cuando no hay datos para calcular

        #Calcular valores y mostrar resultados 
        unidades_totales = sum(item['cantidad'] for item in inventario)
        print(f"La suma total de las unidades es: {unidades_totales}")

        valor_total = sum(item['precio'] * item['cantidad'] for item in inventario)
        print(f"El valor total de los productos es: {valor_total}")

        producto_mas_caro = max(inventario , key = lambda x : x ['precio'])
        print(f"El producto mas caro es: {producto_mas_caro['nombre']} con un valor de {producto_mas_caro['precio']} pesos")

        producto_mayor_stock = max(inventario , key = lambda x : x ['cantidad'])
        print(f"El producto con mayor stock es : {producto_mayor_stock['nombre']} con {producto_mayor_stock['cantidad']} unidades")

        estadisticas = {
            "total_unidades" : unidades_totales,
            "valor_total" : valor_total,
            "producto_mayor_stock" : producto_mayor_stock
        }
        #Regresa mis estadísticas 
        return estadisticas

