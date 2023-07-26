# dictionary comprehensions = create a dictionary using an expression
# can replace for loops and certain lamda functions

# dictionary = {key: expression for (key, value) in iterable}

# cities = {"New York":32, "Boston": 75, "Los Angelas": 100, "Chicago": 50}

# cities_in_C = {key: round((value-32) * (5/9)) for (key, value) in cities.items()}

# print(cities_in_C)

# list places which are sunny
# dictionary = {key: () expression for (key, value) in iterable if condition}
weather = {"New York":"Snowing", "Boston": "Sunny", "Los Angelas": "Sunny", "Chicago": "Cloudy"}

sunny_cities = {key: value for (key, value) in weather.items() if value == "Sunny"}

print(sunny_cities)

# dictionary = {key: () (if/else) expression for (key, value) in iterable}

weather = {"New York":"Snowing", "Boston": "Sunny", "Los Angelas": "Sunny", "Chicago": "Cloudy"}

sunny_cities = {key: "warm" if value =="Sunny" else "Cold" for (key, value) in weather.items() }

print(sunny_cities)

# for complex scenarios
# dictionary = {key: function(value) expression for (key, value) in iterable}