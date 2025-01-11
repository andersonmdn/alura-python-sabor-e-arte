
from modelos.avaliacao import Avaliacao

class Restaurante:
    """ Classe que representa um restaurante. """
    
    restaurantes = []
    
    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        
        return f"Restaurante(nome={self._nome}, categoria={self._categoria}, status={self._ativo})"
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status")
        
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")
            
    @property
    def ativo(self):
        """Retorna um texto indicando o estado de atividade do restaurante."""
        
        return "Ativo" if self._ativo else "Inativo"
    
    def alternar_status(self):
        """Alterna o estado de atividade do restaurante."""
        
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return 'Sem avaliações'
        
        total = sum(avaliacao._nota for avaliacao in self._avaliacao)
        
        return round(total / len(self._avaliacao), 1)
    
    @property
    def nome(self):
        """Retorna um texto indicando o nome do restaurante."""
        return self._nome

    @property
    def categoria(self):
        """Retorna um texto indicando a categoria do restaurante."""
        return self._categoria