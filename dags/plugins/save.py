import os
import json


def save_raw_data(nome_raiz:str, row_data:dict, dt_consulta):
    init = 'raw'
    timestamp = dt_consulta

    nome_pasta = '/opt/airflow/data/raw'

    extencao_arquivo = ".json"
    nome_base = nome_raiz   
    nome_arquivo = f'{init}-{nome_base}-{timestamp}{extencao_arquivo}'

    caminho_completo = os.path.join(nome_pasta, nome_arquivo)

    try:
        with open(caminho_completo, 'w') as file:
            json.dump(row_data, file)
        print('Arquivo salvo com sucesso')

    except IOError as e:
        print(f'Erro ao salvar o arquivo: {e}')

