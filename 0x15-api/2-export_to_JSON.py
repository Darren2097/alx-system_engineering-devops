#!/usr/bin/python3
# script to gather todo data from an API and write to JSON file
import json
import requests
import sys


def get_username(url, user_id):
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
    url = 'https://jsonplaceholder.typicode.com/'

    uname = get_username(url, user_id)
    todo_list = get_todo_list(url, user_id)

    with open('{}.json'.format(user_id), 'w') as f:
        todo_dict = {}
        todo_dict[sys.argv[1]] = []
        for todo in todo_list:
            task = {}
            task['task'] = todo['title']
            task['completed'] = todo['completed']
            task['username'] = uname
            todo_dict[sys.argv[1]].append(task)

        f.write(json.dumps(todo_dict))
