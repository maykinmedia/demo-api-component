from zds_schema.conf.api import *  # noqa - imports white-listed

API_1_VERSION = '1.0.1'
API_2_VERSION = '2.1.0'

REST_FRAMEWORK = BASE_REST_FRAMEWORK.copy()
REST_FRAMEWORK.update({
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_VERSION': '2',
    'ALLOWED_VERSIONS': ('1', '2', ),
})

SECURITY_DEFINITION_NAME = 'JWT-Claims'

SWAGGER_SETTINGS = BASE_SWAGGER_SETTINGS.copy()
SWAGGER_SETTINGS.update({
    'DEFAULT_INFO': 'demo_api.api.schema.info',
    'SECURITY_DEFINITIONS': {
        SECURITY_DEFINITION_NAME: {
            # OAS 3.0
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
            # not official...
            # 'scopes': {},  # TODO: set up registry that's filled in later...

            # Swagger 2.0
            # 'name': 'Authorization',
            # 'in': 'header'
            # 'type': 'apiKey',
        }
    },
    'DEFAULT_FIELD_INSPECTORS': BASE_SWAGGER_SETTINGS['DEFAULT_FIELD_INSPECTORS'][1:],
})
