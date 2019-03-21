

with open("settings.txt", "r") as file:
    file.seek(0)
    text = file.readlines()

print(text)

first = text[0]
second = text[1]
third = text[2]

print('\n' + first)
print(second)
print(third)
print('\n' + '=== VALUES === '+'\n')


json_value = first.replace('\n', '').split('N:')[1]
print('\n' + json_value)

endpoint_value = second.replace('\n', '').split('nt:')[1]
print('\n' + endpoint_value)


