import requests
import pandas as pd

#Funcion para conectar con API
def banco_mexico(token,serie,fecha_inicio,fecha_fin):
    serie= f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/{serie}/datos/{fecha_inicio}/{fecha_fin}"
    
    response=requests.get(serie, headers={"Bmx-Token": token})
    status=response.status_code 
    if status!=200:
        print("Error,codigo{}".format(status))
        return None
    raw_data=response.json()["bmx"]["series"][0]["datos"]
    dataframe=pd.DataFrame(raw_data)
    dataframe["fecha"]=pd.to_datetime(dataframe["fecha"], format="%d/%m/%Y")
    dataframe["dato"]=pd.to_numeric(dataframe["dato"])
    return dataframe

#Funcion para convertir las fechas en datatime para DF y convertir esas fechas en los indices del df
def convertirDF(dataframe):
    dataframe["fecha"]=pd.to_datetime(dataframe["fecha"])
    dataframe["dato"]=pd.to_numeric(dataframe["dato"])
    dataframe=dataframe.set_index("fecha")
    return dataframe
    
