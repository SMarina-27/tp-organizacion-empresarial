Análisis de Ventas Simuladas 
TPN°2 Organización Empresarial con Git, GitHub y Jira
Integrantes del Equipo:
- Vargas, Silvia Marina (Hugo (P1) Líder  y Luis (P3) revisor): Creación del repositorio, estructura inicial, README.md y revisión final mediante Pull Request.
- Monzon, Dario Alexis (Paco (P2) Desarrollador Técnico): Desarrollo de los scripts Python: generador de datos simulados y análisis de ventas con gráfico mensual.

Escenario elegido

Escenario B: Análisis de Ventas de una Pequeña Empresa
Análisis de un conjunto de datos simulados de ventas comerciales para generar indicadores básicos que permitan interpretar el desempeño de la empresa.

Descripción del Dataset

Dataset simulado de ventas comerciales generado en Python. Contiene registros de ventas con información de producto, cantidad, precio y fecha. 
Archivo: datos/ventas.csv

Instrucciones para Ejecutar el Script
Requisito previo: instalar matplotlib
pip install matplotlib

En Google Colab
1.	Clonar el repositorio: 
!git clone https://github.com/SMarina-27/tp-organizacion-empresarial.git 
%cd tp-organizacion-empresarial
2.	Ejecutar el script: 
%run scripts/analisis_ventas.py
3.	Los resultados quedarán en la carpeta /resultados: 
•	grafico_ventas.png: es la imagen del gráfico de evolución de ventas mensuales
•	resultados.csv: es el archivo que genera el script con el resumen de ventas por mes y el total anual.
