#!/usr/bin/python3
"""Exports to-do list information for a particular given employee ID to CSV format."""
import sys
import csv
import requests

if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    api_user = requests.get(api_url + "users/{}".format(user_id)).json()
    username = api_user.get("username")
    todo = requests.get(api_url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvf_ile:
        writer = csv.writer(csvf_ile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, task.get("completed"), task.get("title")]
         ) for task in todo]

