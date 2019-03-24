from collections import Counter

with open("settings.txt", "r") as file:
    file.seek(0)
    text = file.readlines()

# print(text)

first = text[0]
second = text[1]
third = text[2]
fourth = text[3]
fives = text[4]

# print('\n' + first)
# print(second)
# print(third)


# print('\n' + '=== VALUES === '+'\n')


json_value = first.replace('\n', '').replace(']', '').split(':[',1)[1]
if json_value[-1] == ',' or json_value[-1] == ' ':
    json_value = 'mistake'

json_list = json_value.split(',')
json_value_keys_list = []
json_value_values_list = []
for element in json_list:
    element_list = element.split(':')
    key = element_list[0]
    value = element_list[1]
    json_value_keys_list.append(key)
    json_value_values_list.append(value)



#
# print('\n' '1 - ' + str(json_list))
# print(json_value_keys_list)
# print(json_value_values_list)



endpoint_value = second.replace('\n', '').split('nt:')[1]
# print('\n' '2 - ' + endpoint_value)

quantity_value_get = third.replace('\n', '').split('ty:')[1].replace('[', '').replace(']', '')
# print('\n' '3 - ' + quantity_value_get)
quantity_value = quantity_value_get.split(',', 1)
# print(quantity_value)

headers_value = fourth.replace('\n', '').split('eaders:')[1]
# print('\n' '4 - ' + headers_value)

control_word_statement = fives.replace('\n', '').split('ord:', 1)[1]
# print(control_word_statement)
control_word_clean = control_word_statement.replace('[', '').replace(']', '')
# print(control_word_clean)
control_word_separate = control_word_clean.count(',')
# print(control_word_separate)
if control_word_separate == 0:
    control_word_value = control_word_clean
elif control_word_separate > 0:
    control_word_value = control_word_clean.split(',')
    if control_word_value[-1] == '':
        control_word_value = 'mistake'
else:
    control_word_value = 'mistake'


# print(control_word_value)












