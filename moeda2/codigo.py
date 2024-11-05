import streamlit as st
import requests
import pandas as pd
import time


#Incone da pagina
st.set_page_config(page_title="Conversor",page_icon="🪙")
#Atalho para o CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Textos da interface
with st.sidebar:
    st.title("Conversor")
    st.header("Curiosidades sobre conversão de moedas")
    st.write("O mercado de câmbio, também conhecido como Forex (Foreign Exchange), é o maior e mais líquido mercado financeiro do mundo, com um volume diário de negociação que ultrapassa os 6 trilhões de dólares.")
    st.header("Qual o Papel das Taxas de Câmbio?")
    st.write("As taxas de câmbio não são apenas para turistas ou para o comércio internacional. Elas também influenciam as políticas econômicas e as decisões financeiras dos países, afetando preços, inflação, juros e, em última análise, o crescimento econômico.")

# Configuração inicial do Streamlit
st.markdown('<h1 class="titulo">Conversor de Moedas</h1>', unsafe_allow_html=True)
st.markdown('<p class="paragrafo">As taxas de câmbio oscilam a cada minuto. Nossa ferramenta de conversão de moedas fornece aos usuários as taxas de câmbio mais recentes, coletadas de fontes confiáveis e de sólida reputação, para que eles possam tomar decisões informadas em relação a suas transações de câmbio. Com quase 1 ano de experiência nos mercados de taxas de câmbio, o conversor de moedas tem como base todo o nosso conhecimento, experiência e profundo entendimento de como os mercados de câmbio funcionam.</p>', unsafe_allow_html=True)

# API Key e URL base da ExchangeRate-API
API_KEY = "6eeced538f92b8b4965c1a1ec1"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

# Função para obter as taxas de câmbio
def get_exchange_rates(base_currency):
    try:
        response = requests.get(BASE_URL + base_currency)
        response.raise_for_status()
        data = response.json()
        if data["result"] == "success":
            return data["conversion_rates"]
        else:
            st.error(f"Erro: {data['error-type']}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Erro na requisição: {e}")
        return None

# Interface do usuário
moeda_origem = st.selectbox("Moeda de origem", ["USD", "EUR", "BRL", "JPY", "GBP"])
moeda_destino = st.selectbox("Moeda de destino", ["USD", "EUR", "BRL", "JPY", "GBP"])
valor = st.number_input("Valor a ser convertido", min_value=0.0, format="%.2f")

# Botão para iniciar a conversão
if st.button("Converter"):
    taxas = get_exchange_rates(moeda_origem)
    # Carregamento de dados
    with st.spinner('Carregando valores....'):
        time.sleep(2)
    if taxas and moeda_destino in taxas:
        taxa_cambio = taxas[moeda_destino]
        resultado = valor * taxa_cambio
        st.success(f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")

        # Carregamento de dados
        with st.spinner('Carregando Gafico....'):
            time.sleep(2)

        #Graficos do Site
        df = pd.DataFrame(taxas.items(), columns=["Moeda", "Taxa de Câmbio"])

        
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Taxas de Câmbio")
            st.dataframe(df.set_index("Moeda"))

        with col2:
            # Carregamento de dados
            with st.spinner('Carregando Gafico....'):
                time.sleep(2)
            # Gráfico de barras com as taxas de câmbio
            st.markdown("### Gráfico de Taxas de Câmbio")
            st.bar_chart(df.set_index("Moeda")) 

    else:
        st.error("Não foi possível realizar a conversão.")
# Footer
st.markdown('<div class="footer"><p>©2024 Alunos: @Antonio_Vinicius, @Francisco_Everaldo, @Pedro_de_Melo.</p></div>', unsafe_allow_html=True)