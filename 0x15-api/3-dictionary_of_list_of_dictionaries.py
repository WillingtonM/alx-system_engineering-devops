#!/usr/bin/python3
"""Exports to-do list info for particular given employee ID to JSON format."""
import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    api_users = requests.get(api_url + "users").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            usr.get("id"): [{
                "task": tsk.get("title"),
                "completed": tsk.get("completed"),
                "username": usr.get("username")
            } for tsk in requests.get(api_url + "todos",
                                      params={"userId": usr.get("id")}).json()]
            for usr in api_users}, json_file)
