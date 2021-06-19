import json

data = {}
data["people"] = []
data["people"] = [
    {"studentid": 1, "name": "ABC", "subjects": ["Python", "Data Structures"]},
    {"studentid": 2, "name": "PQR", "subjects": ["Java", "Operating System"]},
]

# Write pretty print JSON data to file
with open("filename.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

"""import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
"""
with open("filename.json") as json_file:
    data = json.load(json_file)
    for p in data["people"]:
        print(f'studentid: {p["studentid"]}')
        print(f"name: {p['name']}")
        print(f"subjects: {p['subjects']}")
        print("")
