#!/usr/bin/python3
"""
Extends task 0 to export data in the CSV format
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""
import csv
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

    with open(f"{usr_id}.csv", "w", newline="") as csv_f:
        json_to_csv = csv.writer(csv_f, delimiter=",", quoting=csv.QUOTE_ALL)
        for todo in usr_todos:
            json_to_csv.writerow([usr_id, usr_name,
                                  todo.get("completed"), todo.get("title")])
