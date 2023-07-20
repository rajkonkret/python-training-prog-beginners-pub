import json

with open("people.json") as file:
    content = json.load(file)  # load wczytuje z zargumentu za pomocą metody read (w domyśle z pliku) i
                               # konwertuje na json
    print(content)

for person in content:
    print(person["name"])

string = "{\"name\":\"John\"}"
print(string)
print(json.loads(string))  # loads konwertuje json na struktury danych pythonowe
print(type(json.loads(string)))

print(json.dumps({"key": 5}))  # konwertuje na string w formacie json

