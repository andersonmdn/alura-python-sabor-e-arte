import factory

from models.restaurante import Restaurante

class RestauranteFactory(factory.Factory):
    class Meta:
        model = Restaurante

    nome = factory.Faker("company", locale="pt_BR")
    categoria = factory.Iterator(["Italiana", "Japonesa", "Brasileira", "Mexicana", "Francesa"])
    # ativo = factory.Faker("boolean")