#!/usr/bin/python3
"""
This script gets information about a user's TODO list progress
and exports data in the CSV format.
"""
import csv
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
    records = []
    for todo in todos:
        records.append([
            userId, username, todo.get("completed"), todo.get("title")
            ])

    with open("{}.csv".format(userId), "w") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(records)
