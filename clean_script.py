import codecs
import json

file = codecs.open("riri_sandra.json", "r", "utf-8")
old_data = file.read()
messages = json.loads(old_data)["messages"]

new_data = []
for message in messages:
    if message['author']["name"] == 'umbrellabird':
        new_data.append({'message': message['content']})

json_y = json.dumps(new_data)
print(json_y)

with open("riri_cleaned_sandra.json", "w") as file:
    file.write(json_y)
