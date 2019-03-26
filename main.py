import requests
from settings import *
import bs4
import time
import json

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

    response_list.append(str(response.status_code))
    time.sleep(2)


if response_list:
    with open("logs.txt", 'w') as file:
        file.seek(0)
        file.writelines(response_list)


# data = json_value.replace('{}', f'{1}')
#
# data_true = dict(zip(json_value_keys_list, json_value_values_list))
#
#
# #
# print(data_true)
# print(quantity_value)
#
