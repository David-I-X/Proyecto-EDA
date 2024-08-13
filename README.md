Proyecto: Análisis de Acceso y Calidad del Servicio de Internet en Argentina
Descripción General
Este proyecto tiene como objetivo analizar la penetración y calidad del servicio de internet en las diferentes provincias de Argentina. Utilizando un enfoque basado en KPIs (Key Performance Indicators), hemos desarrollado un dashboard interactivo que permite visualizar y comprender las tendencias y el desempeño del acceso a internet en el país.

El análisis se centra en tres KPIs principales, que miden el crecimiento del acceso, la penetración en hogares y la calidad del servicio de internet. Estos KPIs son cruciales para evaluar el impacto de las políticas públicas y las inversiones en infraestructura de telecomunicaciones.

Contenido del Repositorio
El repositorio está organizado en varias carpetas y archivos, cada uno con un propósito específico:

/data: Contiene los datasets utilizados en el análisis. Aquí se incluyen los datos de acceso a internet por velocidad, penetración en hogares y velocidad media de descarga (VMD) por provincia.

accesos_por_velocidad.csv
penetracion_hogares.csv
totales_vmd.csv
/notebooks: Esta carpeta contiene los notebooks de Jupyter utilizados para realizar el análisis exploratorio de datos (EDA), el cálculo de los KPIs y la generación de las visualizaciones.

EDA_Access_Velocity.ipynb: Análisis exploratorio de los datos de accesos a internet por velocidad.
EDA_Penetracion_Hogares.ipynb: Análisis exploratorio de la penetración de internet en hogares.
EDA_VMD.ipynb: Análisis exploratorio de los datos de velocidad media de descarga.
/dashboard: Incluye los archivos necesarios para implementar el dashboard interactivo utilizando Streamlit.

dashboard.py: Código fuente del dashboard.
requirements.txt: Archivo que especifica las dependencias necesarias para ejecutar el dashboard.
/reports: Reportes generados a partir de los análisis realizados.

KPI_Analysis_Report.pdf: Reporte detallado del análisis de los KPIs.
Visualizations: Carpeta que contiene las visualizaciones generadas para el análisis.
README.md: Este archivo, que proporciona una visión general del proyecto, la estructura del repositorio y un resumen del análisis realizado.

Reporte de Análisis
1. KPI 1: Aumento del 2% en el Acceso a Internet por Provincia
Este KPI mide el crecimiento proyectado del acceso a internet en el próximo trimestre. El análisis muestra que, en promedio, las provincias están cerca de alcanzar el objetivo del 2%, aunque algunas provincias requieren mayor atención para mejorar su infraestructura y accesibilidad.

2. KPI 2: Crecimiento de la Penetración de Internet en Hogares por Provincia
Este KPI permite observar el cambio en la penetración de internet en los hogares entre trimestres consecutivos. Las provincias con crecimiento negativo indican áreas donde se deben priorizar las mejoras en cobertura y accesibilidad.

3. KPI 3: Índice de Calidad del Servicio de Internet por Provincia
Este KPI combina la velocidad media de descarga con la proporción de accesos a velocidades superiores a 20 Mbps. El análisis revela que solo un número limitado de provincias ofrece un servicio de alta calidad a la mayoría de sus usuarios, lo que destaca la necesidad de continuar invirtiendo en la mejora de la infraestructura de red.

Funcionalidad del Dashboard
El dashboard interactivo permite a los usuarios explorar visualmente los tres KPIs definidos. A través de filtros y gráficos dinámicos, se puede analizar cómo varía el acceso a internet y su calidad en cada provincia, comparando trimestres y observando tendencias a lo largo del tiempo.

Funcionalidades Clave:
Visualización de KPIs por provincia y trimestre.
Análisis comparativo entre trimestres.
Filtros interactivos para personalizar las vistas según el interés del usuario.
Gráficos que permiten identificar rápidamente las provincias con mejor o peor desempeño.
