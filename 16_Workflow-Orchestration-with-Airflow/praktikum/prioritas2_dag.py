import requests
import csv
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'dinda',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def get_data_from_api():
    response = requests.get('https://fakestoreapi.com/products')
    return response.json()

def write_to_csv(data):
    with open('/path/to/your/csv/file/products.csv', 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def write_to_txt(data):
    with open('/path/to/your/txt/file/products.txt', 'w') as txtfile:
        for item in data:
            txtfile.write(str(item) + '\n')

with DAG(
    dag_id='prioritas1no1',
    default_args=default_args,
    description='Prioritas 2',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1)
) as dag:

    get_data_from_api = PythonOperator(
        task_id='get_data_from_api',
        python_callable=get_data_from_api,
    )

    write_to_csv = PythonOperator(
        task_id='write_to_csv',
        python_callable=write_to_csv,
        op_args=[get_data_from_api.output],
    )

    write_to_txt = PythonOperator(
        task_id='write_to_txt',
        python_callable=write_to_txt,
        op_args=[get_data_from_api.output],
    )

    echo_done = BashOperator(
        task_id='echo_done',
        bash_command='echo "done!"',
    )

    get_data_from_api >> [write_to_csv, write_to_txt] >> echo_done
