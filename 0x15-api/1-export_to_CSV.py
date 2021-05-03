#!/usr/bin/python3
'''takes an id for employee and return tasks completed'''
import requests
import sys
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]
    employee = requests.get(url + 'users/' + id)
    tasks = requests.get(url + 'todos/')

    employee_dict = employee.json()
    tasks_dict = tasks.json()

    name = employee_dict['username']
    filename = id + '.csv'

    with open(filename, 'w+', newline="") as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks_dict:
            if task['userId'] == int(id):
                write.writerow([id, name, task['completed'], task['title']])
