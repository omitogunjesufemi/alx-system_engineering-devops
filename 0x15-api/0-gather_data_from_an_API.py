#!/usr/bin/python3
"""
A python script that, using a REST API for a given employee ID
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    usr_id = sys.argv[1]
    usr_url = f"https://jsonplaceholder.typicode.com/users/?id={usr_id}"

    usr_response = requests.get(usr_url)
    usr_json = usr_response.json()
    usr_name = usr_json[0].get("name")

    usr_todos = f"https://jsonplaceholder.typicode.com/todos/?userId={usr_id}"
    usr_todo_response = requests.get(usr_todos)
    usr_todos = usr_todo_response.json()
    done_tasks = [todo for todo in usr_todos if todo.get("completed") is True]

    total = len(usr_todos)
    done = len(done_tasks)

    print(f"Employee {usr_name} is done with tasks({done}/{total}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
