# dictionary = a changable, unordered collection uf unique key:value pair
            # fast because hey use hashing, allowing us to acces a value quickly

capitals = {"USA": "Washington DC", 'India': 'New Delhi', 'China': 'Beijing', "Russia": 'moscow'}
# print(capitals['Russia'])
capitals.update({'Germany': 'Berlin'})
capitals.pop('China')
capitals.clear()

print(capitals.get('USA'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)


