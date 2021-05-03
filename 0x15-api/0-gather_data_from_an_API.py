#!/usr/bin/python3
'''takes an id for employee and return tasks completed'''
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]
    employee = requests.get(url + 'users/' + id)
    tasks = requests.get(url + 'todos/')

    employee_dict = employee.json()
    tasks_dict = tasks.json()

    total_tasks = 0
    completed_tasks = 0
    name_of_tasks = []
    for task in tasks_dict:
        if task['userId'] == int(id):
            total_tasks += 1
            if task['completed'] is True:
                completed_tasks += 1
                name_of_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_dict['name'], completed_tasks, total_tasks))

    for item in name_of_tasks:
        print("\t{}".format(item['title']))
