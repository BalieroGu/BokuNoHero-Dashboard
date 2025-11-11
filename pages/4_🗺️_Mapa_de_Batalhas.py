# pages/4_🗺️_Mapa_de_Batalhas.py (VERSÃO FINAL)
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium # Componente para renderizar o Folium
from folium import IFrame # Para criar o popup customizado
from folium.plugins import MarkerCluster # 1. IMPORTAMOS O CLUSTER

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Mapa de Batalhas", 
    page_icon="🗺️", 
    layout="wide"
)
st.title("🗺️ Mapa Interativo de Batalhas")
st.markdown("Passe o mouse sobre um ícone para ver o nome. Clique em um 'cluster' (círculo com número) para separar batalhas no mesmo local.")

# --- CONEXÃO COM O BANCO DE DADOS ---
try:
    conn = st.connection("postgres", type="sql")
except Exception as e:
    st.error(f"Erro ao conectar ao banco de dados: {e}")
    st.stop()

# --- FUNÇÃO DE BUSCA (A SUPER QUERY) ---
# 2. REMOVEMOS O @st.cache_data DAQUI
# Isso força o Streamlit a NUNCA usar o cache nesta página.
def fetch_battle_data():
    sql_query = """
    SELECT 
        b.nome AS battle_name,
        b.data,
        b.duracao,
        b.image_url,
        l.nome AS lugar_nome,
        l.latitude,
        l.longitude,
        STRING_AGG(p.nome, ', ') AS participantes
    FROM 
        batalha b
    JOIN 
        lugar l ON b.id_lugar = l.id_lugar
    LEFT JOIN 
        participantes_batalha pb ON b.id_batalha = pb.id_batalha
    LEFT JOIN 
        personagem p ON pb.id_personagem = p.id_personagem
    WHERE 
        l.latitude IS NOT NULL AND l.longitude IS NOT NULL
    GROUP BY 
        b.id_batalha, l.id_lugar
    ORDER BY
        b.data DESC;
    """
    df = conn.query(sql_query) # Sem 'ttl' (cache)
    return df

# --- CONSTRUÇÃO DO MAPA ---
try:
    df_batalhas = fetch_battle_data()

    if df_batalhas.empty:
        st.warning("Nenhum dado de batalha com localização encontrado.")
        st.stop()

    # Adicionamos uma legenda para depuração:
    st.caption(f"Total de {len(df_batalhas)} batalhas encontradas no banco de dados.")

    # Cria o mapa base, centrado no Japão
    map_center = [
        df_batalhas['latitude'].mean(), 
        df_batalhas['longitude'].mean()
    ]
    m = folium.Map(location=map_center, zoom_start=6, tiles="CartoDB positron")

    # 3. CRIAMOS O CLUSTER DE MARCADORES
    marker_cluster = MarkerCluster().add_to(m)

    # Adiciona um marcador para cada batalha
    for idx, row in df_batalhas.iterrows():
        
        # --- Lógica do Pop-up (HTML) ---
        if row['image_url']:
            image_html = f'<img src="{row["image_url"]}" style="width: 100%; object-fit: cover; border-radius: 5px;">'
        else:
            image_html = '<p style="text-align: center; font-style: italic;">(Sem imagem cadastrada para esta batalha)</p>'

        html_popup = f"""
        <div style="width: 300px;">
            <h3 style="margin-bottom: 5px;">{row['battle_name']}</h3>
            {image_html}
            <hr style="margin: 10px 0;">
            <p><strong>Data:</strong> {row['data'].strftime('%d/%m/%Y')}</p>
            <p><strong>Duração:</strong> {row['duracao']}</p>
            <p><strong>Local:</strong> {row['lugar_nome']}</p>
            <hr style="margin: 10px 0;">
            <p><strong>Participantes Principais:</strong><br>{row.get('participantes', 'N/A')}</p>
        </div>
        """
        iframe = IFrame(html_popup, width=330, height=450)
        popup = folium.Popup(iframe, max_width=330)
        tooltip = f"Batalha: {row['battle_name']}"
        
        # 4. ADICIONA O MARCADOR AO CLUSTER (NÃO AO MAPA)
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=popup,
            tooltip=tooltip,
            icon=folium.Icon(color="red", icon="bomb", prefix="fa") 
        ).add_to(marker_cluster) # Mudamos de .add_to(m) para .add_to(marker_cluster)

    # Renderiza o mapa no Streamlit
    st_data = st_folium(m, width="100%", height=600)

except Exception as e:
    st.error(f"Erro ao construir o mapa: {e}")