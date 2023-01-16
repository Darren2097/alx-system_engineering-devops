#!/usr/bin/python3
"""script to gather data from an API"""
import requests
import sys


def get_uname(url, user_id):
    """Gets username"""

    response = requests.get(
            "{}users/{}".format(url, user_id))
    usr_dict = response.json()

    return usr_dict['username']


def get_todo_list(url, user_id):
    """Gets todo list"""

    response = requests.get(
            "{}users/{}/todos".format(url, user_id))

    return response.json()


if __name__ == '__main__':
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'

    uname = get_uname(url, user_id)
    todo_list = get_todo_list(url, user_id)

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            writer.writerow([user_id, uname, todo['completed'], todo['title']])
