import sys
import json

input = sys.argv[1]
path = json.loads(sys.argv[2])

with open(input) as data:
    value = json.load(data)

for part in path:
    value = value[part]

print(value)