user = ['Evans', "Robbie", "Macharia"]
password = ['Password@123', "Evans@12", "Macharia@12"]

# zip
users = zip(user, password)
# list
users = list(zip(user, password))

for i in users:
    print(i)

# dict
users = dict(zip(user, password))

for key, value in users.items():
    print(key + ' : ' + value)