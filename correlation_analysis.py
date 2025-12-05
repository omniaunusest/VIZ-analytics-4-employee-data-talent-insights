import pandas as pd
import numpy as np

# File path provided by the user
file_path = 'Análisis_y_transformación_datos/raw_data_limpio_2.csv'

try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Select only numeric columns for correlation analysis
    numeric_df = df.select_dtypes(include=np.number)

    # Calculate the correlation matrix
    corr_matrix = numeric_df.corr()

    # Unstack the matrix to create a Series of all correlation pairs
    corr_pairs = corr_matrix.unstack()

    # Filter out self-correlations (e.g., age with age)
    corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]

    # Filter for strong positive correlations (greater than 0.5) and less than 1
    strong_positive_corr = corr_pairs[(corr_pairs > 0.5) & (corr_pairs < 1)].sort_values(ascending=False)

    # Create a set to hold unique pairs to avoid duplicates (e.g., (age, salary) and (salary, age))
    unique_corr_pairs = set()
    
    print("Correlaciones positivas fuertes (> 0.5) encontradas:")

    if strong_positive_corr.empty:
        print("No se encontraron correlaciones positivas fuertes por encima de 0.5.")
    else:
        for (var1, var2), value in strong_positive_corr.items():
            # Create a sorted tuple to represent the pair canonically
            pair = tuple(sorted((var1, var2)))
            if pair not in unique_corr_pairs:
                print(f"- {var1} y {var2}: {value:.4f}")
                unique_corr_pairs.add(pair)

except FileNotFoundError:
    print(f"Error: El archivo no fue encontrado en la ruta '{file_path}'")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
