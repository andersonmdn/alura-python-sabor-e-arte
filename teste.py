
# import os

# from modelos.restaurante import Restaurante
# from modelos.cardapio.bebida import Bebida
# from modelos.cardapio.prato import Prato

# os.system("cls" if os.name == "nt" else "clear")

# restaurante = Restaurante("Cantina da Mama", "Massas")

# prato = Prato("Feijoada", 30.02, "Feijoada completa com arroz, couve, farofa e laranja")
# prato.aplicar_desconto()
# restaurante.adicionar_item_cardapio(prato)


# prato = Prato("Macarronada", 25.10, "Macarronada com molho bolonhesa e queijo ralado")
# prato.aplicar_desconto()
# restaurante.adicionar_item_cardapio(prato)

# bebida = Bebida("Coca-Cola", 5.54, "Lata")
# restaurante.adicionar_item_cardapio(bebida)

# bebida = Bebida("Coca-Cola", 7.31, "Garrafa")
# restaurante.adicionar_item_cardapio(bebida)

# restaurante.lista_cardapio()

import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    restaurantes_json = response.json()
    dados_restaurante = {}
    
    for restaurante in restaurantes_json:
        nome_restaurante = restaurante['Company']
        
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
            
        dados_restaurante[nome_restaurante].append({
            "item": restaurante['Item'],
            "preco": restaurante['price'],
            "descricao": restaurante['description']
        })
        
    
else:
    print("Erro ao acessar a API de restaurantes.")
    
for nome_restaurante, cardapio in dados_restaurante.items():
    nome_arquivo = nome_restaurante.lower().replace(" ", "_") + ".json"
    
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(cardapio, arquivo, indent=4)