
class Avaliacao:
    """ Classe que representa uma avaliação de um restaurante. """
    def __init__(self, cliente, nota):
        """
        Inicializa uma instância de Avaliacao.
        
        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (int): A nota atribuída ao restaurante (entre 1 e 5).
        """
        self._cliente = cliente
        self._nota = nota

    def __str__(self):
        """Retorna uma representação em string da avaliação."""
        return f'{self.nome} - {self.nota}'