from data_loader import load_and_process_aws, load_and_process_gcp, load_and_process_azure

if __name__ == "__main__":
    print("Gerando mock AWS...")
    load_and_process_aws()
    print("Mock AWS gerado com sucesso.")

    print("Gerando mock GCP...")
    load_and_process_gcp()
    print("Mock GCP gerado com sucesso.")

    print("Gerando mock Azure...")
    load_and_process_azure()
    print("Mock Azure gerado com sucesso.")
