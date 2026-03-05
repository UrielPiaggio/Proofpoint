import pandas as pd
import clear_pd as cle
import duplicate_register as dupli 
import report as repo


def read_csv(ar):
    
    df = pd.read_csv(ar)
    
    return df
    

def main ():
    #Cargar ruta del archivo a digitalizar 
    file_pd = read_csv("patch.csv")
    #creamos una copia del DtaFrame para no modificar los datos 
    clear_pd = file_pd.copy()

    
    #Comenzamos a limpiar 
    
    #Primero eliminamos los Serie Name
    no_name_pd = cle.null_Series_Name(clear_pd)
    
    #seteando valores de season number
    set = "Season Number"
    seteo_pd= cle.is_numeric(no_name_pd, set)

    #seteando valores de Episode Number

    set = "Episode Number"
    seteo_pd = cle.is_numeric(seteo_pd, set)

    #seteando Episode Title 

    seteo_pd = cle.title_missing(seteo_pd)
    
    #seteando Air Date

    seteo_pd = cle.air_data_missing(seteo_pd)
    
    # Eliminando registros sin informacion

    no_empty_records_pd = cle.delete_regis(seteo_pd)

    #Estructuando datos
    structed_pd = cle.clean_text_column(no_empty_records_pd, "Series Name")

    structed_pd = cle.clean_text_column(structed_pd, "Episode Title")
    
    #reseteando indice 
   
    
    corrected_entries = repo.number_corrected_entries(file_pd, structed_pd)
    structed_pd = structed_pd.reset_index(drop = True)
    
    #Eliminando duplicados
    
    df_no_duplicate, duplicates = dupli.dedup_episodios(structed_pd)
    
    # metricas
    
    total_origin = len(file_pd)
    total_out = len(df_no_duplicate)
    discarded_entries = total_origin - total_out
    
    
    #Creando reportes 
    
    metrics = {
        "Total number of input records: " :total_origin, 
        "Total number of output records: " :total_out,
        "Number of discarded entries: "  :discarded_entries,
        "Number of corrected entries: " :corrected_entries,
        "Number of duplicates detected: " : duplicates, 
        "Explanation of the deduplication strategy: ": 
            """ \n\tThe deduplication strategy I implemented was developed in several stages.\n
                First, I created three auxiliary columns (valid_air_date, valid_title, valid_season) to validate the quality of the data according to a defined priority list.\
                Then, I ordered the dataset by Season Name and Season Number to maintain a coherent structure.\n
                Next, I performed a sequential search for duplicate episodes. When a duplicate was found, 
                I checked whether it met the validation conditions defined in the priority table.\n
                Valid records were stored in a new vector, and I also maintained a counter to track how many duplicates were detected.\n
                Finally, I transformed the deduplicated vector into a pandas DataFrame, 
                which allowed me to continue the data cleaning and analysis in a structured way."""  
    }
    
    repo.write_csv(df_no_duplicate)
    
    repo.write_md(metrics)




if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    

    
    
    
     
    
    












 








