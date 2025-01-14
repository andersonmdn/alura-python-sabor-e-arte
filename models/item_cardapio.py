from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    """ Classe abstrata que representa um item de cardápio. """
    def __init__(self, nome, preco):
        """
            Inicializa uma instância de ItemCardapio.
            
            Parâmetros:
            - nome (str): O nome do item.
            - preco (float): O preço do item.
        """
        self._nome = nome.title()
        self._preco = round(preco, 2)
        self._disponibilidade = True
        
    @abstractmethod
    def aplicar_desconto(self):
        """Aplica um desconto ao preço do item."""
        pass
    
    @property
    def ativo(self):
        """Retorna um texto indicando o estado de atividade do item."""
        
        return "Ativo" if self._ativo else "Inativo"