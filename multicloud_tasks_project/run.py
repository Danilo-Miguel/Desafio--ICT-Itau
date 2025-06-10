from app import create_app

# Função para criar a aplicação Flask

app = create_app()  # Cria a instância da aplicação Flask 

if __name__ == "__main__":
    # Executa a aplicação Flask em modo debug
    app.run(debug=True)
