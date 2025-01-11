import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

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

restaurantes = [
    {"nome": "Burger King", "categoria": "Fast Food", "ativo": True},
    {"nome": "Doguinho da Tia", "categoria": "Comida Brasileira", "ativo": False},
    {"nome": "Pizzaria Vale a Pena", "categoria": "Pizzaria", "ativo": False},
]

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
    [4] Sair
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

    restaurantes.append({"nome": nome, "categoria": categoria_escolhida, "ativo": False})
    
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
    table.add_column("Status")
        
    for restaurante in restaurantes:
        nome = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "[green]Ativo[/green]" if restaurante["ativo"] else "[red]Inativo[/red]"
        table.add_row(nome, categoria, ativo)

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
    for restaurante in restaurantes:
        if restaurante["nome"].lower() == nome.lower():
            restaurante["ativo"] = not restaurante["ativo"]
            status = "[green]ativado[/green]" if restaurante["ativo"] else "[red]desativado[/red]"
            console.print(f"[bold]Restaurante '{nome}' foi {status} com sucesso![/bold]")
            break
    else:
        console.print(f"[bold red]Restaurante '{nome}' não encontrado![/bold red]")
    
    Prompt.ask("Pressione [bold yellow]Enter[/bold yellow] para voltar ao menu")
        
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
