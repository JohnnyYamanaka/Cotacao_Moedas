import sys

sys.path.append("/opt/airflow/plugins")

from datetime import datetime, timedelta
from time import sleep

from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator, get_current_context
import pendulum

# from ..plugins import extract_data, transform
# from plugins import extract_data, transform
from plugins import extract_data
from plugins.save import save_raw_data
from plugins.transform_usd import transform_data

local_tz = pendulum.timezone("America/Sao_Paulo")


@dag(
    start_date=pendulum.datetime(2025, 8, 1, tz=local_tz),
    # schedule="@daily",
    schedule_interval="0 0 * * 1-5",
    catchup=True,
)
def get_dollar_dag():
    @task
    def get_ds_dash():
        contex = get_current_context()
        return contex["ds_nodash"]

    @task
    def extract(**kwargs):
        string_data_excecucao = datetime.strptime(kwargs["ds"], "%Y-%m-%d")
        data_excecucao = string_data_excecucao.strftime("%m-%d-%Y")

        raw = extract_data.call_api(data_excecucao)
        print("print dentro da dag", data_excecucao)
        return raw

    @task
    def save_data(row_data, dt_consulta, nome_raiz="USD"):
        # nome_arquivo = f'{nome_raiz}_{dt_consulta}'
        save_raw_data(nome_raiz, row_data, dt_consulta)

    @task
    def transform_currency_usd(extracao):
        return transform_data(extracao)
    
    raw = extract()
    ds = get_ds_dash()
    save_raw = save_data(raw, ds)
    transformacao = transform_currency_usd(raw)

    ds >> raw >> [save_raw, transformacao]


get_dollar_dag()
