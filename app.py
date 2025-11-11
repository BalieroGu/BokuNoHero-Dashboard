# app.py (Página Inicial - VERSÃO FINAL)
import streamlit as st

# Configuração da página principal
st.set_page_config(
    page_title="Boku no Hero - DB",
    page_icon="🦸",
    layout="wide"
)

# --- Conteúdo da Página ---

st.title("🦸 Projeto de Banco de Dados II")
st.header("Boku no Hero - Dashboard Interativo")

st.markdown("""
Este projeto é um dashboard interativo completo para a disciplina de Banco de Dados II. 
Ele utiliza **Streamlit** para o front-end e um banco de dados **PostgreSQL** hospedado na nuvem (Neon) para o back-end.

A aplicação permite a visualização, análise e inserção de dados do universo de Boku no Hero.
""")

st.divider()

st.markdown("### 🗺️ Navegação")
st.markdown("Use a barra lateral à esquerda para navegar entre as páginas da aplicação:")

st.markdown("""
* **🏠 Página Inicial:** Esta página que você está vendo.
* **🦸 Dashboard de Heróis:** Exibe o ranking oficial dos heróis, casos resolvidos e suas agências, com gráficos interativos.
* **🧬 Stats de Individualidades:** Analisa a distribuição dos tipos de "Quirks" (Emissor, Mutante, etc.) em gráficos de barra e pizza.
* **✍️ Cadastrar Dados:** Um formulário completo com transações SQL para cadastrar novos Personagens (Heróis, Vilões, Alunos), Batalhas (com participantes) e Entidades (Lugares, Agências, etc.).
* **🗺️ Mapa de Batalhas:** Um mapa interativo do Japão (usando Folium) que mostra onde cada batalha ocorreu. Marcadores agrupados (`MarkerCluster`) permitem explorar batalhas que ocorreram no mesmo local.
""")

st.divider()

# --- AVISO IMPORTANTE SOBRE O NEON ---
st.warning(
    """
    **⚠️ Aviso de Conexão (Neon Scale-to-Zero)**

    O banco de dados gratuito do Neon "dorme" (congela) após 5 minutos de inatividade. 
    
    Ao abrir o site pela primeira vez ou após um período sem uso, o carregamento inicial pode **demorar de 10 a 15 segundos** para "acordar" o banco.
    
    Se você tentar cadastrar um dado e receber um erro de **"SSL connection"**, **apenas atualize a página (F5) e tente novamente.** Isso não é um bug, mas sim uma característica da infraestrutura gratuita.
    """, 
    icon="📡"
)