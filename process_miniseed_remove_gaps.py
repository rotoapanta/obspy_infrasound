"""
This script processes MiniSEED files to remove gaps by interpolation and saves the
processed files to a new directory.

**Input:**

*   Directory containing MiniSEED files (.pri0, .pri1, .pri2 extensions).

**Output:**

*   Directory containing processed MiniSEED files with gaps removed (_sin_gaps.mseed suffix).
*   Prints information about initial and post-interpolation gaps for each file.

**Requirements:**

*   ObsPy library (`pip install obspy`)

**Author:** Your Name (Replace with your actual name)
**Date:** 2025-01-14 (Adapt to the current date)
"""

import os
import obspy

def process_miniseed_files(input_folder, output_folder):
    """
    Processes MiniSEED files to remove gaps by interpolation.

    Args:
        input_folder (str): Path to the directory containing input MiniSEED files.
        output_folder (str): Path to the directory where processed files will be saved.
    """

    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Get list of MiniSEED files with specified extensions
        files = [f for f in os.listdir(input_folder) if f.endswith((".pri0", ".pri1", ".pri2"))]

        if not files:
            print(f"No .pri0, .pri1, or .pri2 files found in {input_folder}")
            return

        # Process each file
        for file in files:
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}_sin_gaps.mseed")

            try:
                st = obspy.read(input_file)

                print(f"Processing file: {file}")

                # Check if the stream is empty before processing
                if not st:
                    print(f"Warning: Stream is empty for file {file}. Skipping.")
                    continue

                print("Initial gaps in the Stream:")
                st.print_gaps()

                # Remove gaps by interpolation
                st.merge(fill_value='interpolate', method=1) # Usar method=1 para forzar la union

                print("Gaps after interpolation:")
                st.print_gaps()

                # Write the processed file
                st.write(output_file, format="MSEED")
                print(f"Processed file saved to: {output_file}\n")

            except obspy.core.inventory.inventory.InventoryError as e:
                print(f"Error reading inventory (station information) for file {file}: {e}. Skipping file.")
                continue #Salta al siguiente archivo
            except obspy.core.trace.Trace.StatsMissingFieldError as e:
                print(f"Error missing stats field for file {file}: {e}. Skipping file.")
                continue
            except Exception as e:
                print(f"Error processing file {file}: {e}")

    except FileNotFoundError:
        print(f"Error: Input folder '{input_folder}' not found.")
    except Exception as e:
        print(f"A general error occurred: {e}")

    print("File processing completed.")

if __name__ == "__main__":
    input_folder = "/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/MiniSEED_2025-01-14_09-30-40/"
    output_folder = "/home/rotoapanta/Documentos/DiGOS/DTA_CEDIA/MiniSEED_procesados_gemini/"
    process_miniseed_files(input_folder, output_folder)