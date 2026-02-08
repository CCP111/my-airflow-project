from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime

with DAG(
    dag_id="k8s_test",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task = KubernetesPodOperator(
        name="hello",
        task_id="hello",
        image="python:3.9",
        cmds=["python", "-c"],
        arguments=["print('Hello from K8s Executor')"],
    )
