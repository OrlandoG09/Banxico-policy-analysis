import requests
import pandas as pd


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

