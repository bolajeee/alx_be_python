# Serialization:
import json

# Sample Python object
data = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}

# Serialize the object to a JSON string
json_string = json.dumps(data)

# Optionally, write the JSON string to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

print(json_string)





# Deserialization:
import json
# Deserialize the JSON string back into a Python object
data = json.loads(json_string)
# Or read from a file and deserialize
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)