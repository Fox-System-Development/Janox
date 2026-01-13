# Janox Power BI Dashboard Rotator

Este projeto consiste em uma aplicacao web desenvolvida com Streamlit para a visualizacao e rotacao automatica de dashboards do Power BI. O objetivo principal e permitir o monitoramento de indicadores em tempo real (Kiosk Mode) com transicoes programadas entre diferentes telas ou vendedores.

## Funcionalidades

* **Rotacao Automatica**: Alterna entre as paginas configuradas a cada 30 segundos.
* **Navegacao Manual**: Barra lateral para selecao direta de relatorios especificos.
* **Layout Full Screen**: Injeção de CSS customizado para remover margens do Streamlit e expandir o iframe do Power BI para ocupar a largura total da tela.
* **Controle de Fluxo**: Opcao de pausar ou retomar a rotacao automatica via toggle na interface lateral.

## Tecnologias Utilizadas

* Python 3.x
* Streamlit
* Power BI Embedded (Integracao via Iframe)

## Estrutura do Projeto

* `app.py`: Codigo fonte principal contendo a logica de navegacao, controle de estado (session state) e configuracoes de layout.
* `requirements.txt`: Lista de dependencias necessarias para execucao do projeto.
* `.env`: Armazenamento de URLs e IDs confidenciais do Power BI (recomendado para producao).

## Instalacao e Execucao

1. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv

2. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate

3. Instale as dependencias:
   ```bash
   pip install -r requirements.txt

4. Execute a aplicação:
   ```bash
   streamlit run app.py