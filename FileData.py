import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "coding"]
}

file_name = "data.json"
with open(file_name, "w") as file:
    json.dump(data, file, indent=4)
with open(file_name, "r") as file:
    content = json.load(file)
    print(json.dumps(content, indent=4))
