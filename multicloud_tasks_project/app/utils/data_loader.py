import os
import pandas as pd
import json

# Define o diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# Define o diretório onde estão os datasets originais
DATASETS_DIR = os.path.join(BASE_DIR, 'datasets')
# Define o diretório onde os dados processados serão salvos
OUTPUT_DIR = os.path.join(BASE_DIR, 'processed_data')

# Função para processar o arquivo global_internet_usage.csv simulando a AWS
def load_and_process_aws():
    """Processa global_internet_usage.csv simulando a AWS"""
    path = os.path.join(DATASETS_DIR, 'global_internet_usage.csv')

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path)
    # Tratamento básico do dataframe (remoção de valores nulos)
    df = df.dropna()  # ou outro tratamento básico, se quiser

    output_path = os.path.join(OUTPUT_DIR, 'aws_mock.json')
    df.to_json(output_path, orient='records', indent=2)

# Função para processar o arquivo world_universities.csv simulando a GCP
def load_and_process_gcp():
    """Processa world_universities.csv simulando a GCP"""
    path = os.path.join(DATASETS_DIR, 'world_universities.csv')

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path, encoding='latin1')
    # Tratamento básico do dataframe (remoção de valores nulos)
    df = df.dropna()  # só tratamento básico

    output_path = os.path.join(OUTPUT_DIR, 'gcp_mock.json')
    df.to_json(output_path, orient='records', indent=2)

# Função para processar o arquivo large_cars.csv simulando a Azure
def load_and_process_azure():
    """Processa large_cars.csv simulando a Azure"""
    path = os.path.join(DATASETS_DIR, 'large_cars.csv')

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path)
    # Tratamento básico do dataframe (remoção de valores nulos)
    df = df.dropna()

    output_path = os.path.join(OUTPUT_DIR, 'azure_mock.json')
    df.to_json(output_path, orient='records', indent=2)
