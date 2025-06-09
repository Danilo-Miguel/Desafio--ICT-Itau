import os
import json
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'processed_data')

def get_azure_data():
    path = os.path.join(PROCESSED_DATA_DIR, 'azure_mock.json')
    with open(path, 'r') as f:
        raw_data = json.load(f)

    simulated_data = []

    for item in raw_data:
        # Exemplo: usar "storage_allocated" ou "transactions" se existir
        storage = item.get("storage_allocated", random.uniform(150, 1200))  # fallback
        transactions = item.get("transactions", random.randint(200, 6000))

        cpu_usage = round((transactions % 90) + random.uniform(-4, 4), 2)
        billing = round(storage * 0.25 + random.uniform(0, 15), 2)
        compliance_score = round(95 - (transactions % 25) + random.uniform(-3, 3), 2)

        simulated_data.append({
            "cpu_usage": max(0, min(cpu_usage, 100)),
            "billing": max(0, billing),
            "compliance_score": max(0, min(compliance_score, 100))
        })

    return simulated_data
