import factory

from models.prato import Prato

class PratoFactory(factory.Factory):
    class Meta:
        model = Prato

    nome = factory.Faker("word", locale="pt_BR")
    preco = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)
    # disponibilidade = factory.Faker("boolean")
    descricao = factory.Faker("sentence", nb_words=6, locale="pt_BR")