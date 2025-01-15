import sqlite3
from rich.console import Console
from rich.table import Table
from rich.progress import track

class DatabaseManager:
    def __init__(self, db_path="restaurante.db"):
        self.db_path = db_path
        self.console = Console()
        self.conn = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.console.log(f"[green]Conexão com o banco de dados '{self.db_path}' foi estabelecida com sucesso![/green]")
        except sqlite3.Error as e:
            self.console.log(f"[red]Erro ao conectar ao banco de dados: {e}[/red]")
            self.conn = None

    def drop_tabelas(self):
        if not self.conn:
            self.console.log("[red]Conexão não estabelecida. Não é possível deletar tabelas.[/red]")
            return

        tabelas = ["restaurantes", "avaliacoes", "pratos", "bebidas"]

        for tabela in tabelas:
            try:
                self.executar(f"DROP TABLE IF EXISTS {tabela};")
                self.console.log(f"[blue]Tabela [bold]{tabela}[/bold] deletada com sucesso![/blue]")
            except sqlite3.Error as e:
                self.console.log(f"[red]Erro ao deletar tabela {tabela}: {e}[/red]")
    
    def criar_tabelas(self):
        if not self.conn:
            self.console.log("[red]Conexão não estabelecida. Não é possível criar tabelas.[/red]")
            return

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
                    FOREIGN KEY (restaurante_id) REFERENCES restaurantes(id) ON DELETE CASCADE
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
                    FOREIGN KEY (restaurante_id) REFERENCES restaurantes(id) ON DELETE CASCADE
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
                    FOREIGN KEY (restaurante_id) REFERENCES restaurantes(id) ON DELETE CASCADE
                );
                """
            }
        ]

        for comando in comandos_sql:
            try:
                # self.conn.execute(comando["query"])
                self.executar(comando["query"])
                self.console.log(f"[green]Tabela [bold]{comando['tabela']}[/bold] criada com sucesso![/green]")
            except sqlite3.Error as e:
                self.console.log(f"[red]Erro ao criar tabela {comando['tabela']}: {e}[/red]")

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.console.log(f"[blue]Conexão com o banco de dados foi encerrada.[/blue]")

    def executar(self, query, log=False, retry_count=0):
        if not self.conn:
            if retry_count >= 3:
                self.console.log("[red]Falha ao reconectar após várias tentativas.[/red]")
                return None
            self.console.log("[red]Conexão não estabelecida. Tentando reconectar.[/red]")
            self.conectar()
            return self.executar(query, log, retry_count + 1)

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            if log: self.console.log("[green]Query executada com sucesso![/green]")
        except sqlite3.Error as e:
            self.console.log(f"[red]Erro ao executar query: {e}[/red]")
            
        return cursor
    
    def get_cursor(self):
        if not self.conn:
            self.console.log("[red]Conexão não estabelecida. Tentando reconectar.[/red]")
            self.conectar()
            return self.get_cursor()

        return self.conn.cursor()
    
    def commit(self):
        if not self.conn:
            return

        self.conn.commit()
    
if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.conectar()
    db_manager.drop_tabelas()
    db_manager.criar_tabelas()
    db_manager.fechar_conexao()
