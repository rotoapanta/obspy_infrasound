import obspy

# Leer los archivos MiniSEED
st = obspy.read("/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/MiniSEED_2025-01-14_09-30-40/c0add240731001425.pri0")
st += obspy.read("/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/MiniSEED_2025-01-14_09-30-40/c0add240731001425.pri1")
st += obspy.read("/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/MiniSEED_2025-01-14_09-30-40/c0add240731001425.pri2")

# Inspección inicial de gaps
print("Gaps iniciales en el Stream:")
st.print_gaps()

# Eliminar gaps rellenando con interpolación
st.merge(fill_value='interpolate')

# Inspección después de eliminar gaps
print("Gaps después de la interpolación:")
st.print_gaps()

# Guardar el Stream procesado
st.write("datos_sin_gaps.mseed_2", format="MSEED")

# Visualizar los trazos después de la limpieza
st.plot()
