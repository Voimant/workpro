import requests
import base64
from pprint import pprint




# BASE_URL = 'http://demo5.autocrm.ru/yii/api/address'
# BASE_URL2 = 'https://demo5.autocrm.ru/yii/api/saleUsedStage/schedule'
# BASE_URL3 = 'https://demo5.autocrm.ru/yii/api/retailCase'
# BASE_URL4 = 'https://demo5.autocrm.ru/yii/api/autosalon'
# BASE_URL5 = 'https://demo5.autocrm.ru/yii/api/refBrand'
# BASE_URL6 = 'https://demo5.autocrm.ru/yii/api/refModel'




def car_for_testdrive():
    BASE_URL7 = 'https://echoauto.autocrm.ru/yii/api/warehouseVehicle'
    login = '3goq7PuUrZdiNttGebNlISJh7jRuOKMK'
    response = requests.get(BASE_URL7, headers={'Authorization': f'Bearer {login}'}, params={"isForTestDrive": 1})
    x = response.json()
    keyboard = []
    for cars in x['result']:
        brand = cars['base']['brand']['name']
        model = cars['base']['model']['name']
        brand_id = cars['base']['brand']['id']
        model_id = cars['base']['model']['id']
        keyboard.append({f"{brand} {model}": {"brand_id": brand_id, "model_id": model_id}})
    return(keyboard)


# pprint(x['result'])

pprint(car_for_testdrive())


def create_work_list(brand_id, model_id):
    base_url = 'https://echoauto.autocrm.ru/yii/api/retailCase'
    login = '3goq7PuUrZdiNttGebNlISJh7jRuOKMK'
    file_2 = {
        'salonId': 9,
        'primaryContactType': 11,
        'assigneedId': 0,
        'brandId': int(brand_id),
        'modelId': int(model_id)
    }
    response = requests.post(base_url, headers={'Authorization': f'Bearer {login}'}, json=file_2)
    pprint(response.text)


def create_lead(first_name, phone, brand_id, model_id):
    login = '3goq7PuUrZdiNttGebNlISJh7jRuOKMK'
    base_url = 'https://echoauto.autocrm.ru/yii/api/leads/request'
    json_body = {
        'salon_id': 9,
        'type': 11,
        'request_type_id': '1',
        'client_type': 'individual',
        'first_name': first_name,
        'phone': phone,
        'source_id': '22',
        'brand_id': int(brand_id),
        'model_id': int(model_id)
    }
    response = requests.post(base_url, headers={'Authorization': f'Bearer {login}'}, json=json_body)
    print(response.json())
    return response.json()