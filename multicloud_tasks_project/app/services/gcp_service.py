import os
import json
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'processed_data')

def get_gcp_data():
    path = os.path.join(PROCESSED_DATA_DIR, 'gcp_mock.json')
    with open(path, 'r') as f:
        raw_data = json.load(f)

    simulated_data = []

    for item in raw_data:
        # Exemplo: usar "disk_usage" ou "api_calls" se existir
        disk_usage = item.get("disk_usage", random.uniform(80, 1100))  # fallback
        api_calls = item.get("api_calls", random.randint(150, 5500))

        cpu_usage = round((api_calls % 85) + random.uniform(-3, 5), 2)
        billing = round(disk_usage * 0.22 + random.uniform(5, 20), 2)
        compliance_score = round(90 - (api_calls % 20) + random.uniform(-2, 4), 2)

        simulated_data.append({
            "cpu_usage": max(0, min(cpu_usage, 100)),
            "billing": max(0, billing),
            "compliance_score": max(0, min(compliance_score, 100))
        })

    return simulated_data
