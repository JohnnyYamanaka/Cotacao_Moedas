import requests


def call_api(dt_consulta: str):
    dt_consulta = dt_consulta
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{dt_consulta}'&$top=100&$format=json"

    print(dt_consulta)

    response = requests.get(url=url)
    result = response.json()

    return result
