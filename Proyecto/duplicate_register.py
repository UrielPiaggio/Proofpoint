import pandas as pd


def date_meets(df):
    # Ceea 3 columnas mas de V o F si tiene ese dato correcto o no 
    
    df["valid_air_date"] = df["Air Date"].notna() & (df["Air Date"] != "Unknown")
    df["valid_title"] = df["Episode Title"] != "Untitled Episode"
    df["valid_season"] = df["Season Number"].notna() & df["Episode Number"].notna()
    
    return df
            
            
def dedup_episodios(data):
    df = data.copy()
    
    df = date_meets(df)
    order_df = df.sort_values(by=["Series Name", "Season Number"], ascending = [True,True])
    
    registros_finales = []
    vistos = set()
    cont = 0

    for i in range(len(order_df)):
        if i in vistos:
            continue

        fila_i = order_df.iloc[i]
        mejor = fila_i
        vistos.add(i)

        for j in range(i+1, len(order_df)):
            fila_j = order_df.iloc[j]

            # Si cambia la serie, cortamos
            if fila_i["Series Name"] != fila_j["Series Name"]:
                break

            # Condiciones de duplicado
            cond1 = (fila_i["Season Number"] == fila_j["Season Number"]) and \
                    (fila_i["Episode Number"] == fila_j["Episode Number"])

            cond2 = (fila_i["Season Number"] == 0 and fila_j["Season Number"] == 0) and \
                    (fila_i["Episode Number"] == fila_j["Episode Number"]) and \
                    (fila_i["Episode Title"] == fila_j["Episode Title"])

            cond3 = (fila_i["Episode Number"] == 0 and fila_j["Episode Number"] == 0) and \
                    (fila_i["Season Number"] == fila_j["Season Number"]) and \
                    (fila_i["Episode Title"] == fila_j["Episode Title"])

            if cond1 or cond2 or cond3:
                vistos.add(j)

                # Comparar prioridades directamente
                prioridad_mejor = (
                    mejor["valid_air_date"],
                    mejor["valid_title"],
                    mejor["valid_season"]
                )
                prioridad_j = (
                    fila_j["valid_air_date"],
                    fila_j["valid_title"],
                    fila_j["valid_season"]
                )
                
                #sumar al contador duplicaciones
                cont +=1

                # Si fila_j tiene mejor prioridad, reemplazar
                if prioridad_j > prioridad_mejor:
                    mejor = fila_j

        registros_finales.append(mejor)
        
        
    
    registros_finales = pd.DataFrame(registros_finales).reset_index(drop=True)  
    registros_finales.drop(columns=["valid_air_date", "valid_title", "valid_season"], inplace=True)
        
    


    return registros_finales, cont

        
    

    

    

    
    