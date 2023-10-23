#!/usr/bin/python3
"""Returns the to-do list information for a particular given employee ID."""

import sys
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    api_user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(api_url + "todos", params={"userId": sys.argv[1]}).json()

    task_comp = [ct.get("title") for ct in todo if ct.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        api_user.get("name"), len(task_comp), len(todo)))
    [print("\t {}".format(tc)) for tc in task_comp]
