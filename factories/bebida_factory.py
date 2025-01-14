import factory

from models.bebida import Bebida

class BebidaFactory(factory.Factory):
    class Meta:
        model = Bebida

    nome = factory.Faker("sentence", locale="pt_BR", nb_words=3)
    preco = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)
    # disponibilidade = factory.Faker("boolean")
    tamanho = factory.Iterator(["Pequeno", "Médio", "Grande"])