import pandas as pd


    
    
def number_corrected_entries(origin, cleaned):
    # Alinear columnas comunes
    origin, cleaned = origin.align(cleaned, join="inner")
    
    # Convertir todo a string para comparar de forma uniforme
    origin = origin.astype(str)
    cleaned = cleaned.astype(str)
    
    # Detectar cambios
    changes = origin != cleaned
    
    # Contar celdas distintas
    corrected_entries = changes.sum().sum()
    
    return  corrected_entries
    
    
def write_csv (df_csv):
    df_csv.to_csv("episodes_clean.csv", index = False)
    print("created successful...")
    

def write_md (mat):
    with open("metrics.md", "w") as f:
        f.write("#Data Cleaning Metrics\n\n")
        for i , v in mat.items():
            f.write(f"- {i}{v}\n")
    
    print("created successful...")
    
    
