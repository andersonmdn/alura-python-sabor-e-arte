import factory

from models.avaliacao import Avaliacao

class AvaliacaoFactory(factory.Factory):
    class Meta:
        model = Avaliacao

    cliente = factory.Faker("name", locale="pt_BR")
    nota = factory.Faker("random_int", min=1, max=5)
    #id_restaurante = factory.Faker("random_int", min=1, max=30)