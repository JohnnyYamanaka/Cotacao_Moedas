import sys
sys.path.append('/opt/airflow/plugins')

from datetime import datetime, timedelta
from time import sleep

from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
import pendulum

# from ..plugins import extract_data, transform
# from plugins import extract_data, transform
from plugins import extract_data, transform

local_tz = pendulum.timezone("America/Sao_Paulo")

@dag(
    start_date=pendulum.datetime(2025, 8, 25, tz=local_tz),
    # schedule="@daily",
    schedule_interval='0 0 * * 1-5',
    catchup=False
)
def get_dollar_dag():

    @task
    def extract(**kwargs):
        string_data_excecucao = datetime.strptime(kwargs['ds'], '%Y-%m-%d')
        data_excecucao = string_data_excecucao.strftime('%m-%d-%Y') 

        print('print dentro da dag',data_excecucao)
        return extract_data.call_api(data_excecucao)
    
    @task
    def transform_data(extracao):
        return transform.transform_data(extracao)
    

    extracao = extract()
    transformacao = transform_data(extracao)

    extracao >> transformacao

get_dollar_dag()
