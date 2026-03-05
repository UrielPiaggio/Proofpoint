import pandas as pd
import clear_pd as cle

def read_csv(ar):
    
    df = pd.read_csv(ar)
    
    return df
    
    

file_pd = read_csv("cosas.csv")


clearing_pd = file_pd.copy()


#elimando nombre de serie nulo
clearing_pd = cle.null_Series_Name(clearing_pd)

#seteando valores de season number
set = "Season Number"
clearing_pd = cle.is_numeric(clearing_pd, set)

#seteando valores de Episode Number

set = "Episode Number"
clearing_pd = cle.is_numeric(clearing_pd, set)

#seteando Episode Title 

clearing_pd = cle.title_missing(clearing_pd)


#seteando Air Date

clearing_pd = cle.air_data_missing(clearing_pd)

# Eliminando registros sin informacion

clearing_pd = cle.delete_regis(clearing_pd)


clearing_pd = cle.clean_text_column(clearing_pd, "Series Name")

clearing_pd = cle.clean_text_column(clearing_pd, "Episode Title")

#print(clearing_pd.isnull().sum())
print(clearing_pd.tail(30)) #177




 








