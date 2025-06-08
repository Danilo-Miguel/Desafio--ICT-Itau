import os
import pandas as pd
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATASETS_DIR = os.path.join(BASE_DIR, 'datasets')
OUTPUT_DIR = os.path.join(BASE_DIR, 'processed_data')


def load_and_process_aws():
    """Processa global_internet_usage.csv simulando a AWS"""
    path = os.path.join(DATASETS_DIR, 'global_internet_usage.csv')

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path)
    # Aqui só tratar o dataframe sem transformar em métricas
    df = df.dropna()  # ou outro tratamento básico, se quiser

    output_path = os.path.join(OUTPUT_DIR, 'aws_mock.json')
    df.to_json(output_path, orient='records', indent=2)


def load_and_process_gcp():
    """Processa world_universities.csv simulando a GCP"""
    path = os.path.join(DATASETS_DIR, 'world_universities.csv')

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path, encoding='latin1')
    df = df.dropna()  # só tratamento básico

    output_path = os.path.join(OUTPUT_DIR, 'gcp_mock.json')
    df.to_json(output_path, orient='records', indent=2)


def load_and_process_azure():
    """Processa large_cars.csv simulando a Azure"""
    path = os.path.join(DATASETS_DIR, 'large_cars.csv')

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path)
    df = df.dropna()

    output_path = os.path.join(OUTPUT_DIR, 'azure_mock.json')
    df.to_json(output_path, orient='records', indent=2)
