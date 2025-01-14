from models.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    """ Classe que representa uma bebida. """
    def __init__(self, nome, preco, tamanho):
        """
            Inicializa uma instância de Bebida.
            
            Parâmetros:
            - nome (str): O nome da bebida.
            - preco (float): O preço da bebida.
            - tamanho (str): O tamanho da bebida.
        """
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        """ Retorna uma representação em string da bebida. """
        return f"Bebida: {self._nome}, Preço: {self._preco}, Tamanho: {self.tamanho}, Ativo: {self._ativo}"
    
    def aplicar_desconto(self):
        """ Aplica um desconto ao preço da bebida. """
        self._preco -= self._preco * 0.05
        
        self._preco = round(self._preco, 2)