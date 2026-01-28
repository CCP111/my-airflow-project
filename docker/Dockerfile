FROM apache/airflow:2.9.3

USER root

# (tuỳ chọn) cài thêm lib OS
RUN apt-get update && apt-get install -y \
    vim \
    curl \
    && apt-get clean

USER airflow

# cài python lib
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

# copy DAGs
COPY ../dags /opt/my-airflow-project/dags



