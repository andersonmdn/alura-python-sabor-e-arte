import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

from modelos.restaurante import Restaurante

console = Console()

categorias_restaurantes = [
    "Fast Food",
    "Comida Brasileira",
    "Pizzaria",
    "Churrascaria",
    "Comida Japonesa",
    "Comida Chinesa",
    "Italiana",
    "Cafeteria",
    "Vegetariana/Vegana",
    "Comida Árabe",
    "Frutos do Mar",
    "Hamburgueria",
    "Doceria/Sorveteria",
    "Comida Indiana",
    "Bar e Petiscos"
]

# restaurantes = [
#     {"nome": "Burger King", "categoria": "Fast Food", "ativo": True},
#     {"nome": "Doguinho da Tia", "categoria": "Comida Brasileira", "ativo": False},
#     {"nome": "Pizzaria Vale a Pena", "categoria": "Pizzaria", "ativo": False},
# ]

def limpar_tela():
    """
    Limpa o console de acordo com o sistema operacional.

    Input: Nenhum.
    Output: Nenhum. Limpa a tela do console.
    """
    os.system("cls" if os.name == "nt" else "clear")

def exibir_titulo():
    """
    Exibe o título estilizado no console.

    Input: Nenhum.
    Output: Título estilizado impresso no console.
    """
    console.print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗  ░█████╗░██████╗░████████╗███████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░  ███████║██████╔╝░░░██║░░░█████╗░░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░  ██╔══██║██╔══██╗░░░██║░░░██╔══╝░░
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗  ██║░░██║██║░░██║░░░██║░░░███████╗
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝      
    """)

def exibir_menu():
    """
    Exibe o menu principal no console.

    Input: Nenhum.
    Output: Menu impresso no console.
    """
    menu = """
    [1] Cadastrar restaurante
    [2] Listar restaurantes
    [3] Ativar/Desativar restaurante
    [4] Receber avaliação
    [5] Incluir Exemplos
    [6] Sair
    """
    console.print(menu)

def finalizar_programa():
    """
    Finaliza o programa com uma mensagem.

    Input: Nenhum.
    Output: Mensagem de encerramento impressa no console.
    """
    console.print("[bold red]Encerrando o programa...[/bold red]")
    limpar_tela()

def opcao_invalida():
    """
    Exibe uma mensagem para opções inválidas no menu.

    Input: Nenhum.
    Output: Mensagem de erro impressa no console.
    """
    console.print("[bold red]Opção inválida![/bold red]")
    Prompt.ask("Pressione [bold yellow]Enter[/bold yellow] para voltar ao menu")

def cadastrar_restaurante():
    """
    Permite ao usuário cadastrar um restaurante.

    Input:
        - Nome do restaurante (str).
        - Categoria do restaurante (escolhida a partir de uma lista de categorias).

    Output:
        - Restaurante adicionado à lista global `restaurantes`.
        - Mensagem de sucesso exibida no console.
    """
    limpar_tela()
    console.print("[bold]Cadastrar restaurante[/bold]")
    nome = Prompt.ask("[bold]Nome do restaurante[/bold]")
    
    print("\nSelecione uma categoria para o restaurante:")
    for i, categoria in enumerate(categorias_restaurantes, start=1):
        print(f"[{i}] {categoria}")
    
    escolha = int(Prompt.ask("\nDigite o número da categoria desejada"))
    categoria_escolhida = categorias_restaurantes[escolha - 1]

    # restaurantes.append({"nome": nome, "categoria": categoria_escolhida, "ativo": False})
    Restaurante(nome, categoria_escolhida)
    
    console.print(f"[bold]Restaurante [green]'{nome}'[/green] da categoria [green]'{categoria_escolhida}'[/green] foi criado com sucesso![/bold]")
    Prompt.ask("Pressione [bold yellow]Enter[/bold yellow] para voltar ao menu")

def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados no sistema.

    Input: Nenhum.
    Output:
        - Tabela com nome, categoria e status de cada restaurante exibida no console.
    """
    limpar_tela()
    console.print("[bold]Listar restaurantes[/bold]")
    
    table = Table(show_header=True, show_lines=True)
    table.add_column("Nome")
    table.add_column("Categoria")
    table.add_column("Avaliação")
    table.add_column("Status")
        
    for restaurante in Restaurante.restaurantes:
        nome = restaurante.nome
        categoria = restaurante.categoria
        media = restaurante.media_avaliacoes
        ativo = f"[green]{restaurante.ativo}[/green]" if restaurante.ativo == "Ativo" else f"[red]{restaurante.ativo}[/red]"
        
        nota_str = "⭐" * int(media) + f" ({media})" if media != "Sem avaliações" else "Sem avaliações"
        table.add_row(nome, categoria, f"{nota_str}",ativo)

    console.print(table)

    Prompt.ask("Pressione [bold yellow]Enter[/bold yellow] para voltar ao menu")

def alternar_status_restaurante():
    """
    Ativa ou desativa o status de um restaurante.

    Input:
        - Nome do restaurante (str).

    Output:
        - Status do restaurante alterado.
        - Mensagem de sucesso ou erro exibida no console.
    """
    limpar_tela()
    console.print("[bold]Ativar/Desativar restaurante[/bold]")
    
    nome = Prompt.ask("[bold]Digite o nome do restaurante que deseja ativar/desativar[/bold]")
    for restaurante in Restaurante.restaurantes:
        if restaurante.nome.lower() == nome.lower():
            restaurante.alternar_status()
            status = f"[green]Ativado[/green]" if restaurante.ativo == "Ativo" else f"[red]Desativado[/red]"
            console.print(f"[bold]Restaurante '{nome}' foi {status} com sucesso![/bold]")
            break
    else:
        console.print(f"[bold red]Restaurante '{nome}' não encontrado![/bold red]")
    
    Prompt.ask("Pressione [bold yellow]Enter[/bold yellow] para voltar ao menu")
        
def receber_avaliacao():
    """
    Recebe uma avaliação para um restaurante.

    Input:
        - Nome do restaurante (str).
        - Nome do cliente (str).
        - Nota da avaliação (float).

    Output:
        - Avaliação adicionada ao restaurante.
        - Mensagem de sucesso ou erro exibida no console.
    """
    limpar_tela()
    console.print("[bold]Receber avaliação[/bold]")
    
    nome_restaurante = Prompt.ask("[bold]Digite o nome do restaurante que deseja avaliar[/bold]")
    nome_cliente = Prompt.ask("[bold]Digite o nome do cliente que esta avaliando[/bold]")
    nota = float(Prompt.ask("[bold]Digite a nota da avaliação (de 0 a 5)[/bold]"))
    
    for restaurante in Restaurante.restaurantes:
        if restaurante.nome.lower() == nome_restaurante.lower():
            restaurante.receber_avaliacao(nome_cliente, nota)
            
            # Vamos criar a string corretamente com o caractere '⭐' multiplicado por 'nota'
            nota_str = "⭐" * int(nota)
            console.print(f"[bold]Avaliação de [green]{nota_str}[/green] recebida com sucesso para o restaurante '{nome_restaurante}'![/bold]")

            break
    else:
        console.print(f"[bold red]Restaurante '{nome_restaurante}' não encontrado![/bold red]")
    
    Prompt.ask("Pressione [bold yellow]Enter[/bold yellow] para voltar ao menu")

def incluir_exemplos():
    """
    Inclui exemplos de restaurantes à lista global `restaurantes`.

    Input: Nenhum.
    Output: Restaurantes adicionados à lista global `restaurantes
    """
    
    restaurante = Restaurante("Burger King", "Fast Food")
    restaurante.receber_avaliacao("João", 4)
    restaurante.receber_avaliacao("Maria", 5)
    restaurante.receber_avaliacao("José", 3)
    restaurante.receber_avaliacao("Ana", 2)
    
    restaurante = Restaurante("Dogão da Tia", "Comida Brasileira")
    restaurante.receber_avaliacao("João", 5)
    restaurante.receber_avaliacao("Maria", 4)
    restaurante.receber_avaliacao("José", 3)
    restaurante.receber_avaliacao("Ana", 2)
    restaurante.receber_avaliacao("Pedro", 1)
    
    restaurante = Restaurante("MC Donalds", "Fast Food")
    restaurante.receber_avaliacao("João", 5)
    restaurante.receber_avaliacao("Maria", 4)
    restaurante.receber_avaliacao("José", 3)
    
    restaurante = Restaurante("Pizzaria do Zé", "Pizzaria")
    restaurante.receber_avaliacao("João", 5)
    restaurante.receber_avaliacao("Maria", 4)
    restaurante.receber_avaliacao("José", 3)
    
    restaurante = Restaurante("Churrascaria do Gaúcho", "Churrascaria")
    restaurante.receber_avaliacao("João", 5)
    restaurante.receber_avaliacao("Maria", 4)
    restaurante.receber_avaliacao("José", 3)
    restaurante.receber_avaliacao("Ana", 2)
    restaurante.receber_avaliacao("Pedro", 1)
    restaurante.receber_avaliacao("Carlos", 5)
    restaurante.receber_avaliacao("Mariana", 4)

def escolher_opcao():
    """
    Gerencia a navegação no menu principal com base na escolha do usuário.

    Input:
        - Opção do menu escolhida pelo usuário (int).

    Output:
        - Execução da opção escolhida ou mensagem de erro.
        - Retorna `False` para sair do programa ou `True` para continuar.
    """
    try:
        opcao_escolhida = IntPrompt.ask("[bold green]Escolha uma opção[/bold green]")
        console.print(f"[bold cyan]Opção escolhida:[/bold cyan] {opcao_escolhida}")
        
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            receber_avaliacao()
        elif opcao_escolhida == 5:
            incluir_exemplos()
        elif opcao_escolhida == 6:
            finalizar_programa()
            return False
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()
    except KeyboardInterrupt:
        return False
        
    return True

def main():
    """
    Executa o loop principal do programa, exibindo o menu e aguardando ações do usuário.

    Input: Nenhum.
    Output: Execução contínua do programa até o usuário sair.
    """
    continuar = True
    while continuar:
        limpar_tela()
        exibir_titulo()
        exibir_menu()
        continuar = escolher_opcao()
        console.print()

if __name__ == "__main__":
    main()
