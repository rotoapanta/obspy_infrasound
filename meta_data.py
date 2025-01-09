import obspy

# Leer el archivo MiniSEED
st = obspy.read("/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/datos_bnas_lahar/EC.BNAS..BHZ.D.2016.013")

# Obtener el primer trazo
tr = st[0]

# Imprimir la información del primer trazo
print(f"Código de estación (station): {tr.stats.station}")
print(f"Código de red (network): {tr.stats.network}")
print(f"Código de canal (channel): {tr.stats.channel}")
print(f"Código de ubicación (location): {tr.stats.location}")
print(f"Hora de inicio (starttime): {tr.stats.starttime}")
print(f"Hora de fin (endtime): {tr.stats.endtime}")
print(f"Sampling rate: {tr.stats.sampling_rate}")
print(f"Número de muestras (npts): {tr.stats.npts}")
