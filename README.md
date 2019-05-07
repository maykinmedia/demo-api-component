
Demo API Component


Version: 2.1.0
Source: https://github.com/maykinmedia/demo-api-component
Keywords: VNG, VNG-realisatie, demo, api
PythonVersion: 3.6

|build-status| |requirements|

[![Status badge](https://img.shields.io/endpoint.svg?style=for-the-badge&amp;url=https://vng-staging.maykin.nl/api/v1/provider-run-shield/127/)](https://vng-staging.maykin.nl/server/33418afd-e667-4892-96ed-4124fe21c54e)

Een voorbeeld van een OAS 3.0 API met bijbehorende referentie implementatie.
Deze repository is hoofdzakelijk voor intern gebruik bij VNG.

De OAS 3.0 specificatie staat in de `API specificatie repository`_.


Inleiding

Om verschillende zaken gerelateerd aan het nieuwe API-landschap te begrijpen,
beheren, ontwikkelen, uitrollen, testen, etc. kan deze repository gebruikt 
worden.

Het is een volledig werkende API met 1 resource en endpoint en is een
vereenvoudigde weergave van allerlei (ontwerp)beslissingen aangaande gebruikte
technieken zoals RESTful APIs, Docker, OAS 3.0, versiebeheer, etc.

Het component is te testen op de `testomgeving`_.


Documentatie

Zie ``INSTALL.rst`` voor installatie instructies en beschikbare commando's.


Referenties

* `API specificatie repository`_
* `Issues <https://github.com/maykinmedia/demo-api-component/issues>`_
* `Code <https://github.com/maykinmedia/demo-api-component>`_


.. |build-status| image:: http://jenkins.nlx.io/buildStatus/icon?job=demo-api-component-stable
    :alt: Build status
    :target: http://jenkins.nlx.io/job/demo-api-component-stable

.. |requirements| image:: https://requires.io/github/maykinmedia/demo-api-component/requirements.svg?branch=master
     :target: https://requires.io/github/maykinmedia/demo-api-component/requirements/?branch=master
     :alt: Requirements status

.. _testomgeving: https://ref.tst.vng.cloud/demo-api/
.. _API specificatie repository: https://github.com/maykinmedia/demo-api


Licentie

Copyright © VNG Realisatie 2019

Licensed under the EUPL_

.. _EUPL: LICENCE.md
