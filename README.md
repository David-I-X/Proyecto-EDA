***Proyecto: Análisis de Acceso y Calidad del Servicio de Internet en Argentina***

**Descripción General**

Este proyecto tiene como objetivo analizar la penetración y calidad del servicio de internet en las diferentes provincias de Argentina. Utilizando un enfoque basado en KPIs (Key Performance Indicators), hemos desarrollado un dashboard interactivo que permite visualizar y comprender las tendencias y el desempeño del acceso a internet en el país.

El análisis se centra en tres KPIs principales, que miden el crecimiento del acceso, la penetración en hogares y la calidad del servicio de internet. Estos KPIs son cruciales para evaluar el impacto de las políticas públicas y las inversiones en infraestructura de telecomunicaciones.

**Contenido del Repositorio**

*El repositorio está organizado en varias carpetas y archivos, cada uno con un propósito específico:*

* /Internet.xlsx: Contiene los datasets utilizados en el análisis. Aquí se incluyen los datos de acceso a internet por velocidad, penetración en hogares y velocidad media de descarga (VMD) por provincia.

* /EDA: contiene lo notebook de Jupyter utilizados para realizar el análisis exploratorio de datos (EDA), el cálculo de los KPIs y la generación de las visualizaciones.

* /f-velocidadxprovincia: contiene las graficas del KPI 1.

* /f-Penetracion-Hogares.ipyn: contiene las graficas del KPI 2.

* /f-VMD.ipynb: contiene las graficas del KPI 3.

* dashboard_kpis_internet_argentina.py: Código fuente del dashboard.

* requirements.txt: Archivo que especifica las dependencias necesarias para ejecutar el dashboard.

* README.md: Este archivo, que proporciona una visión general del proyecto, la estructura del repositorio y un resumen del análisis realizado.

**Reporte de Análisis**

1. *KPI 1: Aumento del 2% en el Acceso a Internet por Provincia*

Este KPI mide el crecimiento proyectado del acceso a internet en el próximo trimestre. El análisis muestra que, en promedio, las provincias están cerca de alcanzar el objetivo del 2%, aunque algunas provincias requieren mayor atención para mejorar su infraestructura y accesibilidad.

2. *KPI 2: Crecimiento de la Penetración de Internet en Hogares por Provincia*

Este KPI permite observar el cambio en la penetración de internet en los hogares entre trimestres consecutivos. Las provincias con crecimiento negativo indican áreas donde se deben priorizar las mejoras en cobertura y accesibilidad.

3. *KPI 3: Índice de Calidad del Servicio de Internet por Provincia*

Este KPI combina la velocidad media de descarga con la proporción de accesos a velocidades superiores a 20 Mbps. El análisis revela que solo un número limitado de provincias ofrece un servicio de alta calidad a la mayoría de sus usuarios, lo que destaca la necesidad de continuar invirtiendo en la mejora de la infraestructura de red.

**Funcionalidad del Dashboard**

El dashboard interactivo permite a los usuarios explorar visualmente los tres KPIs definidos. A través de filtros y gráficos dinámicos, se puede analizar cómo varía el acceso a internet y su calidad en cada provincia, comparando trimestres y observando tendencias a lo largo del tiempo.

**Funcionalidades Clave:**

* Visualización de KPIs por provincia y trimestre.

* Análisis comparativo entre trimestres.

* Filtros interactivos para personalizar las vistas según el interés del usuario.

* Gráficos que permiten identificar rápidamente las provincias con mejor o peor desempeño.
