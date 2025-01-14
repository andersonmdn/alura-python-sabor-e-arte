from models.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    """ Classe que representa um prato. """
    def __init__(self, nome, preco, descricao):
        """ Inicializa uma instância de Prato. """
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        """ Retorna uma representação em string do prato. """
        return f"Prato: {self._nome}, Preço: {self._preco}, Descrição: {self.descricao}, Ativo: {self._ativo}"
    
    def aplicar_desconto(self):
        """ Aplica um desconto ao preço do prato. """
        
        self._preco -= (self._preco * 0.1)
        
        self._preco = round(self._preco, 2)