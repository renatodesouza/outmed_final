import requests
import json
#Docs https://developers.mercadolivre.com.br/pt_br/api-docs-pt-br

user_id = '164975144'
access_token = ''
url = f'https://api.mercadolibre.com/users/me?access_token=${access_token}'
public_endpoint_url = f'https://api.mercadolibre.com/users/{user_id}/'
private_endpoint_url = f'https://api.mercadolibre.com/users/{user_id}?access_token=${access_token}'