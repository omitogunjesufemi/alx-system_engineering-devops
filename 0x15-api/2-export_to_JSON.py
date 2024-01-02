#!/usr/bin/python3
"""
Extend task 0 to export data in the JSON format
- Records all tasks that are owned by this employee
- Format must be:
  { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
                 "username": "USERNAME"}, ... ]}
- File name must be: USER_ID.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    usr_id = sys.argv[1]
    usr_url = f"https://jsonplaceholder.typicode.com/users/?id={usr_id}"

    usr_response = requests.get(usr_url)
    usr_json = usr_response.json()
    usr_name = usr_json[0].get("username")

    usr_todos = f"https://jsonplaceholder.typicode.com/todos/?userId={usr_id}"
    usr_todo_response = requests.get(usr_todos)
    usr_todos = usr_todo_response.json()

    task_list = []
    for todo in usr_todos:
        task_dict = {}
        task_dict["task"] = todo.get("title")
        task_dict["completed"] = todo.get("completed")
        task_dict["username"] = usr_name
        task_list.append(task_dict)

    output_dict = {}
    output_dict[str(usr_id)] = task_list

    with open(f"{usr_id}.json", "w", encoding="UTF-8") as json_file:
        json_file.write(json.dumps(output_dict))
