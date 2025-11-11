# 🦸 Projeto de Banco de Dados II - Boku no Hero Dashboard

Este projeto é um dashboard interativo para a disciplina de Banco de Dados II, usando Streamlit e um banco de dados Neon.

---

## 🚀 Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/BalieroGu/BokuNoHero-Dashboard.git
    cd BokuNoHero-Dashboard
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure o Banco de Dados (IMPORTANTE):**
    Este projeto requer um arquivo de segredos para conectar ao banco de dados.
    * Crie a pasta: `.streamlit`
    * Dentro dela, crie o arquivo: `secrets.toml`
    * Cole o seguinte conteúdo e adicione sua própria URL de conexão do Neon:

    ```toml
    [connections]
    [connections.postgres]
    url = "SUA_URL_DE_CONEXAO_POSTGRESQL_AQUI"
    ```

4.  **Rode o Streamlit:**
    ```bash
    streamlit run app.py
    ```

---

### ⚠️ Aviso de Conexão (Neon Scale-to-Zero)

O banco de dados gratuito do Neon "dorme" após 5 minutos de inatividade. Ao abrir o site pela primeira vez, o carregamento pode demorar 10-15 segundos. Se você receber um erro de **"SSL connection"** ao cadastrar um dado, **apenas atualize a página (F5) e tente novamente.**
