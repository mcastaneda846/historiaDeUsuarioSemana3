from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto,eliminar_producto,calcular_estadisticas
from archivos import guardar_csv, sobreescribir

inventario = []

while True:
    print("\n-----INVENTARIO AVANZADO-----\n"
          "\nMenú principal\n"
          "\n1. Agregar\n"
          "2. Mostrar\n"
          "3. Buscar\n"
          "4. Actualizar\n"
          "5. Eliminar\n"
          "6. Estadísticas\n"
          "7. Guardar CSV\n"
          "8. Cargar CSV\n"
          "9. Salir")
    
    try: 
        opcion = int(input("Ingrese la opción: "))
    except ValueError:
        print("\nDebe ingresar un número entre 1 y 9")
        continue

    match opcion:
        case 1:
            print("\n-----AGREGAR PRODUCTOS-----\n")
            agregar_producto(inventario)

        case 2:
            mostrar_inventario(inventario)

        case 3:
            print("\n----BUSCAR PRODUCTO----")
            name = input("\nIngrese el nombre del producto: ")
            buscar_producto(inventario, name)

        case 4:
            print("\n-----ACTUALIZAR PRODUCTOS-----")
            actualizar_producto(inventario)

        case 5:
            print("\n-----ELIMINAR PRODUCTO-----\n")
            eliminar_producto(inventario , name = None)

        case 6:
            print("\n-----ESTADISTICAS-----\n")
            calcular_estadisticas(inventario)

        case 7:
            ruta = "inventario.csv"
            guardar_csv(inventario, ruta, incluir_header=True)

        case 8:
            ruta = "inventario.csv"
            inventario = sobreescribir(ruta, inventario)
            guardar_csv(inventario , ruta)
            
        case 9:
            print("Saliendo del programa...")
            break

        case _:
            print("\nIngrese un valor entre 1 y 9")