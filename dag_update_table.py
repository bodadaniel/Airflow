
# Import the DAG object
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


# Define the default_args dictionary
default_args = {
  'owner': 'bdani',
  'start_date': datetime(2022, 11, 20, 11, 0, 0),
  'end_date': datetime(2022, 11, 22, 11, 0, 0),
  #'retries': 2,
  'schedule_interval':'32 * * * *',
}

# Instantiate the DAG object
etl_dag = DAG('update_table_etl', default_args=default_args)

#add python operator

bash_op = BashOperator(
    task_id='update_db',
    bash_command='python3 /home/daniel/airflow/airflowenv/lib/python3.10/site-packages/airflow/mypy/update_db_with_dt.py',
    dag=etl_dag)

