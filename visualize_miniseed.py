import matplotlib.pyplot as plt
from obspy import read, UTCDateTime
import matplotlib.dates as mdates
import numpy as np

def graficar_mseed(archivo, intervalo_minutos=5, color=None):  # color ahora es None por defecto
    """
    Grafica un archivo MiniSEED con opciones de formato y color.

    Args:
        archivo (str): Ruta al archivo MiniSEED.
        intervalo_minutos (int): Intervalo en minutos para las marcas del eje x.
        color (str, optional): Color de la línea de la señal. Si es None, se usa el color por defecto de Matplotlib.
    """
    try:
        st = read(archivo)
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
        return

    if not st:
        print(f"El archivo {archivo} no contiene datos.")
        return

    tr = st[0]
    times = tr.times("matplotlib")
    data = tr.data

    fig, ax = plt.subplots(figsize=(12, 6))

    # Verificar si hay NaNs y graficar con manejo de gaps visuales
    if np.isnan(data).any():
        print("La traza contiene valores NaN. Se mostrarán como gaps en el gráfico.")
        masked_data = np.ma.masked_where(np.isnan(data), data)
        ax.plot(times, masked_data, linewidth=0.5, color=color) #color se usa solo si se especifica
    else:
        ax.plot(times, data, linewidth=0.5, color=color) #color se usa solo si se especifica

    # Formato del eje x (tiempo)
    minutes = mdates.MinuteLocator(interval=intervalo_minutos)
    minute_fmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_locator(minutes)
    ax.xaxis.set_major_formatter(minute_fmt)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    # Formato del gráfico
    ax.set_xlabel("Tiempo UTC (AAAA-MM-DD HH:MM:SS)")
    ax.set_ylabel("Amplitud")
    ax.set_title(f"Señal de {archivo} ({tr.stats.starttime.strftime('%Y-%m-%d')})")
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    archivo_mseed = "/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/MiniSEED_2025-01-14_09-29-53/c0add240625194443.pri0"

    #graficar_mseed(archivo_mseed, intervalo_minutos=10)        # Grafica con el color por defecto de Matplotlib (azul en la mayoria de los casos)
    graficar_mseed(archivo_mseed, intervalo_minutos=15, color='green')  # Grafica en verde
    #graficar_mseed(archivo_mseed, intervalo_minutos=5, color='#0080FF') #Grafica en azul claro con codigo hexadecimal
    #graficar_mseed(archivo_mseed, color='red') #Grafica en rojo con el intervalo por defecto de 5 minutos
