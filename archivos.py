import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("El inventario está vacío, no hay productos para guardar")
        return
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if incluir_header:
                writer.writerow(["Nombre", "Precio", "Cantidad"])

            for item in inventario:
                writer.writerow([item['nombre'], item['precio'], item['cantidad']])
        print(f"Archivo CSV guardado correctamente en: {ruta}")
    except Exception as e:
        print("Ocurrió un error al guardar el archivo")
        print(e)


def cargar_csv(ruta):
    inventario = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            encabezado = next(reader, None)
            if encabezado != ["Nombre", "Precio", "Cantidad"]:
                print("El archivo CSV no tiene un formato válido.")
                return []

            for fila in reader:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                try:
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    inventario.append({
                        "nombre": fila[0],
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except ValueError:
                    filas_invalidas += 1
                    continue

        print(f"Inventario cargado desde: {ruta}")
        if filas_invalidas > 0:
            print(f"{filas_invalidas} fila(s) inválida(s) omitida(s).")
        return inventario

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
        return []

    except UnicodeDecodeError:
        print("Error: el archivo no tiene una codificación válida (UTF-8)")
        return []

    except Exception as e:
        print("Ocurrió un error al cargar el archivo.")
        print(e)
        return []


def sobreescribir(ruta, inventario):
    datos_csv = cargar_csv(ruta)

    if not datos_csv:
        print("No se cargaron datos.")
        return inventario

    print("\nArchivo cargado correctamente.")
    decision = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()

    if decision == "S":
        print("Inventario sobrescrito.\n")
        return datos_csv  # inventario nuevo

    print("Fusionando inventarios...\n")

    nombres_existentes = {item["nombre"]: item for item in inventario}

    for nuevo in datos_csv:
        nombre = nuevo["nombre"]
        if nombre in nombres_existentes:
            antiguas = nombres_existentes[nombre]
            antiguas["cantidad"] += nuevo["cantidad"]
            if antiguas["precio"] != nuevo["precio"]:
                print(f"El producto '{nombre}' actualiza el precio de {antiguas['precio']} a {nuevo['precio']}")
                antiguas["precio"] = nuevo["precio"]
        else:
            inventario.append(nuevo)

    print("Fusión completada.\n")
    return inventario
