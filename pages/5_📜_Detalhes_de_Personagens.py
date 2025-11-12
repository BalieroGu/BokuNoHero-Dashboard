import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Detalhes de Personagens",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Detalhes dos Personagens")

try:
    conn = st.connection("postgres", type="sql")
except Exception as e:
    st.error(f"Erro ao conectar ao banco de dados: {e}")
    st.stop()

@st.cache_data
def load_personagens():
    df = conn.query("""
        SELECT
            p.id_personagem,
            p.nome AS nome_real,
            p.alias,
            p.data_nascimento,
            p.status,
            h.nome_heroi,
            h.ranking,
            h.num_casos_resolvidos,
            a.nome AS agencia,
            v.nome_vilao,
            v.num_crimes,
            o.nome AS organizacao,
            i.nome AS individualidade,
            i.tipo AS tipo_individualidade,
            i.descricao AS desc_individualidade
        FROM personagem p
        LEFT JOIN heroi h ON p.id_personagem = h.id_personagem
        LEFT JOIN agencia a ON h.id_agencia = a.id_agencia
        LEFT JOIN vilao v ON p.id_personagem = v.id_personagem
        LEFT JOIN vilao_pertence_organizacao vo ON v.id_personagem = vo.id_vilao
        LEFT JOIN organizacao_viloes o ON vo.id_organizacao = o.id_organizacao
        LEFT JOIN personagem_possui_individualidade pi ON p.id_personagem = pi.id_personagem
        LEFT JOIN individualidade i ON pi.id_individualidade = i.id_individualidade
        ORDER BY p.nome ASC;
    """)
    return df

try:
    df_personagens = load_personagens()

    nomes = df_personagens["nome_real"].unique().tolist()
    selected = st.selectbox("Selecione um personagem", options=nomes, index=None, placeholder="Escolha um personagem")

    if selected:
        dados = df_personagens[df_personagens["nome_real"] == selected].iloc[0]

        st.subheader(f"👤 {dados['nome_real']}")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"**Alias:** {dados['alias'] or '—'}")
            st.markdown(f"**Status:** {dados['status'] or '—'}")
            if pd.notna(dados['data_nascimento']):
                st.markdown(f"**Data de Nascimento:** {dados['data_nascimento'].strftime('%d/%m/%Y')}")
            st.markdown("---")
            st.markdown("### 💫 Individualidade")
            st.markdown(f"**Nome:** {dados['individualidade'] or '—'}")
            st.markdown(f"**Tipo:** {dados['tipo_individualidade'] or '—'}")
            st.markdown(f"**Descrição:** {dados['desc_individualidade'] or '—'}")

        with col2:
            if pd.notna(dados['nome_heroi']):
                st.markdown("### 🦸 Herói")
                st.markdown(f"**Nome de Herói:** {dados['nome_heroi']}")
                st.markdown(f"**Ranking:** {dados['ranking'] or '—'}")
                st.markdown(f"**Casos Resolvidos:** {dados['num_casos_resolvidos'] or '—'}")
                st.markdown(f"**Agência:** {dados['agencia'] or '—'}")
            elif pd.notna(dados['nome_vilao']):
                st.markdown("### 😈 Vilão")
                st.markdown(f"**Nome de Vilão:** {dados['nome_vilao']}")
                st.markdown(f"**Crimes Cometidos:** {dados['num_crimes'] or '—'}")
                st.markdown(f"**Organização:** {dados['organizacao'] or '—'}")
            else:
                st.markdown("### 🎓 Aluno")
                st.markdown("Sem dados adicionais de herói/vilão — provavelmente um aluno.")

except Exception as e:
    st.error(f"Erro ao carregar detalhes dos personagens: {e}")
