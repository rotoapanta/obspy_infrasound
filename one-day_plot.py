from obspy import read

# Ruta al archivo MiniSEED
archivo = "/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/datos_bnas_lahar/EC.BNAS..BHZ.D.2016.013"

# Leer el archivo de datos
st = read(archivo)
#st.filter("lowpass", freq=0.1, corners=2)
st.filter('bandpass', freqmin=1.0, freqmax=3.0, corners=4, zerophase=True)

# Graficar los datos
#st.plot(type="dayplot", interval=60, right_vertical_labels=False, vertical_scaling_range=5e3,
#        one_tick_per_line=True, color=['k', 'r', 'b', 'g'], show_y_UTC_label=False,
#        events={'min_magnitude': 4.5})


st.plot(type="dayplot", interval=60, right_vertical_labels=False, vertical_scaling_range=5e3,
        one_tick_per_line=True, color=['k', 'r', 'b', 'g'], show_y_UTC_label=True)
