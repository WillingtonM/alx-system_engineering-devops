#!/usr/bin/python3
"""Exports to-do list information for a particular given employee ID to JSON format."""
import sys
import json
import requests

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    api_user = requests.get(url + "users/{}".format(user_id)).json()
    username = api_user.get("username")
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump({user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todo]}, json_file)
