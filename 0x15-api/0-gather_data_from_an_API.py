#!/usr/bin/python3
"""Returns the to-do list info for a particular given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    api_user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    task_comp = [ct.get("title") for ct in todo if ct.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        api_user.get("name"), len(task_comp), len(todo)))
    [print("\t {}".format(tc)) for tc in task_comp]
