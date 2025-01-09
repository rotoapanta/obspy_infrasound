import obspy

# Leer el archivo MiniSEED
st = obspy.read("/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/datos_bnas_lahar/EC.BNAS..BHZ.D.2016.013")

# Recorrer cada trazo (trace) en el Stream
for tr in st:
    print("Código de estación (station):", tr.stats.station)
    print("Código de red (network):", tr.stats.network)
    print("Código de canal (channel):", tr.stats.channel)
    print("Código de ubicación (location):", tr.stats.location)
    print("Hora de inicio (starttime):", tr.stats.starttime)
    print("Hora de fin (endtime):", tr.stats.endtime)
    print("Sampling rate:", tr.stats.sampling_rate)
    print("Número de muestras (npts):", tr.stats.npts)
    print("------------------------------------------------------")
