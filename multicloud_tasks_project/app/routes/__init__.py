from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.routes.metrics import metrics_bp
    app.register_blueprint(metrics_bp, url_prefix="/")
    return app
