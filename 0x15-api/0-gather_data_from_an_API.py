#!/usr/bin/python3
"""script to gather data from an API"""
import requests
import sys


def get_uname(url, user_id):
    """Gets username"""

    response = requests.get(
            "{}users/{}".format(url, user_id))
    usr_dict = response.json()
    return usr_dict['name']


def get_todo_list(url, user_id):
    """Gets todo list"""

    response = requests.get(
            "{}users/{}/todos".format(url, user_id))
    return response.json()


def get_completed(todo_list):
    """Gets completed items"""

    done_str = ""
    done_list = []
    count = 0

    for todo in todo_list:
        if todo['completed'] is True:
            count += 1
            done_list.append("\t {}".format(todo['title']))
    done_str = "\n".join(done_list)

    return count, done_str


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    uname = get_uname(url, user_id)
    todo_list = get_todo_list(url, user_id)
    total = len(todo_list)

    count, done_str = get_completed(todo_list)

    print("Employee {} is done with tasks({}/{}):".format(
        uname, count, total))
    if count > 0:
        print(done_str)
