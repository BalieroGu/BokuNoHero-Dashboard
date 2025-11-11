# pages/3_✍️_Cadastrar_Dados.py (VERSÃO CORRIGIDA)
import streamlit as st
import pandas as pd
from sqlalchemy.sql import text
from datetime import date # <--- MUDANÇA 1: Importamos a biblioteca 'date'

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Cadastrar Dados", 
    page_icon="✍️", 
    layout="centered"
)
st.title("✍️ Cadastrar Novos Dados")

# --- CONEXÃO COM O BANCO DE DADOS ---
try:
    conn = st.connection("postgres", type="sql")
except Exception as e:
    st.error(f"Erro ao conectar ao banco de dados: {e}")
    st.stop()

# --- FUNÇÕES DE BUSCA (para popular os dropdowns) ---
@st.cache_data
def load_select_data():
    """Busca dados de tabelas auxiliares para os menus"""
    locais = conn.query("SELECT id_lugar, nome FROM lugar ORDER BY nome")
    agencias = conn.query("SELECT id_agencia, nome FROM agencia ORDER BY nome")
    orgs = conn.query("SELECT id_organizacao, nome FROM organizacao_viloes ORDER BY nome")
    individs = conn.query("SELECT id_individualidade, nome FROM individualidade ORDER BY nome")
    personagens = conn.query("SELECT id_personagem, nome FROM personagem ORDER BY nome")
    
    # Criamos dicionários para mapear Nome -> ID facilmente
    locais_map = {row['nome']: row['id_lugar'] for _, row in locais.iterrows()}
    agencias_map = {row['nome']: row['id_agencia'] for _, row in agencias.iterrows()}
    orgs_map = {row['nome']: row['id_organizacao'] for _, row in orgs.iterrows()}
    individs_map = {row['nome']: row['id_individualidade'] for _, row in individs.iterrows()}
    personagens_map = {row['nome']: row['id_personagem'] for _, row in personagens.iterrows()}
    
    return locais_map, agencias_map, orgs_map, individs_map, personagens_map

# Carrega os dados
try:
    locais_map, agencias_map, orgs_map, individs_map, personagens_map = load_select_data()
except Exception as e:
    st.error(f"Erro ao carregar dados para os formulários: {e}")
    st.stop()


# --- NAVEGAÇÃO DOS FORMULÁRIOS (Substituindo st.tabs) ---
page = st.radio(
    "Selecione o formulário:",
    ["Cadastrar Personagem", "Cadastrar Batalha", "Cadastrar Entidades"],
    horizontal=True,
    label_visibility="collapsed", # Esconde o rótulo "Selecione o formulário:"
    key="cadastro_page_selector" # Chave para salvar o estado
)
st.divider() # Linha divisória

# --- SEÇÃO 1: CADASTRAR PERSONAGEM ---
if page == "Cadastrar Personagem":
    st.header("Novo Personagem")
    st.info("Para cadastrar um personagem, a 'Individualidade' e a 'Agência'/'Organização' dele já devem existir. Use a aba 'Cadastrar Entidades' se precisar.")
    
    st.subheader("Tipo de Personagem")
    tipo_personagem = st.radio(
        "Tipo", 
        ["Aluno", "Herói", "Vilão"], 
        horizontal=True, 
        index=None,
        key="tipo_personagem_selector"
    )
    st.divider()

    with st.form("form_personagem", clear_on_submit=True):
        st.subheader("Dados Básicos")
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome Real", placeholder="Izuku Midoriya")
        with col2:
            alias = st.text_input("Alias (Apelido)", placeholder="Deku")
        
        col3, col4 = st.columns(2)
        with col3:
            # <--- MUDANÇA 2: Definimos um limite de 100 anos para trás ---
            min_birth_date = date.today().replace(year=date.today().year - 200)
            data_nasc = st.date_input(
                "Data de Nascimento",
                value=date(2009, 1, 1), # Um padrão razoável
                min_value=min_birth_date,
                max_value=date.today()
            )
        with col4:
            status = st.selectbox("Status", ["Vivo", "Viva", "Falecido", "Preso", "Desconhecido", "Aposentado"])

        individualidade_nome = st.selectbox(
            "Individualidade Principal", 
            options=individs_map.keys(),
            index=None,
            placeholder="Selecione a Individualidade"
        )
        st.divider()

        if tipo_personagem == "Aluno":
            st.subheader("Informações de Aluno")
            ano_letivo = st.number_input("Ano Letivo", min_value=1, max_value=3, step=1)
            turma = st.text_input("Turma", placeholder="1-A")
        
        elif tipo_personagem == "Herói":
            st.subheader("Informações de Herói")
            nome_heroi = st.text_input("Nome de Herói", placeholder="All Might")
            ranking = st.number_input("Ranking", min_value=1, step=1, value=None, placeholder="Opcional")
            casos = st.number_input("Casos Resolvidos", min_value=0, step=1)
            agencia_nome = st.selectbox(
                "Agência (Opcional)", 
                options=agencias_map.keys(),
                index=None,
                placeholder="Selecione a Agência"
            )

        elif tipo_personagem == "Vilão":
            st.subheader("Informações de Vilão")
            nome_vilao = st.text_input("Nome de Vilão", placeholder="Tomura Shigaraki")
            crimes = st.number_input("Número de Crimes", min_value=0, step=1)
            org_nome = st.selectbox(
                "Organização (Opcional)", 
                options=orgs_map.keys(),
                index=None,
                placeholder="Selecione a Organização"
            )
        
        st.divider()
        submitted = st.form_submit_button("Cadastrar Personagem")

    if submitted:
        if not nome or not individualidade_nome or not tipo_personagem:
            st.error("Por favor, preencha Nome, Individualidade e Tipo.")
        else:
            try:
                with conn.session as s:
                    sql_personagem = text("""
                        INSERT INTO PERSONAGEM (Nome, Data_Nascimento, Status, Alias)
                        VALUES (:nome, :data, :status, :alias)
                        RETURNING id_personagem;
                    """)
                    result = s.execute(sql_personagem, {
                        "nome": nome, 
                        "data": data_nasc, 
                        "status": status, 
                        "alias": alias
                    })
                    new_id = result.scalar()
                    
                    if tipo_personagem == "Aluno":
                        sql_tipo = text("""
                            INSERT INTO ALUNO (ID_Personagem, Ano_Letivo, Turma)
                            VALUES (:id, :ano, :turma);
                        """)
                        s.execute(sql_tipo, {"id": new_id, "ano": ano_letivo, "turma": turma})
                    
                    elif tipo_personagem == "Herói":
                        id_agencia = agencias_map.get(agencia_nome)
                        sql_tipo = text("""
                            INSERT INTO HEROI (ID_Personagem, Nome_Heroi, Ranking, Num_Casos_Resolvidos, ID_Agencia)
                            VALUES (:id, :nome_h, :rank, :casos, :id_ag);
                        """)
                        s.execute(sql_tipo, {
                            "id": new_id, 
                            "nome_h": nome_heroi, 
                            "rank": ranking, 
                            "casos": casos, 
                            "id_ag": id_agencia
                        })

                    elif tipo_personagem == "Vilão":
                        id_org = orgs_map.get(org_nome)
                        sql_tipo = text("""
                            INSERT INTO VILAO (ID_Personagem, Nome_Vilao, Num_Crimes)
                            VALUES (:id, :nome_v, :crimes);
                        """)
                        s.execute(sql_tipo, {"id": new_id, "nome_v": nome_vilao, "crimes": crimes})
                        
                        if id_org:
                            sql_org = text("""
                                INSERT INTO VILAO_PERTENCE_ORGANIZACAO (ID_Vilao, ID_Organizacao)
                                VALUES (:id_v, :id_o);
                            """)
                            s.execute(sql_org, {"id_v": new_id, "id_o": id_org})

                    id_ind = individs_map[individualidade_nome]
                    sql_ind = text("""
                        INSERT INTO PERSONAGEM_POSSUI_INDIVIDUALIDADE (ID_Personagem, ID_Individualidade)
                        VALUES (:id_p, :id_i);
                    """)
                    s.execute(sql_ind, {"id_p": new_id, "id_i": id_ind})

                    s.commit()
                    st.success(f"Personagem '{nome}' cadastrado com sucesso! (ID: {new_id})")
                    st.cache_data.clear() 

            except Exception as e:
                st.error(f"Erro ao cadastrar personagem: {e}")


# --- SEÇÃO 2: CADASTRAR BATALHA ---
elif page == "Cadastrar Batalha":
    st.header("Nova Batalha")
    st.info("Para cadastrar uma batalha, o 'Local' já deve existir. Use a aba 'Cadastrar Entidades' se precisar.")

    with st.form("form_batalha", clear_on_submit=True):
        nome_batalha = st.text_input("Nome da Batalha", placeholder="Batalha de Kamino")
        
        col1, col2 = st.columns(2)
        with col1:
            # <--- MUDANÇA 3: Definimos um limite para a data da batalha ---
            data_batalha = st.date_input(
                "Data da Batalha", 
                value=date.today(),
                min_value=date(2010, 1, 1) # Limite de 2010
            )
        with col2:
            duracao = st.text_input("Duração", placeholder="30 minutos")

        image_url = st.text_input("URL da Imagem (Opcional)", placeholder="https://media.tenor.com/...gif")

        local_nome = st.selectbox(
            "Local da Batalha",
            options=locais_map.keys(),
            index=None,
            placeholder="Selecione o Local"
        )
        
        participantes_nomes = st.multiselect(
            "Participantes",
            options=personagens_map.keys(),
            placeholder="Selecione os personagens envolvidos"
        )
        
        submitted_batalha = st.form_submit_button("Cadastrar Batalha")

    if submitted_batalha:
        if not nome_batalha or not local_nome or not participantes_nomes:
            st.error("Por favor, preencha Nome, Local e pelo menos um Participante.")
        else:
            try:
                with conn.session as s:
                    id_local = locais_map[local_nome]
                    
                    sql_batalha = text("""
                        INSERT INTO BATALHA (Nome, Data, Duracao, ID_Lugar, image_url)
                        VALUES (:nome, :data, :dur, :id_lugar, :img_url)
                        RETURNING id_batalha;
                    """)
                    
                    result = s.execute(sql_batalha, {
                        "nome": nome_batalha,
                        "data": data_batalha,
                        "dur": duracao,
                        "id_lugar": id_local,
                        "img_url": image_url
                    })
                    
                    new_id_batalha = result.scalar()

                    selected_ids = [personagens_map[nome] for nome in participantes_nomes]
                    params_list = [
                        {"id_b": new_id_batalha, "id_p": p_id} for p_id in selected_ids
                    ]
                    sql_participante = text("""
                        INSERT INTO PARTICIPANTES_BATALHA (ID_Batalha, ID_Personagem)
                        VALUES (:id_b, :id_p);
                    """)
                    s.execute(sql_participante, params_list)
                    s.commit()
                
                st.success(f"Batalha '{nome_batalha}' e seus {len(participantes_nomes)} participantes cadastrados!")
                st.cache_data.clear() 

            except Exception as e:
                st.error(f"Erro ao cadastrar batalha: {e}")

# --- SEÇÃO 3: CADASTRAR ENTIDADES ---
elif page == "Cadastrar Entidades":
    st.header("Cadastrar Novas Entidades")
    st.info("Cadastre aqui os itens que aparecem nos menus de seleção.")

    with st.form("form_lugar", clear_on_submit=True):
        st.subheader("Novo Local")
        col1, col2 = st.columns(2)
        with col1:
            lugar_nome = st.text_input("Nome do Local", placeholder="Kamino Ward")
            lugar_pais = st.text_input("País", value="Japão")
            lugar_lat = st.number_input("Latitude", format="%.6f", placeholder="Ex: 35.447700")
        with col2:
            lugar_cidade = st.text_input("Cidade", placeholder="Yokohama")
            lugar_arco = st.text_input("Arco Associado", placeholder="All Might vs All For One")
            lugar_lon = st.number_input("Longitude", format="%.6f", placeholder="Ex: 139.641800")
        
        sub_lugar = st.form_submit_button("Cadastrar Local")
        if sub_lugar and lugar_nome:
            try:
                sql = text("""
                    INSERT INTO LUGAR (Nome, Cidade, Pais, Arco_Associado, Latitude, Longitude)
                    VALUES (:nome, :cid, :pais, :arco, :lat, :lon);
                """)
                with conn.session as s:
                    s.execute(sql, {
                        "nome": lugar_nome, "cid": lugar_cidade, "pais": lugar_pais,
                        "arco": lugar_arco, "lat": lugar_lat, "lon": lugar_lon
                    })
                    s.commit()
                st.success(f"Local '{lugar_nome}' cadastrado!")
                st.cache_data.clear()
            except Exception as e:
                st.error(f"Erro: {e}")

    with st.form("form_ind", clear_on_submit=True):
        st.subheader("Nova Individualidade")
        nome_ind = st.text_input("Nome da Individualidade", placeholder="One For All")
        tipo_ind = st.selectbox("Tipo", ["Emissor", "Transformação", "Mutante", "Desconhecido"])
        desc_ind = st.text_area("Descrição")
        
        sub_ind = st.form_submit_button("Cadastrar Individualidade")
        if sub_ind and nome_ind:
            try:
                sql = text("INSERT INTO INDIVIDUALIDADE (Nome, Tipo, Descricao) VALUES (:nome, :tipo, :desc);")
                with conn.session as s:
                    s.execute(sql, {"nome": nome_ind, "tipo": tipo_ind, "desc": desc_ind})
                    s.commit()
                st.success(f"Individualidade '{nome_ind}' cadastrada!")
                st.cache_data.clear()
            except Exception as e:
                st.error(f"Erro: {e}")
                
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        with st.form("form_agencia", clear_on_submit=True):
            st.subheader("Nova Agência")
            nome_ag = st.text_input("Nome da Agência", placeholder="Agência Endeavor")
            loc_ag = st.text_input("Localização", placeholder="Tóquio, Japão")
            num_ag = st.number_input("Nº de Membros", min_value=1, step=1)
            
            sub_ag = st.form_submit_button("Cadastrar Agência")
            if sub_ag and nome_ag:
                try:
                    sql = text("INSERT INTO AGENCIA (Nome, Num_Membros, Localizacao) VALUES (:nome, :num, :loc);")
                    with conn.session as s:
                        s.execute(sql, {"nome": nome_ag, "num": num_ag, "loc": loc_ag})
                        s.commit()
                    st.success(f"Agência '{nome_ag}' cadastrada!")
                    st.cache_data.clear()
                except Exception as e:
                    st.error(f"Erro: {e}")
    
    with col2:
        with st.form("form_org", clear_on_submit=True):
            st.subheader("Nova Organização de Vilões")
            nome_org = st.text_input("Nome da Organização", placeholder="Liga dos Vilões")
            loc_org = st.text_input("Localização", placeholder="Esconderijo")
            num_org = st.number_input("Nº de Membros", min_value=1, step=1)
            
            sub_org = st.form_submit_button("Cadastrar Organização")
            if sub_org and nome_org:
                try:
                    sql = text("INSERT INTO ORGANIZACAO_VILOES (Nome, Num_Membros, Localizacao) VALUES (:nome, :num, :loc);")
                    with conn.session as s:
                        s.execute(sql, {"nome": nome_org, "num": num_org, "loc": loc_org})
                        s.commit()
                    st.success(f"Organização '{nome_org}' cadastrada!")
                    st.cache_data.clear()
                except Exception as e:
                    st.error(f"Erro: {e}")