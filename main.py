import requests
import csv
import time


def all_usrs():
    group_id = input('goup_id: ')
    access_token = input('token: ')
    users_count = input('number_of_users: ')
    params = {
        'group_id': group_id,
        'access_token': access_token,
        'fields': fields,
        'count': 1000,
        'offset': 0,
        'v': 5.31
    }
    users = []    
    while offset < int(users_count):
        offset += 1000
        all_users.extend(requests.get
                         (
            'https://api.vk.com/method/groups.getMembers',
            params=params
                         ).json()['response']['items'])
    return users



def file_writer(users):
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
file_writer(all)
