# Find the list of of your drinking buddies the age limit is 18 and over
friends = [
    ("Pinky", 18),
    ("Ponky", 18),
    ("Spongebob", 16),
    ("Evans", 17),
    ("Robbie", 21),
    ("Jane", 20),
]
friend_list = lambda data:data[1] >= 18
drinking_buddies = list(filter(friend_list, friends))

for i in drinking_buddies:
    print(i)

