# 📊 Panorama de Ações

Este projeto é uma aplicação interativa desenvolvida em **Python** utilizando **Streamlit** para a análise de preços históricos de ações da Bolsa de Valores. A ferramenta permite visualizar a evolução dos preços ao longo do tempo, analisar o desempenho dos ativos e facilitar a tomada de decisões para investidores e entusiastas do mercado financeiro.

## 🚀 Funcionalidades

- **Seleção interativa de ações**: Escolha os ativos listados na B3 para análise.
- **Definição de período de análise**: Selecione a data inicial e final utilizando um calendário interativo.
- **Visualização de dados históricos**: Gráficos de linha para acompanhar a evolução dos preços das ações ao longo do tempo.
- **Cálculo de performance**: Exibição do retorno percentual dos ativos selecionados e da carteira como um todo.

## 🛠 Tecnologias e Bibliotecas Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python** – Linguagem principal do projeto.
- **Streamlit** – Framework para criação de aplicações web interativas de forma rápida e eficiente.
- **Pandas** – Biblioteca para manipulação e análise de dados.
- **Yahoo Finance API (yfinance)** – Para obtenção de dados históricos das ações.
- **Matplotlib / Seaborn** *(opcional)* – Para visualizações mais avançadas dos dados.

![image](https://github.com/user-attachments/assets/89593697-79fa-421c-a712-589aeee30bbe)
         ![image](https://github.com/user-attachments/assets/8b8ae755-cea0-46fd-8827-d899211b1b30)


## 📥 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/panorama-acoes.git
   cd panorama-acoes
   ```
2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate     # Para Windows
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Execute o aplicativo:**
   ```bash
   streamlit run main.py
   ```

## 🔍 Observações

- Os dados são obtidos via **Yahoo Finance**, então certifique-se de estar conectado à internet ao utilizar o aplicativo.
- Caso haja problemas com a atualização dos dados, verifique se os tickers das ações estão corretos e disponíveis para consulta.
- O arquivo IBOV.csv são os tickers das ações listados da B3, e como são dados públicos e notórios, foram disponibilizados aqui como planilha.
