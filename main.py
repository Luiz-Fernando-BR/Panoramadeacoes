# Importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import date, timedelta

# Definir as datas padrão
DATA_INICIAL_PADRAO = date(2000, 1, 1)
DATA_FINAL_PADRAO = date.today() - timedelta(days=1)  # Último fechamento do mercado

# Criar funções de carregamento de dados
@st.cache_data
def carregar_dados(empresas, data_inicio, data_fim):
    if not empresas:
        st.error("Nenhuma ação selecionada. Selecione pelo menos uma ação.")
        return None

    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)

    try:
        # Converter datas para string no formato esperado pelo Yahoo Finance
        cotacoes_acao = dados_acao.history(period="1d", start=str(data_inicio), end=str(data_fim))
    except Exception as e:
        st.error(f"Ocorreu um erro ao tentar carregar os dados: {e}")
        return None

    if cotacoes_acao.empty:
        st.error("Nenhum dado retornado. Verifique se os tickers estão corretos.")
        return None
    
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

@st.cache_data
def carregar_tickers_acoes():
    # Simulando a leitura de um arquivo CSV de tickers
    # Substitua pelo seu arquivo real "IBOV.csv"
    base_tickers = pd.read_csv("IBOV.csv", sep=";")
    tickers = list(base_tickers["Código"])
    tickers = [item + ".SA" for item in tickers]
    return tickers

# Carregar os tickers
acoes = carregar_tickers_acoes()

# Criar a interface do Streamlit
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações ao longo dos anos.
""")

# Sidebar para filtros
st.sidebar.header("Filtros")

# Filtro de ações
lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar", acoes)

# Filtros de data
with st.sidebar:
    data_inicial = st.date_input("Selecione a Data Inicial", DATA_INICIAL_PADRAO, min_value=DATA_INICIAL_PADRAO, max_value=DATA_FINAL_PADRAO)
    data_final = st.date_input("Selecione a Data Final", DATA_FINAL_PADRAO, min_value=DATA_INICIAL_PADRAO, max_value=DATA_FINAL_PADRAO)

# Verificar se a data inicial não é maior que a final
if data_inicial > data_final:
    st.error("A data inicial deve ser menor ou igual à data final.")
    st.stop()

# Carregar os dados conforme as datas escolhidas
dados = carregar_dados(lista_acoes, data_inicial, data_final)

if dados is not None:
    # Ajustar os dados para visualização
    if len(lista_acoes) == 0:
        st.write("Por favor, selecione pelo menos uma ação para visualizar.")
    else:
        # Filtra os dados conforme as ações escolhidas
        dados = dados[lista_acoes] if lista_acoes else dados

        # Criar o gráfico
        st.line_chart(dados)

        # Cálculo de performance
        texto_performance_ativos = ""

        if len(lista_acoes) == 0:
            lista_acoes = list(dados.columns)

        carteira = [1000 for acao in lista_acoes]
        total_inicial_carteira = sum(carteira)

        for i, acao in enumerate(lista_acoes):
            performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
            performance_ativo = float(performance_ativo)

            carteira[i] = carteira[i] * (1 + performance_ativo)

            if performance_ativo > 0:
        # :cor[texto]
                texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :green[{performance_ativo:.1%}]"
            elif performance_ativo < 0:
                texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :red[{performance_ativo:.1%}]"
            else:
                texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: {performance_ativo:.1%}"

        total_final_carteira = sum(carteira)
        performance_carteira = total_final_carteira / total_inicial_carteira - 1

        if performance_carteira > 0:
            texto_performance_carteira = f"Performance da carteira com todos os ativos: :green[{performance_carteira:.1%}]"
        elif performance_carteira < 0:
            texto_performance_carteira = f"Performance da carteira com todos os ativos: :red[{performance_carteira:.1%}]"
        else:
             texto_performance_carteira = f"Performance da carteira com todos os ativos: {performance_carteira:.1%}"



st.write(f"""
### Performance dos Ativos
Essa foi a perfomance de cada ativo no período selecionado:

{texto_performance_ativos}

{texto_performance_carteira}
""")