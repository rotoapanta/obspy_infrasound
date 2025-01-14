"""Plots MiniSEED files with formatting and color options.

This script reads a MiniSEED file, extracts time series data, and generates a plot using Matplotlib.
It handles NaN values by masking them, creating visual gaps.

**Requires:**
*   ObsPy (`pip install obspy`)
*   Matplotlib (`pip install matplotlib`)
*   NumPy (`pip install numpy`)

**Example:**
    To plot 'data.mseed' with a 10-minute interval and red color:
    #>>> plot_miniseed('data.mseed', interval_minutes=10, color='red')

    To plot with default settings:
    #>>> plot_miniseed('data.mseed')
"""

import matplotlib.pyplot as plt
from obspy import read
import matplotlib.dates as mdates
import numpy as np

def plot_miniseed(filepath, interval_minutes=5, color=None):
    """Plots a MiniSEED file.

    Args:
        filepath (str): Path to the MiniSEED file.
        interval_minutes (int, optional): Interval for x-axis ticks (minutes). Defaults to 5.
        color (str, optional): Line color. Defaults to Matplotlib's default.
    """
    try:
        st = read(filepath)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    if not st:
        print(f"{filepath} contains no data.")
        return

    tr = st[0]
    times = tr.times("matplotlib")
    data = tr.data

    fig, ax = plt.subplots(figsize=(12, 6))

    if np.isnan(data).any():
        print("Trace contains NaN values. Displaying as gaps.")
        masked_data = np.ma.masked_where(np.isnan(data), data)
        ax.plot(times, masked_data, linewidth=0.5, color=color)
    else:
        ax.plot(times, data, linewidth=0.5, color=color)

    # Format x-axis (time)
    minutes = mdates.MinuteLocator(interval=interval_minutes)
    minute_fmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_locator(minutes)
    ax.xaxis.set_major_formatter(minute_fmt)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    # Format plot
    ax.set_xlabel("UTC Time (YYYY-MM-DD HH:MM:SS)")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Signal from {filepath} ({tr.stats.starttime.strftime('%Y-%m-%d')})")
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    miniseed_file = "/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/MiniSEED_2025-01-14_09-29-53/c0add240625194443.pri0"
    # plot_miniseed(miniseed_file, interval_minutes=10)        # Grafica con el color por defecto de Matplotlib (azul en la mayoria de los casos)
    plot_miniseed(miniseed_file, interval_minutes=10, color='green')  # Grafica en verde
    # plot_miniseed(miniseed_file, interval_minutes=5, color='#0080FF') #Grafica en azul claro con codigo hexadecimal
    # plot_miniseed(miniseed_file, color='red') #Grafica en rojo con el intervalo por defecto de 5 minutos
