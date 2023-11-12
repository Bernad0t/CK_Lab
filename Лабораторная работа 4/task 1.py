# TODO решите задачу
import json


def task() -> float:
    with open("input.json", "r") as file:
        data = json.load(file)
    res = 0
    for i in data:
        res += i["score"] * i["weight"]
    return round(res, 3)


print(task())
