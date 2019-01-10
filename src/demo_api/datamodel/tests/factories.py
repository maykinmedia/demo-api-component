import factory


class QuoteFactory(factory.django.DjangoModelFactory):
    tekst = factory.Faker('bs')
    bron_naam = factory.Faker('word')

    class Meta:
        model = 'datamodel.Quote'
