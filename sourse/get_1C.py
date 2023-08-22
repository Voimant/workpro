import requests
from bs4 import BeautifulSoup as BS
import ast
from sourse.get_req import req_xml



def get_request_1C(gos, vin):
    BASE_URL = ' Http://ws.echoauto.ru:44382/AutoServiceWork/ws/AutoServiceWork/RepairStatus'
    data2 = req_xml(gos, vin)
    response = requests.post(BASE_URL, data=data2)
    soup = BS(response.text, 'html.parser')
    date = soup.find('m:return')
    soup_dict = ast.literal_eval(date.text)


    return(soup_dict)