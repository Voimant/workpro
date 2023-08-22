import requests
from pprint import pprint


def get_test_re(url):
    response = requests.get(url)
    resp_text = response.text
    return resp_text