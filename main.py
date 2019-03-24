import requests
from settings import *
import bs4

response_list = []
#
# for element in range(quantity_value[0], quantity_value[-1]):
#     data = json_value.replace('{}', f'{element}')
#     response = requests.post(data=data, url=endpoint_value, headers=headers_value)
#     response_list.append(str(response.status_code))

#
# with open("logs.txt", 'w') as file:
#     file.seek(0)
#     file.writelines(response_list)


data = json_value.replace('{}', f'{1}')

data_true = dict(zip(json_value_keys_list,json_value_values_list))


#
print(data_true)
print(quantity_value)

