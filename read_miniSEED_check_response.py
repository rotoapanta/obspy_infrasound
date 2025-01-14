"""
This script reads a MiniSEED data file and checks for sensor response information 
in the metadata.

**Input:**

* MiniSEED file path (replace with your actual file path)

**Output:**

* Prints the station channel and sensor sensitivity information (if available)
* Informs the user if the response information is missing from the file.

**Requirements:**

* ObsPy library (`pip install obspy`)

**Author:** Your Name (replace with your name)
**Date:** 2025-01-14
"""

from obspy import read


def print_sensor_info(filepath):
  """
  Reads a MiniSEED file, extracts channel information, and checks for sensor response data.

  Args:
      filepath (str): Path to the MiniSEED file.
  """
  try:
    st = read(filepath)
    tr = st[0]  # Assuming one Trace in the Stream

    print(f"Channel: {tr.stats.channel}")

    if "response" in tr.stats:
      if "sensitivity" in tr.stats.response:
        sensitivity = tr.stats.response["sensitivity"]
        print(f"Sensitivity: {sensitivity['value']} {sensitivity['input_units']} / {sensitivity['output_units']}")
      else:
        print("Sensitivity information not available in response metadata.")
    else:
      print("MiniSEED file does not contain response information.")

  except Exception as e:
    print(f"Error reading MiniSEED file: {e}")


if __name__ == "__main__":
  # Replace with the path to your actual MiniSEED file
  filepath = "/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/MiniSEED_2025-01-14_09-58-28/c0add240626154043.pri2"
  print_sensor_info(filepath)
