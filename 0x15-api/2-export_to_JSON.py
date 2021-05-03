#!/usr/bin/python3
'''takes an id for employee and return tasks completed'''
import json, requests, sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]
    employee = requests.get(url + 'users/' + id)
    tasks = requests.get(url + 'todos/' + '?userId=' + id)

    employee_dict = employee.json()
    tasks_dict = tasks.json()

    name = employee_dict["username"]
    name_of_tasks = []
    new_dict = {id: []}
    for task in tasks_dict:
        new_dict[id].append({"task": task['title'],
                                   "completed": task['completed'],
                                   "username": name})

    filename = id + '.json'
    with open(filename, 'w+') as f:
        json_string = json.dumps(new_dict)
        f.write(json_string)
