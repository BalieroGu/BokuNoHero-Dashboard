# app.py (Este é o NOVO arquivo na pasta RAIZ)
import streamlit as st

# Configuração da página principal
st.set_page_config(
    page_title="Boku no Hero - DB",
    page_icon="🦸",
    layout="wide"
)

st.title("🦸 Projeto de Banco de Dados II")
st.header("Boku no Hero - Dashboard Interativo")
st.markdown("### Bem-vindo ao Dashboard!")
st.markdown("Use a barra lateral à esquerda para navegar entre as páginas:")
st.markdown("""
* **Dashboard de Heróis:** Vê o ranking e estatísticas dos heróis.
* **Stats de Individualidades:** Analisa a distribuição de tipos de individualidade.
""")
st.markdown("---")
st.markdown("Este projeto foi feito para a disciplina de Banco de Dados II, usando Streamlit e NeonDB.")