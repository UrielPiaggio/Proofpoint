import pandas as pd
import re 


def null_Series_Name(data):
    ar = data[data["Series Name"].notna() & (data["Series Name"].str.strip() != "")]
    return ar


def is_numeric(data, val):
    data[val] = pd.to_numeric(data[val], errors= "coerce")
    
    data[val] = data[val].fillna(0)
    data.loc[data[val] < 0, val] = 0
    
    data[val] = data[val].astype(int)
    
    return data
    
    
    
def title_missing(data):
    set = "Episode Title"
    data[set] = data[set].fillna("Untitled Episode")
    
    data.loc[data[set].str.strip() == "", set] = "Untitled Episode"
    
    
    return data


def air_data_missing(data):
    set = "Air Date"
    data[set] = pd.to_datetime(data[set], errors= "coerce").dt.date
    data[set] = data[set].fillna("Unknown")
    #data.loc[set].astype(str).str.strip() == "","Air DAte"
    
    return data

def delete_regis(data):
    data = data.drop(data[
        (data["Episode Number"] == 0)&
        (data["Episode Title"] == "Untitled Episode") &
        (data["Air Date"] == "Unknown")                 
    ].index
    )
    
    return data

def clean_text_column(data, col):
    # Convertir a string y eliminar espacios extra
    data[col] = data[col].astype(str).str.strip()
    
    # Eliminar caracteres extraños (dejamos solo letras, números y espacios)
    data[col] = data[col].apply(lambda x: re.sub(r'[^A-Za-z0-9\s]', '', x))
    
    # Pasar a formato "Title Case" (primera letra de cada palabra en mayúscula)
    data[col] = data[col].str.title()
    
    # Eliminar espacios múltiples
    data[col] = data[col].apply(lambda x: re.sub(r'\s+', ' ', x))
    
    return data




    
    
    
    
    
    
    