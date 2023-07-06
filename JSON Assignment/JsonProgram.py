import json

with open('JsonData.json') as f:
    data = json.load(f)

x = json.dumps(data, indent=20)

print("\nDone: Priya Budania\n")

print(x)
print(type(x))

print(data)
print(type(data))

print("Done: Priya Budania")