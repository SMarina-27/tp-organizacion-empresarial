# Codigo generado por ayuda de IA
# Propósito: Generar un dataset simulado de ventas para análisis
# Los datos son ficticios y representan ventas de una pequeña empresa

import csv
import os
import random
from datetime import date, timedelta

# -------------------------------------------------------
# Configuración de rutas relativas al script
# -------------------------------------------------------
BASE = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV = os.path.join(BASE, "..", "datos", "ventas.csv")

# -------------------------------------------------------
# Datos de productos con sus precios base
# -------------------------------------------------------
PRODUCTOS = [
    ("Yerba Mate 500g",     1500),
    ("Aceite Girasol 1L",   2200),
    ("Arroz 1kg",            800),
    ("Fideos 500g",          600),
    ("Azucar 1kg",           900),
    ("Harina 1kg",           700),
    ("Leche 1L",            1100),
    ("Pan Frances",          400),
    ("Sal Fina 1kg",         350),
    ("Pure de Tomate 500g",  550),
]

# -------------------------------------------------------
# Generación del dataset
# -------------------------------------------------------
CANTIDAD_REGISTROS = 150
FECHA_INICIO = date(2026, 1, 1)
FECHA_FIN    = date(2026, 12, 31)
RANGO_DIAS   = (FECHA_FIN - FECHA_INICIO).days

def generar_fecha_aleatoria():
    """Devuelve una fecha aleatoria dentro del año 2026."""
    dias_aleatorios = random.randint(0, RANGO_DIAS)
    return FECHA_INICIO + timedelta(days=dias_aleatorios)

def generar_dataset():
    """Genera el archivo ventas.csv con datos simulados."""
    try:
        with open(RUTA_CSV, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo, delimiter=";")

            # Escribir encabezados
            writer.writerow(["producto", "cantidad_vendida", "precio", "fecha_de_venta"])

            # Generar registros
            for _ in range(CANTIDAD_REGISTROS):
                producto, precio = random.choice(PRODUCTOS)
                cantidad = random.randint(1, 20)
                fecha = generar_fecha_aleatoria()
                writer.writerow([producto, cantidad, precio, fecha])

        print(f"Dataset generado exitosamente: {RUTA_CSV}")
        print(f"Total de registros: {CANTIDAD_REGISTROS}")

    except OSError:
        print(f"Error: No se pudo crear el archivo en {RUTA_CSV}")
        print("Verificá que la carpeta /datos exista en el repositorio.")

# -------------------------------------------------------
# Punto de entrada
# -------------------------------------------------------
if __name__ == "__main__":
    generar_dataset()
