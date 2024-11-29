import json

data = {
    "student": "John Doe",
    "age": 15,
    "city": "Delhi",
    "hobbies": ["reading", "traveling", "coding"]
}

file_name = "data.json"
file_name1 = "data1.json"

with open(file_name, "w") as file:
    json.dump(data, file, indent=4)

with open(file_name, "r") as file1, open(file_name1, "w") as file2:
    content = file1.read()
    print(content, file=file2)

with open(file_name1, "r") as file3:
    content1 = json.load(file3)
    print(json.dumps(content1, indent=4))
