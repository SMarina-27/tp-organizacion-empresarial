import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Para obtener la ruta relativa donde se encuetra el archivo
BASE = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE, "..", "datos", "ventas.csv")
ARCHIVO_RESULTADOS = os.path.join(BASE, "..", "resultados", "resultados.csv")
# Definicion de variables y diccionarios a utilizar
total_ventas= 0
productos_vendidos = {}
ventas_mensuales = {}
meses ={1: "Enero", 2: "Febrero", 3: "Marzo",
    4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre",
    10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
producto_mas_vendido = ""
cantidad_mas_vendida = 0

def datos_ordenados():
    # Ordena los datos del diccionario de ventas mensuales
    meses_ordenados = sorted(ventas_mensuales.keys())
    totales_ordenados = []
    for mes in meses_ordenados:
        total = sum(ventas_mensuales[mes])
        totales_ordenados.append(total)
    nombres_meses = []
    for mes in meses_ordenados:
        nombres_meses.append(meses[mes])
    return meses_ordenados, totales_ordenados, nombres_meses

def guardar_datos():
    # Genera archivo resultados.csv con los datos mensuales de ventas y el total anual
    try:
        with open(ARCHIVO_RESULTADOS, "w" , newline="", encoding="utf-8-sig") as arc:
            escritor = csv.DictWriter(arc, fieldnames=["mes", "ventas_mensuales"])
            escritor.writeheader()
            meses_ordenados, totales_ordenados, nombres_meses = datos_ordenados()

            for mes, venta in zip(nombres_meses, totales_ordenados):
                escritor.writerow({"mes": (mes), "ventas_mensuales": (venta)})
            escritor.writerow({"mes": "Total ventas anuales","ventas_mensuales": total_ventas})
        print(f"Resultados guardados en: ../tp-analisis-ventas/resultados/")
    except Exception as e:
        print(f"ERROR: Ocurrio un error inesperado: ", type(e).__name__, {e})

def crear_grafico():
    # Esta funcion fue generada mediante ayuda de IA.
       
    meses_ordenados, totales_ordenados, nombres_meses = datos_ordenados()
    # Crear el gráfico

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(nombres_meses, totales_ordenados, 
            marker="o",          # punto en cada mes
            color="steelblue", 
            linewidth=2, 
            markersize=8)

    # Etiquetas con el valor encima de cada punto
    for i, total in enumerate(totales_ordenados):
        ax.annotate(f"${total:.0f}", 
                    xy=(i, total),
                    xytext=(0, 10),
                    textcoords="offset points",
                    ha="center")

    # Títulos y etiquetas
    ax.set_title("Evolución de Ventas Mensuales", fontsize=14, fontweight="bold")
    ax.set_xlabel("Mes", fontsize=12)
    ax.set_ylabel("Total Ventas ($)", fontsize=12)
    ax.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()

    # Guardar en /resultados
    RUTA_GRAFICO = os.path.join(BASE, "..", "resultados", "grafico_ventas.png")
    plt.savefig(RUTA_GRAFICO)
    print(f"Gráfico guardado en: ../tp-analisis-ventas/resultados/")

    #plt.show()

try:
    with open(NOMBRE_ARCHIVO, "r", newline="", encoding="utf-8-sig") as archivo:
        datos = csv.DictReader(archivo, delimiter=";")
        
        # Recorre el diccionario y asignamos variables a los valores
        for linea in datos:
            if not linea["producto"]:
                continue
                 
            producto = linea["producto"]
            cantidad = float(linea["cantidad_vendida"]) # Se convierte el str a tipo float
            precio = float(linea["precio"]) # Se convierte el str a tipo float
            fecha = datetime.strptime(linea["fecha_de_venta"], "%Y-%m-%d") # Se convierte el str a tipo fecha
            venta = precio * cantidad
            total_ventas += venta
            
            # Para armar un diccionario de ventas mensuales
            for i in range (1,13):
                if fecha.month == i:
                    if i not in ventas_mensuales:
                        ventas_mensuales[i] = []
                    ventas_mensuales[i].append(venta)
            
            # Para armar un diccionario de productos vendidos
            if producto not in productos_vendidos:
                productos_vendidos[producto] = []
            productos_vendidos[producto].append(cantidad)    
except FileNotFoundError:
    print("ERROR: Archivo no encontrado")
    print("Verifique que se encuentre en ../tp-analisis-ventas/datos/ y que su nombre sea ventas.csv")
except PermissionError:
    print("ERROR: El archivo podria estar siendo utilizado por otro programa. Verifique.")
except KeyError:
    print("ERROR: El archivo no posee los encabezados correctos. Verifique")
    print("Encabezados: producto | cantidad_vendida | precio | fecha_de_venta")
except ValueError as e:
    print(f"ERROR: Archivo incompleto o con datos errones: {e}")
except Exception as e:
    print(f"ERROR: Ocurrio un error inesperado: {e}")
else:
    print("\nArchivo procesado exitosamente")
    print("______________________________________________________________\n")
    # Para imprimir el monto mensual de ventas
    meses_ordenados, totales_ordenados, nombres_meses = datos_ordenados()
    for mes, venta in zip(nombres_meses, totales_ordenados):
        print(f"Las ventas de {mes} fueron $ {venta}")
    print("______________________________________________________________\n")    
    print(f"Las ventas totales fueron $: {total_ventas}")
    guardar_datos()
    # Determina el producto mas vendido
    for producto,cantidad in productos_vendidos.items():
        cantidad_vendida = sum(cantidad)
        if cantidad_vendida > cantidad_mas_vendida:
            cantidad_mas_vendida = cantidad_vendida
            producto_mas_vendido = producto
    print("______________________________________________________________\n")
    print(f"El producto mas vendido fue {producto_mas_vendido} con un total de {cantidad_mas_vendida} unidades")
    print("______________________________________________________________\n")
    crear_grafico()
    
finally:
    print("El proceso a finalizado")
