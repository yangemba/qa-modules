import requests
from settings import *
import bs4
import time
import json
import logging

response_list = []

for element in range(int(quantity_value[0]), int(quantity_value[-1])):
    s = []
    t = []
    for value in json_value_values_list:
        # print(value)
        k = value.replace('{}', str(element)).replace('"', '')
        s.append(k)
    for key in json_value_keys_list:
        k = key.replace('"', '')
        t.append(k)
    data = dict(zip(t, s))
    json_ob = json.dumps(data)
    print(data)
    response = requests.post(data=data, url=endpoint_value, headers={"Content-Type": "application/x-www-form-urlencoded"})

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    html_text = str(soup)
    if type(control_word_value) == str:
        print("\n\n STR")
        if control_word_value in html_text:
            response_list.append(f' {element} - OK')
        else:
            response_list.append(f' {element} - BAD')
    if type(control_word_value) == list:
        print("\n\n LIST")
        number = len(control_word_value)
        counter = 0
        for keyword in control_word_value:
            if keyword in html_text:
                counter = counter + 1
        if counter == number:
            response_list.append(f' {element} - OK')
        else:
            response_list.append(f' {element} - BAD')

    # response_list.append(str(response.status_code))

with open("logs.txt", 'w') as file:
    file.seek(0)
    file.write(str(time.ctime()))
    for element in response_list:
        file.write(f'\n{element}')


# data = json_value.replace('{}', f'{1}')
#
# data_true = dict(zip(json_value_keys_list, json_value_values_list))
#
#
# #
# print(data_true)
# print(quantity_value)
#
