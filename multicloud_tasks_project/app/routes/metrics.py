from flask import Blueprint, jsonify
from app.services.aws_service import get_aws_raw_data
from app.services.azure_service import get_azure_raw_data
from app.services.gcp_service import get_gcp_raw_data
from flasgger.utils import swag_from
import random

# Cria um blueprint para as rotas de métricas
metrics_bp = Blueprint('metrics', __name__)

# Função para simular métricas a partir dos dados crus
def simulate_metrics(raw_data):
    simulated_data = []

    for item in raw_data:
        # Simula o valor de armazenamento
        storage = float(item.get("2020", 0)) if item.get("2020", "..") != ".." else random.uniform(100, 1000)
        # Simula o número de requisições
        requests = random.randint(100, 5000)

        # Simula o uso de CPU
        cpu_usage = round((requests % 100) + random.uniform(-5, 5), 2)
        # Simula o valor de cobrança
        billing = round(storage * 0.23 + random.uniform(0, 10), 2)
        # Simula o score de compliance
        compliance_score = round(100 - (requests % 30) + random.uniform(-2, 2), 2)

        simulated_data.append({
            "cpu_usage": max(0, min(cpu_usage, 100)),  # Garante que o valor fique entre 0 e 100
            "billing": max(0, billing),                # Garante que o valor não seja negativo
            "compliance_score": max(0, min(compliance_score, 100))  # Entre 0 e 100
        })

    return simulated_data

# Função para calcular a média das métricas simuladas
def compute_avg(data):
    filtered = [
        d for d in data
        if all(k in d for k in ("cpu_usage", "billing", "compliance_score"))
    ]

    if not filtered:
        return {
            "cpu_usage_avg": 0,
            "billing_avg": 0,
            "compliance_score_avg": 0
        }

    cpu_avg = sum(d["cpu_usage"] for d in filtered) / len(filtered)
    billing_avg = sum(d["billing"] for d in filtered) / len(filtered)
    compliance_avg = sum(d["compliance_score"] for d in filtered) / len(filtered)

    return {
        "cpu_usage_avg": round(cpu_avg, 2),
        "billing_avg": round(billing_avg, 2),
        "compliance_score_avg": round(compliance_avg, 2)
    }

# Rota para retornar os dados de todos os serviços
@metrics_bp.route('/data', methods=['GET'])
@swag_from({
    'tags': ['Data'],
    'responses': {200: {'description': 'Dados crus de todos os serviços'}}
})
def get_data():
    return jsonify({
        "aws": get_aws_raw_data(),
        "azure": get_azure_raw_data(),
        "gcp": get_gcp_raw_data()
    })

# Rota para retornar as métricas agregadas de todos os serviços
@metrics_bp.route('/metrics', methods=['GET'])
@swag_from({
    'tags': ['Metrics'],
    'responses': {200: {'description': 'Métricas simuladas e agregadas'}}
})
def get_metrics():
    aws_sim = simulate_metrics(get_aws_raw_data())
    azure_sim = simulate_metrics(get_azure_raw_data())
    gcp_sim = simulate_metrics(get_gcp_raw_data())

    return jsonify({
        "aws": compute_avg(aws_sim),
        "azure": compute_avg(azure_sim),
        "gcp": compute_avg(gcp_sim)
    })

# Rota para retornar os dados da AWS
@metrics_bp.route('/data/aws', methods=['GET'])
@swag_from({'tags': ['Data'], 'responses': {200: {'description': 'Dados AWS'}}})
def get_aws_data():
    return jsonify(get_aws_raw_data())

# Rota para retornar os dados da Azure
@metrics_bp.route('/data/azure', methods=['GET'])
@swag_from({'tags': ['Data'], 'responses': {200: {'description': 'Dados Azure'}}})
def get_azure_data():
    return jsonify(get_azure_raw_data())

# Rota para retornar os dados do GCP
@metrics_bp.route('/data/gcp', methods=['GET'])
@swag_from({'tags': ['Data'], 'responses': {200: {'description': 'Dados GCP'}}})
def get_gcp_data():
    return jsonify(get_gcp_raw_data())

# Rota para retornar as métricas da AWS
@metrics_bp.route('/metrics/aws', methods=['GET'])
@swag_from({'tags': ['Metrics'], 'responses': {200: {'description': 'Métricas AWS'}}})
def get_aws_metrics():
    raw = get_aws_raw_data()
    simulated = simulate_metrics(raw)
    return jsonify(compute_avg(simulated))

# Rota para retornar as métricas da Azure
@metrics_bp.route('/metrics/azure', methods=['GET'])
@swag_from({'tags': ['Metrics'], 'responses': {200: {'description': 'Métricas Azure'}}})
def get_azure_metrics():
    raw = get_azure_raw_data()
    simulated = simulate_metrics(raw)
    return jsonify(compute_avg(simulated))

# Rota para retornar as métricas do GCP
@metrics_bp.route('/metrics/gcp', methods=['GET'])
@swag_from({'tags': ['Metrics'], 'responses': {200: {'description': 'Métricas GCP'}}})
def get_gcp_metrics():
    raw = get_gcp_raw_data()
    simulated = simulate_metrics(raw)
    return jsonify(compute_avg(simulated))
