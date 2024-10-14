import json

with open("sample.txt") as file:
    result = json.load(file)
    print(result["message"])
    # print(result.values())