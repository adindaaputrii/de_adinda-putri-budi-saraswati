import random
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'dinda',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def generate_random_numbers():
    random_numbers = [random.randint(1, 50) for _ in range(25)]
    return random_numbers
   
def calculate_sum(numbers):
    return sum(numbers)

def check_even_sum(sum_result):
    if sum_result % 2 == 0:
        return "Even Sum"
    else:
        return "Odd Sum"

with DAG(
    dag_id='prioritas1no1',
    default_args=default_args,
    description='Prioritas 1 No 2',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1, 2)
) as dag:

    generate_numbers = PythonOperator(
        task_id='generate_random_numbers',
        python_callable=generate_random_numbers,
    )

    calculate_sum = PythonOperator(
        task_id='calculate_sum',
        python_callable=calculate_sum,
        op_args=[],
        op_kwargs={'numbers': '{{ task_instance.xcom_pull(task_ids="generate_random_numbers") }}'},
    )

    check_even = PythonOperator(
        task_id='check_even_sum',
        python_callable=check_even_sum,
        op_args=[],
        op_kwargs={'sum_result': '{{ task_instance.xcom_pull(task_ids="calculate_sum") }}'},
    )

    generate_numbers >> calculate_sum >> check_even