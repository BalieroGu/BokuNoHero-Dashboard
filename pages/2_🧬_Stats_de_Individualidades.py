# pages/2_🧬_Stats_de_Individualidades.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Config da página
st.set_page_config(
    page_title="Stats de Individualidades", 
    page_icon="🧬", 
    layout="wide"
)

st.title("🧬 Estatísticas de Individualidades")
st.header("Distribuição por Tipo")

# --- CONEXÃO COM O BANCO DE DADOS ---
# (Toda página que acessa o BD precisa disso)
try:
    conn = st.connection("postgres", type="sql")
except Exception as e:
    st.error(f"Erro ao conectar ao banco de dados: {e}")
    st.stop() # Para a execução se a conexão falhar

# --- FUNÇÃO DE BUSCA (QUERY) ---
@st.cache_data
def fetch_quirk_stats():
    # Este SQL agrupa por tipo e conta quantos tem em cada tipo
    df = conn.query(
        """
        SELECT 
            Tipo, 
            COUNT(*) AS "Contagem"
        FROM 
            INDIVIDUALIDADE
        WHERE 
            Tipo IS NOT NULL AND Tipo != ''
        GROUP BY 
            Tipo
        ORDER BY 
            "Contagem" DESC;
        """,
        ttl=3600 # Cache de 1 hora
    )
    # Prepara o df para os gráficos
    df_for_charts = df.set_index("tipo")
    return df_for_charts

# --- CONSTRUÇÃO DA PÁGINA ---
try:
    df_stats = fetch_quirk_stats()

    st.subheader("Gráfico de Barras")
    st.bar_chart(df_stats, y="Contagem")

    st.subheader("Gráfico de Pizza")
    # Criamos a figura (fig) e os eixos (ax) para o gráfico
    fig, ax = plt.subplots()

    # Gera o gráfico de pizza
    ax.pie(
        df_stats["Contagem"],      # Os valores (fatias)
        labels=df_stats.index,     # Os rótulos (nomes)
        autopct="%1.1f%%",         # Formato da porcentagem
        startangle=90              # Começa no topo
    )
    ax.axis('equal')  # Garante que seja um círculo

    # Exibe o gráfico (fig) no Streamlit
    st.pyplot(fig)

    st.subheader("Dados Brutos (Tabela)")
    st.dataframe(df_stats, width='stretch')

except Exception as e:
    st.error(f"Erro ao buscar dados: {e}")