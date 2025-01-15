import random
import requests
import factory
import os

from rich.console import Console
from rich.table import Table
# from factories.prato_factory import PratoFactory
# from factories.bebida_factory import BebidaFactory
from factories.restaurante_factory import RestauranteFactory
from factories.avaliacao_factory import AvaliacaoFactory

from database import DatabaseManager

console = Console()

db = DatabaseManager()
db.conectar()
db.drop_tabelas()
db.criar_tabelas()
    
# # Tabela para os pratos
# prato_table = Table(title="Pratos Disponíveis", style="green")
# prato_table.add_column("Nome", style="bold cyan", justify="left")
# prato_table.add_column("Preço", style="bold yellow", justify="right")
# prato_table.add_column("Disponível", style="bold magenta", justify="center")
# prato_table.add_column("Descrição", justify="left")

# # Gerando pratos
# for _ in range(3):
#     prato = PratoFactory()
#     prato_table.add_row(
#         prato._nome,
#         f"R${prato._preco:.2f}",
#         "✅ Sim" if prato._disponibilidade else "❌ Não",
#         prato.descricao,
#     )

# # Exibindo a tabela de pratos
# console.print(prato_table)

# # Descomente para criar tabelas adicionais de bebidas, restaurantes e avaliações.

# # Tabela para bebidas
# bebida_table = Table(title="Bebidas Disponíveis", style="blue")
# bebida_table.add_column("Nome", style="bold cyan", justify="left")
# bebida_table.add_column("Preço", style="bold yellow", justify="right")
# bebida_table.add_column("Disponível", style="bold magenta", justify="center")
# bebida_table.add_column("Tamanho", justify="left")

# for _ in range(10):
#     bebida = BebidaFactory()
#     bebida_table.add_row(
#         bebida._nome,
#         f"R${bebida._preco:.2f}",
#         "✅ Sim" if bebida._disponibilidade else "❌ Não",
#         bebida.tamanho,
#     )
# console.print(bebida_table)

# # Tabela para restaurantes

url = "http://127.0.0.1:8000/restaurantes/"
restaurante_table = Table(title="Restaurantes", style="red")
restaurante_table.add_column("Id", justify="left")
restaurante_table.add_column("Nome", justify="left")
restaurante_table.add_column("Categoria", justify="left")
restaurante_table.add_column("Ativo", justify="center")
restaurante_table.add_column("Banco de Dados", justify="center")

for _ in range(10):
    restaurante = RestauranteFactory()
    if random.randint(0, 1) == 1:
        restaurante.alternar_status()
        
    dados_restaurante = {
        "nome": restaurante.nome,
        "categoria": restaurante.categoria,
        "ativo": True if restaurante.ativo == "Ativo" else False
    }
    
    response = requests.post(url, json=dados_restaurante)
    
    if response.status_code != 201:
        console.print(f"[red]Falha ao criar restaurante: {response.status_code}")
        
    restaurante_table.add_row(
        str(response.json().get("id")),
        response.json().get("nome"),
        response.json().get("categoria"),
        "✅ Sim" if response.json().get("ativo") else "❌ Não",
        "💾 Salvo" if response.status_code == 201 else "❌ Erro",
    )
console.print(restaurante_table)

# Tabela para avaliações

url = "http://127.0.0.1:8000/avaliacoes/"

avaliacao_table = Table(title="Avaliações", style="purple")
avaliacao_table.add_column("Cliente", justify="left")
avaliacao_table.add_column("Nota", justify="right")
avaliacao_table.add_column("ID Restaurante", justify="right")
avaliacao_table.add_column("Banco de Dados", justify="center")

for i in range(30):
    for _ in range(10):
        avaliacao = AvaliacaoFactory()
        
        dados_avaliacao = {
            "cliente": avaliacao.cliente,
            "nota": avaliacao.nota,
            "id_restaurante": i + 1
        }

        response = requests.post(url, json=dados_avaliacao)
        
        if response.status_code != 201:
            console.print(f"[red]Falha ao criar restaurante: {response.status_code}")

        estrelas = "⭐" * avaliacao.nota
        avaliacao_table.add_row(
            avaliacao.cliente,
            f"{avaliacao.nota} {estrelas}",
            str(i + 1),
            "💾 Salvo" if response.status_code == 201 else "❌ Erro",
        )
        
    os.system("cls" if os.name == "nt" else "clear")
    console.print(avaliacao_table)

# # Exemplo de pratos e restaurantes personalizados
# prato_personalizado = PratoFactory(nome="Picanha com Fritas", preco=49.90, descricao="Prato especial da casa")
# console.print(f"[bold blue]Prato Personalizado:[/bold blue] {prato_personalizado._nome}, Preço: [yellow]R${prato_personalizado._preco:.2f}[/yellow], Descrição: [green]{prato_personalizado.descricao}[/green]")

# restaurante_personalizado = RestauranteFactory(nome="Restaurante do Chef", categoria="Brasileira")
# console.print(f"[bold red]Restaurante Personalizado:[/bold red] {restaurante_personalizado._nome}, Categoria: [yellow]{restaurante_personalizado._categoria}[/yellow]")

db.fechar_conexao()