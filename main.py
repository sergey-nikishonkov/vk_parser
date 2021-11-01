import requests
import csv
import time


def all_inform():
    group_id = input('goup_id: ')
    access_token = input('token: ')
    user = input('number_of_users: ')
    v = 5.131
    count = 1000
    offset = 0
    all_users = []
    print('Собираю информацию')
    while offset < int(user):
        fields = 'bdate, city,contacts, can_write_private_message, connections, online_mobile'
        response = requests.get('https://api.vk.com/method/groups.getMembers', params={'group_id': group_id,
                                                                                           'fields': fields,
                                                                                           'count': count,
                                                                                           'offset': offset,
                                                                                           'access_token': access_token,
                                                                                           'v': v})
        print(response.json())
        data = response.json()['response']['items']
        offset += 1000
        all_users.extend(data)
        time.sleep(0.5)
        print('Собираю информацию')

    return all_users

users = all_inform()

def file_writer(users):
    print('Создаю и записываю файл')
    with open('Users.csv', 'w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Имя', 'Город', 'Дата рождения', 'Телефон', 'Skype', 'Instagram', 'Ссылка'])
    for i in users:
        inf = [''] * 7
        inf[0] = (i['first_name'] + ' ' + i['last_name'])
        inf[1] = i['city']['title'] if i.get('city') else ''
        inf[2] = i.get('bdate', '')
        inf[3] = (i.get('mobile_phone', '') + ' ' + i.get('home_phone', ''))
        inf[4] = i.get('skype', '')
        inf[5] = i.get('instagram', '')
        inf[6] = 'https://vk.com/id' + str(i['id'])
        with open('Users.csv', 'a', newline='',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(inf)
    print('Файл записан')
file_writer(users=users)