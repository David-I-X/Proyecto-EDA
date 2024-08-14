import streamlit as st

# Configuración inicial del layout y tema
st.set_page_config(page_title="Dashboard Interactivo de KPI's del Internet en Argentina", layout="wide")

# Encabezado principal con formato
st.markdown("""
# **Presentación Interactiva de KPI's del Internet en Argentina** 📈
Este dashboard interactivo presenta tres KPI's clave relacionados con el estado del internet en Argentina. 
Navega por los diferentes KPI's para explorar las gráficas y análisis asociados. Utiliza el menú lateral para seleccionar y visualizar cada KPI.
""", unsafe_allow_html=True)

# Sidebar para la selección de KPI
st.sidebar.header("Selecciona un KPI:")
kpi = st.sidebar.selectbox(
    '',
    ('KPI 1: Acceso por Velocidad', 
     'KPI 2: Penetración-Hogares', 
     'KPI 3: Velocidad Media de Descarga')
)

# Mostrar contenido basado en la selección de KPI
if kpi == 'KPI 1: Acceso por Velocidad':
    st.header('📊 KPI 1: Acceso por Velocidad')
    st.markdown("""
    **Descripción**: Este KPI mide la distribución de accesos a internet por diferentes velocidades en las provincias de Argentina. 
    Las gráficas muestran la evolución de los accesos a lo largo del tiempo y la distribución por provincias.
    """)

    # Selección de la gráfica para mostrar
    grafico_kpi1 = st.selectbox(
        'Selecciona la gráfica para KPI 1',
        ('Accesos Actuales Proyectados por Provincias', 
         'Relación entre Accesos Actuales y el Incremento Absoluto', 
         'Mapa de Calor del Aumento')
    )
    
    if grafico_kpi1 == 'Accesos Actuales Proyectados por Provincias':
        st.image('f-accesoxvelocidad/accesos_actuales_proyectados.png', caption='Accesos Actuales Proyectados por Provincias')
        st.markdown("""
        **Uniformidad del Aumento**: La gráfica confirma que el aumento del 2% se aplicaría de manera uniforme en todas las provincias, independientemente del número inicial de accesos.
        **Consideraciones Estratégicas**: Las provincias con un mayor número de accesos actuales recibirán una mayor cantidad absoluta de nuevos accesos.
        """)
    
    elif grafico_kpi1 == 'Relación entre Accesos Actuales y el Incremento Absoluto':
        st.image('f-accesoxvelocidad/dispersión_accesos_incremento.png', caption='Relación entre Accesos Actuales y el Incremento Absoluto')
        st.markdown("""
        **Consistencia del KPI**: Esta gráfica refuerza la idea de que el aumento propuesto del 2% es uniforme y aplicado de manera equitativa a todas las provincias.
        **Simplicidad en la Interpretación**: El mapa de calor visualiza claramente que el aumento del 2% es homogéneo en todo el país.
        """)

    elif grafico_kpi1 == 'Mapa de Calor del Aumento':
        st.image('f-accesoxvelocidad/mapa_calor_aumento_accesos.png', caption='Mapa de Calor del Aumento de Accesos')
        st.markdown("""
        **Efecto Proporcional del KPI**: La gráfica confirma que el KPI de un aumento del 2% se distribuye proporcionalmente en función del número de accesos actuales.
        **Desigualdad Regional**: Las provincias más pequeñas podrían necesitar un enfoque más detallado para mejorar la infraestructura y aumentar los accesos.
        """)

elif kpi == 'KPI 2: Penetración-Hogares':
    st.header('📉 KPI 2: Penetración-Hogares')
    st.markdown("""
    **Descripción**: Este KPI mide el crecimiento intertrimestral de la penetración de internet en los hogares de cada provincia. 
    Permite observar la evolución del acceso a internet en los hogares, crucial para identificar tendencias y áreas que requieren atención.
    """)

    # Selección de la gráfica para mostrar
    grafico_kpi2 = st.selectbox(
        'Selecciona la gráfica para KPI 2',
        ('Crecimiento de la Penetración del Internet', 
         'Penetración Actual vs Anterior por Provincia', 
         'Mapa de Calor de la Penetración')
    )
    
    if grafico_kpi2 == 'Crecimiento de la Penetración del Internet':
        st.image('f-penetracion-hogares/Barras_penetracion.png', caption='Crecimiento de la Penetración del Internet')
        st.markdown("""
        **Provincias Destacadas**: Santa Cruz muestra un crecimiento notable, lo que podría estar vinculado a mejoras en infraestructura o políticas locales.
        **Identificación Rápida**: Este gráfico ayuda a identificar rápidamente provincias donde la penetración de internet está cambiando significativamente.
        """)

    elif grafico_kpi2 == 'Penetración Actual vs Anterior por Provincia':
        st.image('f-penetracion-hogares/lineas_actual_anterior.png', caption='Penetración Actual vs Anterior por Provincia')
        st.markdown("""
        **Visualización del Cambio**: Este gráfico permite ver cómo ha cambiado la penetración de internet de un trimestre a otro en cada provincia.
        **Tendencias y Cambios**: Útil para identificar tendencias y cambios a lo largo del tiempo, destacando áreas con crecimiento o estabilidad.
        """)

    elif grafico_kpi2 == 'Mapa de Calor de la Penetración':
        st.image('f-penetracion-hogares/mapa_calor_penetracion.png', caption='Mapa de Calor de la Penetración')
        st.markdown("""
        **Penetración por Regiones**: Muestra claramente la diferenciación entre provincias con alta y baja penetración de internet.
        **Identificación de Necesidades**: Útil para visualizar rápidamente las provincias con mayores y menores niveles de penetración, identificando áreas que requieren atención.
        """)

elif kpi == 'KPI 3: Velocidad Media de Descarga':
    st.header('🚀 KPI 3: Velocidad Media de Descarga')
    st.markdown("""
    **Descripción**: Este KPI evalúa la calidad del servicio de internet en cada provincia, combinando la Velocidad Media de Descarga (VMD) con el porcentaje de accesos a internet con velocidades superiores a 20 Mbps. Proporciona una visión clara de la calidad del servicio en diferentes regiones.
    """)

    # Selección de la gráfica para mostrar
    grafico_kpi3 = st.selectbox(
        'Selecciona la gráfica para KPI 3',
        ('Índice de Calidad por Provincia', 
         'Porcentaje de Accesos > 20mbps', 
         'Velocidad Media por Provincia')
    )
    
    if grafico_kpi3 == 'Índice de Calidad por Provincia':
        st.image('f-vmd/indice_de_calidad.png', caption='Índice de Calidad por Provincia')
        st.markdown("""
        **Áreas Destacadas**: Capital Federal y Buenos Aires destacan por su alta calidad de acceso a internet.
        **Desafíos de Infraestructura**: Provincias con un índice de calidad bajo podrían enfrentar desafíos en la infraestructura de internet.
        """)

    elif grafico_kpi3 == 'Porcentaje de Accesos > 20mbps':
        st.image('f-vmd/porcentaje_de_accesos.png', caption='Porcentaje de Accesos > 20mbps')
        st.markdown("""
        **Distribución por Tecnología**: Muestra la distribución actual de los accesos a internet por diferentes velocidades y tecnologías.
        **Enfoque en Alta Velocidad**: Útil para evaluar qué provincias ofrecen acceso a velocidades superiores a 20 Mbps.
        """)

    elif grafico_kpi3 == 'Velocidad Media por Provincia':
        st.image('f-vmd/velocidad_media_descarga.png', caption='Velocidad Media por Provincia')
        st.markdown("""
        **Disparidad Regional**: Hay una marcada desigualdad en la velocidad de internet entre diferentes regiones del país.
        **Necesidad de Inversiones**: Provincias con velocidades más bajas podrían beneficiarse de inversiones en infraestructura.
        **Variabilidad Interna**: Algunas provincias muestran una alta variabilidad interna en la velocidad de descarga.
        """)

# Conclusión final del dashboard
st.header('📝 Conclusión General sobre los Resultados y la Interpretación de los Datos')
st.markdown("""
El análisis global de los datos sobre acceso a internet y velocidad en Argentina revela una serie de tendencias significativas y disparidades regionales que son clave para entender el estado actual de la infraestructura de telecomunicaciones en el país.

**Incremento General en el Acceso a Internet:**

Existe un incremento uniforme del 2% en el acceso a internet en todas las provincias, lo que indica un progreso positivo en la expansión de la conectividad. Sin embargo, el impacto absoluto de este incremento varía considerablemente según la base de accesos actuales de cada provincia. Provincias con una base de accesos más grande, como Buenos Aires y Capital Federal, experimentan un mayor aumento absoluto, mientras que regiones como Catamarca y Santiago Del Estero muestran incrementos menores en términos absolutos.

**Desigualdades en la Velocidad y Calidad del Acceso:**

Se observa una marcada diferencia en la velocidad media de descarga entre provincias. Capital Federal y Buenos Aires lideran con velocidades significativamente altas, reflejando un acceso a internet de alta calidad. En contraste, provincias como Tucumán, Santa Fe y Santiago Del Estero tienen velocidades muy bajas, lo que sugiere una necesidad urgente de mejoras en la infraestructura.

**Penetración de Velocidades Superiores:**

El porcentaje de accesos con velocidades superiores a 20 Mbps ha aumentado considerablemente en los últimos años, pasando de ser casi insignificante a representar una proporción significativa en algunas provincias. Sin embargo, este avance no ha sido uniforme, con grandes diferencias entre regiones. Capital Federal presenta una alta penetración de estas velocidades, mientras que otras provincias aún están rezagadas.

**Índice de Calidad del Acceso a Internet:**

El índice de calidad, que combina la velocidad media de descarga y el porcentaje de accesos por encima de 20 Mbps, destaca aún más las disparidades regionales. Capital Federal y Buenos Aires tienen los índices de calidad más altos, indicando un acceso a internet robusto y eficiente. En cambio, provincias como Tucumán y Santiago Del Estero muestran índices muy bajos, subrayando la necesidad de intervenciones específicas para mejorar la calidad del acceso en estas áreas.

**Desafíos y Oportunidades:**

Aunque el incremento general en el acceso a internet es alentador, las disparidades en la velocidad y la calidad del acceso evidencian desafíos significativos. Para cerrar estas brechas, será crucial seguir invirtiendo en infraestructura, especialmente en las provincias más rezagadas. Además, un análisis más profundo de las razones detrás de las grandes diferencias en penetración y velocidad permitirá desarrollar estrategias más efectivas para mejorar el acceso a internet en todo el país.
""")

