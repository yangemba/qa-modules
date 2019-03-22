import requests
from settings import *
import bs4


response_list = []

for element in range(quantity_value):
    data = json_value.replace('{}', f'{element}')
    response = requests.post(data=data, url=endpoint_value, headers=headers_value)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    text = str(soup)
    check_list = text.split()

















