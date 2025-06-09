import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'processed_data')

def get_gcp_raw_data():
    path = os.path.join(PROCESSED_DATA_DIR, 'gcp_mock.json')
    with open(path, 'r') as f:
        return json.load(f)
