import os
import json

# Define o diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# Define o diretório onde estão os dados processados
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'processed_data')

# Função para obter os dados crus da AWS a partir de um arquivo JSON
def get_aws_raw_data():
    path = os.path.join(PROCESSED_DATA_DIR, 'aws_mock.json')  
    with open(path, 'r') as f:
        return json.load(f)  
