import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('0WIgFUuKmw3ZU2-sNCLhCjbJEufJWQVY5tx5_GEjCmjj')
service = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

response = service.analyze(
    url='http://www.cronicasdeleste.com.uy/Noticias/germ%C3%A1n-cardoso-y-eduardo-elinger-denuncian-que-les-hackearon-las-cuentas.html?no_redirect=true',
    features=Features(entities=EntitiesOptions(),
                      keywords=KeywordsOptions())).get_result()

print(json.dumps(response, indent=2))
