#!/usr/bin/python3
"""
This script returns information about a user's TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    userId = int(sys.argv[1])
    res = requests.get("{}/{}/{}".format(url, "users", userId))
    userInfo = res.json()

    params = {
            "userId": userId,
            }
    res = requests.get("{}/{}/".format(url, "todos"), params=params)
    todos = res.json()

    completed_todos = [
            todo.get("title") for todo in todos if todo.get("completed")
            ]

    print("Employee {} is done with tasks({}/{}):".format(
        userInfo.get("name"),
        len(completed_todos),
        len(todos)
        ))
    for title in completed_todos:
        print("\t {}".format(title))
