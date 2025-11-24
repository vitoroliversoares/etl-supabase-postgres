# Automação de backup ETL (PostgreSQL & Supabase)

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
   ```env
   SUPABASE_URL=sua_url_de_conexao
   LOCAL_DB_PASS=sua_senha_local
   Instale as dependências: pip install python-dotenv
   Execute: backup.py
   ```
