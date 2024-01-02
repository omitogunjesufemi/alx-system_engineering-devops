#!/usr/bin/python3
"""
Extend task 0 to export data into JSON format
- Records all tasks from all employees
- Format must be:
  { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
               "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
               "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]
   "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
              "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
              "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
- File name must be: todo_all_employees.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    usr_url = f"https://jsonplaceholder.typicode.com/users"
    usr_response = requests.get(usr_url)
    users = usr_response.json()

    output_dict = {}
    for user in users:
        usr_id = user.get("id")
        url = f"https://jsonplaceholder.typicode.com/todos/?userId={usr_id}"
        todo_response = requests.get(url)
        todos = todo_response.json()
        task_list = []
        for todo in todos:
            task_dict = {}
            task_dict["task"] = todo.get("title")
            task_dict["completed"] = todo.get("completed")
            task_dict["username"] = user.get("username")
            task_list.append(task_dict)

        output_dict[str(user.get("id"))] = task_list

    with open("todo_all_employees.json", "w", encoding="UTF-8") as json_file:
        json_file.write(json.dumps(output_dict))
