from flask import Blueprint, jsonify
from app.services.aws_service import get_aws_data
from app.services.azure_service import get_azure_data
from app.services.gcp_service import get_gcp_data

metrics_bp = Blueprint('metrics', __name__)

@metrics_bp.route('/data', methods=['GET'])
def get_data():
    return jsonify({
        "aws": get_aws_data(),
        "azure": get_azure_data(),
        "gcp": get_gcp_data()
    })

def compute_avg(data):
    # Filtra os dicionários que têm todas as chaves necessárias
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

@metrics_bp.route('/metrics', methods=['GET'])
def get_metrics():
    aws = get_aws_data()
    azure = get_azure_data()
    gcp = get_gcp_data()

    return jsonify({
        "aws": compute_avg(aws),
        "azure": compute_avg(azure),
        "gcp": compute_avg(gcp)
    })
