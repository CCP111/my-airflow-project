FROM apache/airflow:2.9.3

USER root

# Cài build tools (RẤT QUAN TRỌNG)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    libssl-dev \
    libffi-dev \
    && apt-get clean

USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r /requirements.txt
