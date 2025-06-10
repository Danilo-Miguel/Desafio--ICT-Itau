# Desafio--ICT-Itau
Desafio Multicloud API
Objetivo
Desenvolver uma API que consome dados multicloud e retorna métricas em tempo real, como uso de CPU, billing (custo) e compliance.

Descrição
Foi criada uma API em Python utilizando Flask para esse propósito. Os dados são mockados, mas baseados em datasets reais baixados do Kaggle — uma plataforma que oferece diversos conjuntos de dados públicos para projetos de ciência de dados e machine learning. São eles: Global Internet Usage by Country (2000-2023); Large Dataset of Cars e QS World University Rankings

Esses dados foram armazenados em um storage interno da aplicação e carregados simulando uma coleta em tempo real para cada provedor: AWS, GCP e Azure. Com base nessa coleta simulada, são geradas métricas fictícias (fake) para uso de CPU, custo e compliance.

São criados três arquivos .json a partir desses dados.

aws_mock.json que contém os dados do data set Global Internet Usage by Country (2000-2023)
azure_mock.json que contém os dados do data set arge Dataset of Cars
gcp_mock.json ue contém os dados do data set QS World University Rankings

A documentação da API e seus endpoints estão disponíveis via Swagger.

Como utilizar
1. Clonar o repositório:
git clone https://github.com/Danilo-Miguel/Desafio--ICT-Itau

2. Entrar na pasta do projeto:
cd multicloud_tasks_project

3. Instalar as dependências:
pip install -r requirements.txt

4. Executar o projeto:
python run.py

Como testar?
Via navegador:
Dados unificados dos três provedores:
http://localhost:5000/data

Métricas unificadas dos três provedores:
http://localhost:5000/metrics

Dados por provedor:

GCP: http://localhost:5000/data/gcp

AWS: http://localhost:5000/data/aws

Azure: http://localhost:5000/data/azure


Métricas por provedor:

GCP: http://localhost:5000/metrics/gcp

AWS: http://localhost:5000/metrics/aws

Azure: http://localhost:5000/metrics/azure

Documentação Swagger:
http://localhost:5000/apidocs/#/Data/get_data

Observação
Foi implementado um loop para simular a coleta em tempo real, além do cálculo das métricas. Portanto, ao atualizar a página (F5), os dados são atualizados dinamicamente.


