from obspy import read

# Ruta al archivo MiniSEED
archivo = "/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/datos_bnas_lahar/EC.BNAS..BHZ.D.2016.013"

# Leer el archivo de datos
st = read(archivo)

# Filtrar la señal utilizando un filtro pasa-banda entre 1.0 Hz y 3.0 Hz.
# 'freqmin' establece la frecuencia mínima (1.0 Hz) y 'freqmax' la frecuencia máxima (3.0 Hz).
# 'corners' define el número de segmentos del filtro (4 en este caso, para un filtro de orden 4).
# 'zerophase' asegura que el filtro no introduce desfase en la señal (filtro de fase cero).
st.filter('bandpass', freqmin=1.0, freqmax=3.0, corners=4, zerophase=True)

# Graficar los datos de ObsPy utilizando 'dayplot' (gráfico por día).
# 'interval' controla el intervalo entre las marcas de tiempo en la gráfica (60 minutos en este caso).
# 'right_vertical_labels' si es True, agrega etiquetas en el eje Y a la derecha de la gráfica.
# 'vertical_scaling_range' ajusta el rango de amplitud en el eje Y. Se usa 5e3 como un valor de ejemplo.
# 'one_tick_per_line' asegura que haya una marca (tick) por cada línea de datos.
# 'color' especifica los colores para las trazas. ['k', 'r', 'b', 'g'] corresponde a negro, rojo, azul y verde.
# 'show_y_UTC_label' si es True, muestra las etiquetas UTC (hora en formato UTC) en el eje Y.
st.plot(type="dayplot", interval=60, right_vertical_labels=True, vertical_scaling_range=5e3,
        one_tick_per_line=True, color=['k', 'r', 'b', 'g'], show_y_UTC_label=True)
