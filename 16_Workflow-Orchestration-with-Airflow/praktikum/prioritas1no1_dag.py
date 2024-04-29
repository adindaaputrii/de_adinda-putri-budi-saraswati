import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'dinda',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='prioritas1no1',
    default_args=default_args,
    description='Prioritas 1 No 1',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1, 2)
) as dag:

    task1 = BashOperator(
        task_id='echo_hello_airflow',
        bash_command='echo "hello airflow"',
    )

    task2 = BashOperator(
        task_id='mkdir_about_us',
        bash_command='mkdir -p about_us',
    )

    task3 = BashOperator(
        task_id='touch_about_us_about.txt',
        bash_command='touch about_us/about.txt',
    )

    task4 = BashOperator(
        task_id='mkdir_our_works',
        bash_command='mkdir -p our_works',
    )

    task5 = BashOperator(
        task_id='touch_our_works_about.txt',
        bash_command='touch our_works/about.txt',
    )

    task6 = BashOperator(
        task_id='echo_done',
        bash_command='echo "done"',
    )

    task1 >> [task2, task4]
    task2 >> task3 >> task6
    task4 >> task5 >> task6
