import factory


class QuoteFactory(factory.django.DjangoModelFactory):
    tekst = factory.Faker('bs')

    class Meta:
        model = 'datamodel.Quote'
