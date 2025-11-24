import os
import sys
import subprocess

PG_BIN = r"C:\Program Files\PostgreSQL\18\bin"
DB_LOCAL_USER = "postgres"
DB_LOCAL_NAME = "postgres"

def carregar_env():
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    caminho_env = os.path.join(pasta_script, ".env")

    if not os.path.exists(caminho_env):
        print(f"Erro: Arquivo .env não encontrado em {caminho_env}")
        return False

    with open(caminho_env, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if "=" in linha and not linha.startswith("#"):
                chave, valor = linha.strip().split("=", 1)
                os.environ[chave] = valor
    return True

def main():
    if not carregar_env():
        sys.exit(1)

    url_supabase = os.environ.get("SUPABASE_URL")
    senha_local = os.environ.get("LOCAL_DB_PASS")

    if not url_supabase or not senha_local:
        print("Erro: Variáveis de ambiente não encontradas no arquivo .env")
        sys.exit(1)

    pg_dump = os.path.join(PG_BIN, "pg_dump.exe")
    psql = os.path.join(PG_BIN, "psql.exe")

    if not os.path.exists(pg_dump):
        print(f"Erro: Executáveis do PostgreSQL não encontrados em {PG_BIN}")
        sys.exit(1)

    arquivo_temp = os.path.join(os.environ["USERPROFILE"], "Desktop", "temp_sync.sql")

    print("Baixando dados do Banco de Dados...")
    cmd_dump = f'"{pg_dump}" "{url_supabase}" --clean --if-exists --no-owner --no-acl -f "{arquivo_temp}"'
    
    try:
        subprocess.run(cmd_dump, check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Erro durante o download dos dados.")
        sys.exit(1)

    print("Importando para o servidor local...")
    cmd_restore = f'"{psql}" -U {DB_LOCAL_USER} -f "{arquivo_temp}" {DB_LOCAL_NAME}'
    
    env_execucao = os.environ.copy()
    env_execucao["PGPASSWORD"] = senha_local

    try:
        subprocess.run(cmd_restore, check=True, shell=True, env=env_execucao)
        print("Processo finalizado com sucesso.")
    except subprocess.CalledProcessError:
        print("Erro durante a importação local.")
        sys.exit(1)
    finally:
        if os.path.exists(arquivo_temp):
            os.remove(arquivo_temp)

if __name__ == "__main__":
    main()