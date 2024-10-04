from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def my_task():
    print("Hello, Airflow!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG('example_dag', default_args=default_args, schedule_interval='@daily')

run_my_task = PythonOperator(
    task_id='run_my_task',
    python_callable=my_task,
    dag=dag,
)
