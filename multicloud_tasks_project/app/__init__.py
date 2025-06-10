from flask import Flask
from flasgger import Swagger
from app.routes.metrics import metrics_bp

# Função para inicializar a aplicação Flask e registrar o blueprint
def create_app():
    # Cria uma instância da aplicação Flask
    app = Flask(__name__)

    # Inicializa o Swagger 
    Swagger(app)

    # Registra o blueprint de métricas na aplicação
    app.register_blueprint(metrics_bp)

   
    return app
