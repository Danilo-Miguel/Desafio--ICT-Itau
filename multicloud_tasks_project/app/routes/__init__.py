from flask import Flask

# Função para criar e configurar a aplicação Flask
def create_app():
    app = Flask(__name__)  
    from app.routes.metrics import metrics_bp  # Importa o blueprint de métricas
    app.register_blueprint(metrics_bp, url_prefix="/")  # Registra o blueprint 
    return app  
