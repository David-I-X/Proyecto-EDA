import streamlit as st

# Título principal
st.title('Presentación Interactiva de KPI\'s del Internet en Argentina')
st.markdown("""
Este dashboard interactivo presenta tres KPI's clave relacionados con el estado del internet en Argentina. 
Navega por los diferentes KPI's para explorar las gráficas y análisis asociados.
""")

# Selección de KPI en el menú lateral
kpi = st.sidebar.selectbox(
    'Selecciona el KPI que deseas visualizar',
    ('KPI 1: Acceso por Velocidad', 
     'KPI 2: Penetracion-Hogares', 
     'KPI 3: Velocidad Media de Descarga')
)

# Mostrar contenido basado en la selección
if kpi == 'KPI 1: Acceso por Velocidad':
    st.header('KPI 1: Acceso por Velocidad')
    st.markdown("""
    **Descripción**: Este KPI mide el porcentaje de hogares con acceso a internet en diferentes provincias de Argentina. 
    Las gráficas muestran la evolución de la penetración de internet a lo largo del tiempo y la comparación entre provincias.
    """)

    # Seleccionar la gráfica para mostrar
    grafico_kpi1 = st.selectbox(
        'Selecciona la gráfica para KPI 1',
        ('Accesos Actuales Proyectados por Provincias', 
         'Relacion entre Accesos Actuales y el Incremento Absoluto', 
         'Mapa de Calor del Aumento')
    )
    
    if grafico_kpi1 == 'Accesos Actuales Proyectados por Provincias':
        st.image('f-accesoxvelocidad\\accesos_actuales_proyectados.png', caption='Evolución Temporal de la Penetración de Internet')
        st.write('**Uniformidad del Aumento:** La gráfica confirma que el aumento del 2% se aplicaría de manera uniforme en todas las provincias, independientemente del número inicial de accesos.**Consideraciones Estratégicas:** Dado que el aumento es pequeño, pero proporcional, las provincias con un gran número de accesos actuales recibirán una mayor cantidad absoluta de nuevos accesos. Sin embargo, para alcanzar el KPI en provincias con menos accesos, puede ser necesario implementar estrategias específicas, como mejorar la infraestructura o incentivar la adopción de servicios de internet.'
                 )
    
    elif grafico_kpi1 == 'Relacion entre Accesos Actuales y el Incremento Absoluto':
        st.image('f-accesoxvelocidad\dispersión_accesos_incremento.png', caption='Comparación de Penetración de Internet entre Provincias')
        st.write('**Consistencia del KPI:** Esta gráfica refuerza la idea de que el aumento propuesto del 2% es uniforme y aplicado de manera equitativa a todas las provincias, sin distinción de la cantidad de accesos actuales.**Simplicidad en la Interpretación:** El mapa de calor visualiza claramente que el aumento del 2% es homogéneo en todo el país, lo que facilita la interpretación y justifica la uniformidad de la implementación del KPI.'
                 )
    
    elif grafico_kpi1 == 'Mapa de Calor del Aumento':
        st.image('f-accesoxvelocidad\mapa_calor_aumento_accesos.png', caption='Distribución de la Penetración de Internet por Provincia')
        st.write('**Efecto Proporcional del KPI:** La gráfica confirma que el KPI de un aumento del 2% se distribuye proporcionalmente en función del número de accesos actuales. Esto es una indicación de que el KPI es escalable y adaptable a provincias de diferentes tamaños. **Desigualdad Regional:** Las provincias más pequeñas en términos de accesos pueden necesitar un enfoque más detallado para mejorar la infraestructura y aumentar los accesos a un ritmo más rápido en el futuro, ya que su crecimiento absoluto es menor.'
                 )

elif kpi == 'KPI 2: Penetracion-Hogares':
    st.header('KPI 2:Penetracion-Hogares')
    st.markdown("""
    **Descripción**: Este KPI mide el crecimiento intertrimestral de la penetración de internet en los hogares de cada provincia. Permite observar cómo ha evolucionado el acceso a internet en los hogares, lo que es crucial para identificar tendencias y áreas que requieren atención.
    """)

    # Seleccionar la gráfica para mostrar
    grafico_kpi2 = st.selectbox(
        'Selecciona la gráfica para KPI 2',
        ('Crecimiento de la Penetracion del Internet', 
         'Penetracion Actual vs Anterior por Provincia', 
         'Mapa de Calor de la Penetracion')
    )
    
    if grafico_kpi2 == 'Crecimiento de la Penetracion del Internet':
        st.image('f-penetracion-hogares\Barras_penetracion.png', caption='Evolución de la Velocidad Media de Descarga')
        st.write('Este gráfico resalta de manera clara las provincias que experimentan un crecimiento destacado, siendo Santa Cruz la más notable. Este crecimiento podría estar vinculado a una mejora en las políticas locales, en la infraestructura o en la adopción de servicios de internet, lo que merece un análisis más detallado. Este gráfico es útil para identificar rápidamente las provincias donde la penetración de internet está cambiando de manera significativa, lo que puede ayudar a tomar decisiones informadas sobre dónde enfocar recursos y esfuerzos.'
                 )
        
    elif grafico_kpi2 == 'Penetracion Actual vs Anterior por Provincia':
        st.image('f-penetracion-hogares\lineas_actual_anterior.png', caption='Distribución de la Velocidad de Descarga')
        st.write('Este gráfico es útil para visualizar rápidamente cómo ha cambiado la penetración de internet de un trimestre a otro en cada provincia. Mientras que la mayoría de las provincias han mantenido niveles de penetración relativamente estables, hay algunas excepciones notables, especialmente en Santa Cruz, donde se ha producido un aumento significativo en la penetración de internet. Este tipo de gráfico es útil para identificar tendencias y cambios a lo largo del tiempo y puede ayudar a identificar áreas donde se han realizado mejoras o donde se requiere atención adicional.'
                 )
        
    elif grafico_kpi2 == 'Mapa de Calor de la Penetracion':
        st.image('f-penetracion-hogares\mapa_calor_penetracion.png', caption='Comparación de la Velocidad Media entre Provincias')
        st.write('La mayoría de las provincias se encuentran en el rango medio (60%-90%), lo cual sugiere una penetración moderada en la mayor parte del país. Sin embargo, hay una clara diferenciación entre provincias con una penetración alta (azul oscuro) y aquellas con una penetración baja (amarillo claro). Este mapa de calor es muy útil para identificar rápidamente las provincias con los mayores y menores niveles de penetración de internet, así como para visualizar de manera clara los cambios entre trimestres. Es evidente que las provincias más urbanizadas o con mejor infraestructura (como Capital Federal y Tierra del Fuego) tienen mayores niveles de penetración, mientras que las provincias más rurales o menos desarrolladas (como Formosa y Chaco) presentan niveles más bajos.'
                 )

elif kpi == 'KPI 3: Velocidad Media de Descarga':
    st.header('KPI 3: Velocidad Media de Descarga')
    st.markdown("""
    **Descripción**:  Este KPI evalúa la calidad del servicio de internet en cada provincia, combinando la Velocidad Media de Descarga (VMD) con el porcentaje de accesos a internet con velocidades superiores a 20 Mbps. Esto proporciona una visión clara de cuántos usuarios disfrutan de un servicio de alta calidad.
 """)

    # Seleccionar la gráfica para mostrar
    grafico_kpi3 = st.selectbox(
        'Selecciona la gráfica para KPI 3',
        ('Indice de Calidad por Provincia', 
         'Porcentaje de Accesos > 20mbps', 
         'Velocidad Media por Provincia')
    )
    
    if grafico_kpi3 == 'Indice de Calidad por Provincia':
        st.image('f-vmd\indice_de_calidad.png', caption='Evolución de Accesos por Tecnología')
        st.write('Capital Federal y Buenos Aires están destacando como las áreas con mejor calidad de acceso a internet, lo que es coherente con su desarrollo urbano y tecnológico. Las provincias con un índice de calidad bajo podrían estar enfrentando desafíos en la infraestructura de internet, lo que afecta tanto la velocidad de conexión como el acceso a velocidades más altas. Esta información es crucial para identificar áreas donde se necesita mejorar la infraestructura de internet, especialmente en las provincias con índices de calidad más bajos.'
                 )
        
    elif grafico_kpi3 == 'Porcentaje de Accesos > 20mbps':
        st.image('f-vmd\porcentaje_de_accesos.png', caption='Distribución de Accesos por Tecnología')
        st.write('Distribución actual de los accesos a internet por diferentes tecnologías.'
                 )
        
    elif grafico_kpi3 == 'Velocidad Media por Provincia':
        st.image('f-vmd\\velocidad_media_descarga.png', caption='Comparación de Accesos entre Tecnologías')
        st.write('**Disparidad en la Infraestructura de Internet:** La gráfica indica que hay una marcada desigualdad en la velocidad de internet entre diferentes regiones del país, con provincias como Capital Federal y Buenos Aires liderando significativamente. **Necesidad de Mejora en Provincias Rezagadas:** Provincias con velocidades más bajas, como Chubut y Santa Cruz, podrían beneficiarse de inversiones en infraestructura para mejorar la velocidad de internet. **Variabilidad Interna:** En algunas provincias, como Buenos Aires, existe una alta variabilidad interna en la velocidad de descarga, lo que podría estar relacionado con diferencias socioeconómicas o urbanización desigual. Esta información es esencial para las políticas públicas y las estrategias empresariales orientadas a mejorar la infraestructura de telecomunicaciones en las regiones con menor velocidad de internet en Argentina.'
                 )

# Conclusión
st.header('Conclusión')
st.markdown("""
En resumen, este dashboard proporciona una visión clara de la evolución y el estado actual del internet en Argentina, 
abarcando la penetración, la velocidad media de descarga, y los accesos por tecnología. Las gráficas interactivas 
permiten explorar diferentes aspectos de cada KPI y comparar resultados entre provincias y tecnologías.
""")
