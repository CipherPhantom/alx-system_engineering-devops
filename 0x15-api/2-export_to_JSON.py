#!/usr/bin/python3
"""
This script gets information about a user's TODO list progress
and exports data in the JSON format.
"""
import json
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

    username = userInfo.get("username")
    record = {
            str(userId): []
            }
    for todo in todos:
        record[str(userId)].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
            })

    with open("{}.json".format(userId), "w") as jsonfile:
        json.dump(record, jsonfile)
