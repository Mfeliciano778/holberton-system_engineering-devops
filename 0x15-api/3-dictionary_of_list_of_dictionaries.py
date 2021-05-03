#!/usr/bin/python3
'''takes an id for employee and return tasks completed'''
import json, requests, sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + 'users/')

    employee_dict = employee.json()
    new_dict = {}
    for user in employee_dict:
        id = str(user['id'])
        new_dict[id] = []
        task_names = []
        name = user["username"]
        tasks = requests.get(url + 'todos/' + '?userId=' + id)
        task_dict = tasks.json()
        for task in task_dict:
            new_dict[id].append({"task": task['title'],
                                 "completed": task['completed'],
                                 "username": name})

    filename = 'todo_all_employees.json'
    with open(filename, 'w+') as f:
        json_string = json.dumps(new_dict)
        f.write(json_string)
