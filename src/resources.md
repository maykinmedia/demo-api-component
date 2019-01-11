# Resources

Dit document beschrijft de (RGBZ-)objecttypen die als resources ontsloten
worden met de beschikbare attributen.


## Quote

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/quote)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | De volledige resource identifier als URL. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| tekst | De tekst van de quote. | string | ja | C​R​U​D |
| bronNaam | Naam van de bron. | string | ja | C​R​U​D |
| bronLink | Link naar de oorspronkelijke bron. | string | nee | C​R​U​D |
| aangemaakt | Datum en tijd van wanneer het object is aangemaakt. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| laatstBijgewerkt | Datum en tijd van wanneer het object voor het laatst is bijgewerkt. | string | nee | C​R​U​D |


* Create, Read, Update, Delete
