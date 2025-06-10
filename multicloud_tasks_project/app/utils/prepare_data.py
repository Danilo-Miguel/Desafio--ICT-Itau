from data_loader import load_and_process_aws, load_and_process_gcp, load_and_process_azure

# Executa o script apenas se for chamado diretamente
if __name__ == "__main__":
    print("Gerando mock AWS...")
    load_and_process_aws()  # Gera e salva o mock de dados da AWS
    print("Mock AWS gerado com sucesso.")

    print("Gerando mock GCP...")
    load_and_process_gcp()  # Gera e salva o mock de dados do GCP
    print("Mock GCP gerado com sucesso.")

    print("Gerando mock Azure...")
    load_and_process_azure()  # Gera e salva o mock de dados da Azure
    print("Mock Azure gerado com sucesso.")
