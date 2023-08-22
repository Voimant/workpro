import requests
import base64
from pprint import pprint




BASE_URL = 'http://demo5.autocrm.ru/yii/api/address'

login = 'tx7bGz3qmvafFMCdilBAKqsc6zzYFeo0'
log_encode = login.encode('ascii')
base64_log = base64.b64encode(log_encode)
base64_mess = base64_log.decode('ascii')

response = requests.get(BASE_URL, headers={'Authorization': f'Bearer {login}'}, params={'id': 3})
pprint(base64_mess)
pprint(response.json())

class Infotech:
    def __init__(self, login, base_url):
        self.base_url = base_url
        self.login = login
        self.auth = {'Authorization': f'Bearer {login}'}


    def adress(self):

