import sqlite3
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

def criar_conexao():
    db_path = "restaurante.db"
    
    try:
        conn = sqlite3.connect(db_path)
        console.log(f"[green]Conexão com o banco de dados '{db_path}' foi estabelecida com sucesso![/green]")
        return conn
    except sqlite3.Error as e:
        console.log(f"[red]Erro ao conectar ao banco de dados: {e}[/red]")
        return None

def get_connection():
    return criar_conexao()

def criar_tabelas(conn):
    comandos_sql = [
        {
            "tabela": "restaurantes",
            "query": """
            CREATE TABLE IF NOT EXISTS restaurantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                ativo BOOLEAN DEFAULT 0
            );
            """
        },
        {
            "tabela": "avaliacoes",
            "query": """
            CREATE TABLE IF NOT EXISTS avaliacoes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                nota INTEGER NOT NULL CHECK(nota BETWEEN 1 AND 5),
                restaurante_id INTEGER NOT NULL,
                FOREIGN KEY (restaurante_id) REFERENCES restaurante(id) ON DELETE CASCADE
            );
            """
        },
        {
            "tabela": "pratos",
            "query": """
            CREATE TABLE IF NOT EXISTS pratos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                disponibilidade BOOLEAN DEFAULT 1,
                descricao TEXT NOT NULL,
                restaurante_id INTEGER NOT NULL,
                FOREIGN KEY (restaurante_id) REFERENCES restaurante(id) ON DELETE CASCADE
            );
            """
        },
        {
            "tabela": "bebidas",
            "query": """
            CREATE TABLE IF NOT EXISTS bebidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                disponibilidade BOOLEAN DEFAULT 1,
                tamanho TEXT NOT NULL,
                restaurante_id INTEGER NOT NULL,
                FOREIGN KEY (restaurante_id) REFERENCES restaurante(id) ON DELETE CASCADE
            );
            """
        }
    ]

    for comando in comandos_sql:
        try:
            conn.execute(comando["query"])
        except sqlite3.Error as e:
            console.log(f"[red]Erro ao criar tabela {comando['tabela']}: {e}[/red]")
        else:
            console.log(f"[green]Tabela [bold]{comando['tabela']}[/bold] criada com sucesso![/green]")

def fechar_conexao(conn):
    conn.close()
    console.log(f"[blue]Conexão com o banco de dados foi encerrada.[/blue]")

def main():
    conn = criar_conexao()
    if conn is None:
        return

    criar_tabelas(conn)

    conn.close()
    console.log(f"[blue]Conexão com o banco de dados foi encerrada.[/blue]")

if __name__ == "__main__":
    main()
