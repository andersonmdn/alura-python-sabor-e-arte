# Gerenciamento de Restaurantes 🎉

Este projeto é uma aplicação simples de console desenvolvida em Python que permite o gerenciamento de restaurantes, com funcionalidades para cadastrar, listar e ativar/desativar restaurantes. Ele utiliza o pacote `Rich` para exibir saídas estilizadas no terminal. 🎨✨✅

## Funcionalidades 🍽️

- **Cadastrar Restaurante**: Permite adicionar novos restaurantes com um nome e uma categoria escolhida de uma lista predefinida.
- **Listar Restaurantes**: Exibe uma tabela com o nome, categoria e status (ativo/inativo) de todos os restaurantes cadastrados.
- **Ativar/Desativar Restaurante**: Permite alternar o status de um restaurante cadastrado.
- **Sair**: Finaliza o programa.

## Requisitos 📦

- Python 3.7 ou superior
- Biblioteca `Rich`

### Instalação do Rich 📥

Para instalar o pacote `Rich`, execute o seguinte comando:

```bash
pip install rich
```

## Como executar o projeto ▶️

1. Clone este repositório ou copie os arquivos para o seu ambiente local.
2. Certifique-se de ter o Python e o pacote `Rich` instalados.
3. Execute o script principal com o seguinte comando:

```bash
python app.py
```

Substitua `app.py` pelo nome do arquivo Python que contém o código.

## Estrutura do Projeto 📁

O projeto consiste em um único arquivo Python com as seguintes funções principais:

- `limpar_tela`: Limpa o console de acordo com o sistema operacional.
- `exibir_titulo`: Exibe o título estilizado no console.
- `exibir_menu`: Mostra o menu principal.
- `finalizar_programa`: Encerra o programa com uma mensagem.
- `opcao_invalida`: Informa o usuário sobre uma opção inválida.
- `cadastrar_restaurante`: Permite cadastrar um novo restaurante.
- `listar_restaurantes`: Lista todos os restaurantes cadastrados.
- `alternar_status_restaurante`: Altera o status de um restaurante para ativo ou inativo.
- `escolher_opcao`: Gerencia a navegação no menu com base na escolha do usuário.
- `main`: Loop principal do programa.

## Exemplo de Uso 🖥️

Ao executar o programa, será exibido o seguinte menu:

```
[1] Cadastrar restaurante
[2] Listar restaurantes
[3] Ativar/Desativar restaurante
[4] Sair
```

- Escolha uma opção digitando o número correspondente.
- Siga as instruções exibidas no console para completar a ação escolhida.
- Para sair, escolha a opção `[4] Sair`.

## Personalização ⚙️

Você pode personalizar a lista de categorias de restaurantes alterando a variável `categorias_restaurantes` no início do código.

## Melhorias Futuras 🔮

- Adicionar persistência dos dados (ex.: salvar e carregar restaurantes de um arquivo).
- Permitir edição de informações de restaurantes.
- Criar filtros para listar restaurantes por categoria ou status.

