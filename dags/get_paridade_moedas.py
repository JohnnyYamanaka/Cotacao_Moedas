from datetime import datetime

from airflow.decorators import dag, task
from airflow.operators.python import get_current_context

import pendulum

from plugins.extract_paridade_moedas import get_paridade
from plugins.save import save_raw_data
from plugins.transform_paridade import transform_paridade_moedas

local_tz = pendulum.timezone("America/Sao_Paulo")


@dag(
    start_date=pendulum.datetime(2025, 8, 1, tz=local_tz),
    schedule_interval="0 0 * * 1-5",
    catchup=True,
)
def get_paridade_moeda_dag():
    @task
    def get_ds_dash():
        context = get_current_context()
        return context["ds_nodash"]

    @task
    def gerar_lista_moedas():
        return ["EUR", "GBP", "JPY"]

    @task
    def extract(moeda, data_consulta):
        raw = get_paridade(dt_consulta=data_consulta, moeda=moeda)
        return raw

    @task
    def save_data(row_data, dt_consulta, nome_raiz):
        save_raw_data(nome_raiz, row_data, dt_consulta)

    @task
    def transform_moedas(extracao):
        return transform_paridade_moedas(extracao)

    lista_moedas = gerar_lista_moedas()
    data_execucao = get_ds_dash()
    # parametros = montar_parametros(moeda=lista_moedas, dt_consulta=data_execucao)
    extracao = extract.partial(data_consulta=data_execucao).expand(moeda=lista_moedas)
    save = save_data.partial(dt_consulta=data_execucao).expand(
        row_data=extracao, nome_raiz=lista_moedas
    )
    transform = transform_moedas.expand(extracao=extracao)

    # [lista_moedas, data_execucao] >> extracao >> [save, transform]


get_paridade_moeda_dag()
