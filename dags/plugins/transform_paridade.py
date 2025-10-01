import pandas as pd

def transform_paridade_moedas(dictonary: dict):
    result = dictonary['value']

    df_paridade = pd.json_normalize(result)

    return df_paridade