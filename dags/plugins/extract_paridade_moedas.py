import requests
from datetime import datetime


def get_paridade(dt_consulta: str, moeda: str):
    dt_consulta = datetime.strptime(dt_consulta, "%Y%m%d")
    data_formatada = datetime.strftime(dt_consulta, "%m-%d-%Y")
    moeda = moeda

    print(f"Data da consulta: {data_formatada}")
    print(f"Moeda extraída: {moeda}")

    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='{moeda}'&@dataCotacao='{data_formatada}'&$top=100&$format=json"

    response = requests.get(url)
    result = response.json()

    return result
