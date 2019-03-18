import requests


url = 'http://users.bugred.ru/user/register/index.html'
response_list = []
for element in range(7, 9):
    data = {
        "name": "yanaparat{}".format(element),
        "email": "superyanaparat{}@gmail.com".format(element),
        "password": "1",
        "act_register_now": "Зарегистрироваться"
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(data=data, url=url, headers=headers)
    response_list.append(str(response))

with open('logs.txt', 'w') as file:
    file.seek(0)
    file.writelines(response_list)
