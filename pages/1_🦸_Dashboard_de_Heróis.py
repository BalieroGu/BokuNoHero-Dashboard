# app.py (Versão Corrigida)
import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Boku no Hero - Dashboard",
    page_icon="🦸",
    layout="wide"
)

# --- CONEXÃO COM O BANCO DE DADOS ---
# Esta é a forma moderna! O Streamlit lê o secrets.toml
# e gerencia a conexão para nós.
try:
    conn = st.connection("postgres", type="sql")
except Exception as e:
    st.error(f"Erro ao conectar ao banco de dados: {e}")
    st.stop() # Para a execução se a conexão falhar

# --- FUNÇÃO DE BUSCA (QUERY) ---
# A anotação @st.cache_data garante que a consulta (query) só seja
# executada se algo mudar, melhorando a performance.
@st.cache_data
def fetch_hero_data():
    # Usamos o conn.query para buscar os dados e já transformá-los
    # em um DataFrame do Pandas.
    df = conn.query(
        """
        SELECT 
            h.Ranking,
            p.Nome AS "Nome Real",
            h.Nome_Heroi AS "Nome de Herói",
            h.Num_Casos_Resolvidos AS "Casos Resolvidos",
            a.Nome AS "Agência"
        FROM 
            HEROI h
        JOIN 
            PERSONAGEM p ON h.ID_Personagem = p.ID_Personagem
        LEFT JOIN 
            AGENCIA a ON h.ID_Agencia = a.ID_Agencia
        WHERE
            h.Ranking IS NOT NULL
        ORDER BY 
            h.Ranking ASC;
        """,
        ttl=3600  # Armazena o resultado em cache por 1 hora
    )
    return df

# --- CONSTRUÇÃO DA PÁGINA ---
st.title("🦸 Dashboard de Heróis - Boku no Hero")
st.header("Ranking Oficial de Heróis")

# Tenta buscar os dados
try:
    df_herois = fetch_hero_data()
    
    # Exibe os dados em uma tabela interativa
    st.dataframe(df_herois, use_container_width=True)
    
    st.header("Estatísticas de Casos Resolvidos")
    
    # Cria um gráfico de barras
    st.bar_chart(df_herois, x="Nome de Herói", y="Casos Resolvidos")

except Exception as e:
    st.error(f"Erro ao buscar dados: {e}")