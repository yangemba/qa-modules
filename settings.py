with open("settings.txt", "r") as file:
    file.seek(0)
    text = file.readlines()

print(text)

first = text[0]
second = text[1]
third = text[2]
fourth = text[3]
fives = text[4]

print('\n' + first)
print(second)
print(third)


print('\n' + '=== VALUES === '+'\n')


json_value = first.replace('\n', '').split('N:')[1]
print('\n' '1 - ' + json_value)

endpoint_value = second.replace('\n', '').split('nt:')[1]
print('\n' '2 - ' + endpoint_value)

quantity_value = third.replace('\n', '').split('ty:')[1]
print('\n' '3 - ' + quantity_value)

headers_value = fourth.replace('\n', '').split('eaders:')[1]
print('\n' '4 - ' + headers_value)
