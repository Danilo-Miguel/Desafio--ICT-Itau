from flask import Flask
from flasgger import Swagger
from app.routes.metrics import metrics_bp

def create_app():
    app = Flask(__name__)

    # Inicializa o Swagger
    Swagger(app)

    # Registra o blueprint sem prefixo adicional
    app.register_blueprint(metrics_bp)

    return app
