import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

authenticator = IAMAuthenticator('0WIgFUuKmw3ZU2-sNCLhCjbJEufJWQVY5tx5_GEjCmjj')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

natural_language_understanding.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

response = natural_language_understanding.analyze(
    text='Puede degustar una gran variedad de platos rodeado de un ambiente elegante en el restaurante gourmet Saint Tropez, probar la carne a la parrilla con la inigualable vista a la Isla Gorriti que ofrece Las Brisas, caminar junto a la piscina con los tragos de la temporada en Ovo Pool & Bar o tomar el té de las 17: 00 hs en SOE Bar. Cada espacio dentro del hotel es único porque tiene personalidad y estilo propios que permiten brindar a los clientes un gran abanico de posibilidades.',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True,
                                 limit=2))).get_result()

print(json.dumps(response, indent=2))
