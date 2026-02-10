![](https://komarev.com/ghpvc/?username=vitoroliversoares-etl-supabase-postgres&label=Visualizações+do+Projeto&color=2ecc71)

# Automação de backup ETL (PostgreSQL & Supabase)

![Python](https://img.shields.io/badge/Python-ED8B00?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)

Pipeline de engenharia de dados desenvolvido em **Python** para automatizar a sincronização segura entre banco de dados em nuvem (Supabase) e infraestrutura local (On-Premise).

## 🍀 Funcionalidades:

- **Extração (Extract):** Dump automatizado do banco Supabase via `pg_dump`.
- **Carga (Load):** Restauração segura no PostgreSQL local via `psql`.
- **Segurança:** Uso de variáveis de ambiente (`.env`) para proteção de credenciais.
- **Limpeza:** Remoção automática de arquivos temporários pós-processamento.
- **Tratamento de Erros:** Sistema robusto que interrompe o processo em caso de falha de conexão.

## 🛠️ Tecnologias
- Python 3.14.0
- PostgreSQL 18
- Libs: `python-dotenv`, `subprocess`

## ⚙️ Como Configurar
1. Clone o repositório.
2. Crie um arquivo `.env` na raiz com as variáveis:
   ```ini
   SUPABASE_URL=sua_url_de_conexao
   LOCAL_DB_PASS=sua_senha_local
3. Instale as dependências: (`pip install python-dotenv`)
4. Execute: (`backup.py`)
