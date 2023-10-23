#!/usr/bin/python3
"""
This script gets information about a user's TODO list progress
and exports data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    res = requests.get("{}/{}/".format(url, "users"))
    users = res.json()

    records = {}
    for user in users:
        userId = user.get("id")
        params = {
                "userId": userId,
                }
        res = requests.get("{}/{}/".format(url, "todos"), params=params)
        todos = res.json()

        userId = str(userId)
        username = user.get("username")

        records[userId] = []
        for todo in todos:
            records[userId].append({
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
                })

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(records, jsonfile)
