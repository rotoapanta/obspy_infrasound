import matplotlib.pyplot as plt
from obspy import read, UTCDateTime
import matplotlib.dates as mdates

def graficar_mseed(archivo, intervalo_minutos=5):
    """
    Grafica un archivo MiniSEED con opciones de formato.

    Args:
        archivo (str): Ruta al archivo MiniSEED.
        intervalo_minutos (int): Intervalo en minutos para las marcas del eje x.
    """
    try:
        st = read(archivo)
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
        return

    if not st:  # Verifica si el Stream está vacío
        print(f"El archivo {archivo} no contiene datos.")
        return

    tr = st[0]  # Obtiene el primer Trace del Stream
    times = tr.times("matplotlib")
    data = tr.data

    fig, ax = plt.subplots(figsize=(12, 6))  # Ajusta el tamaño de la figura para mejor visualización
    ax.plot(times, data, 'k-', linewidth=0.5)  # Grafica los datos con línea negra delgada

    # Formato del eje x (tiempo)
    minutes = mdates.MinuteLocator(interval=intervalo_minutos)
    minute_fmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')  # Formato más completo
    ax.xaxis.set_major_locator(minutes)
    ax.xaxis.set_major_formatter(minute_fmt)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")  # Rota las etiquetas para mejor legibilidad

    # Formato del gráfico
    ax.set_xlabel("Tiempo UTC (AAAA-MM-DD HH:MM:SS)")
    ax.set_ylabel("Amplitud")
    ax.set_title(f"Señal de {archivo} ({tr.stats.starttime.strftime('%Y-%m-%d')})")
    ax.grid(True, linestyle='--', alpha=0.5)  # Añade una grilla tenue
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    archivo_mseed = "/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/MiniSEED_2025-01-14_09-58-28/c0add240626154043.pri2"  # Reemplaza con la ruta correcta si es necesario
    graficar_mseed(archivo_mseed, intervalo_minutos=10) #Grafica con marcas cada minuto

    #Ejemplo de como graficar con otro intervalo
    #graficar_mseed(archivo_mseed, intervalo_minutos=15) #Grafica con marcas cada 15 minutos