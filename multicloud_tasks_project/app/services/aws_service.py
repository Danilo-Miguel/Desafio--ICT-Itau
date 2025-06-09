import os
import json
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'processed_data')

def get_aws_data():
    path = os.path.join(PROCESSED_DATA_DIR, 'aws_mock.json')
    with open(path, 'r') as f:
        raw_data = json.load(f)

    simulated_data = []

    for item in raw_data:
        # Simulação baseada em alguns campos presentes, como "storage_used" ou "requests"
        storage = item.get("storage_used", random.uniform(100, 1000))  # valor de fallback
        requests = item.get("requests", random.randint(100, 5000))

        cpu_usage = round((requests % 100) + random.uniform(-5, 5), 2)
        billing = round(storage * 0.23 + random.uniform(0, 10), 2)
        compliance_score = round(100 - (requests % 30) + random.uniform(-2, 2), 2)

        simulated_data.append({
            "cpu_usage": max(0, min(cpu_usage, 100)),
            "billing": max(0, billing),
            "compliance_score": max(0, min(compliance_score, 100))
        })

    return simulated_data
