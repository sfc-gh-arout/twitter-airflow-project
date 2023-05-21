from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from twitter_etl import run_twitter_etl

with DAG('Twitter_project', start_date = datetime(2023,5,21),schedule_interval=timedelta(days=1),catchup=False,default_args={
        "owner": 'ASIM-ROUT',
        "retries": 1,
        "retry_delay": timedelta(minutes=1),
        "retry_exponential_backoff": True,
        "max_retry_delay": timedelta(hours=2),
    },) as dag:

 run_dag_etl = PythonOperator(
            task_id = 'complete_twitter_etl',
            python_callable = run_twitter_etl
                            )

run_dag_etl
