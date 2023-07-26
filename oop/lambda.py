double = lambda x:x*2
multiply = lambda x, y: x*y

full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age:True if age >= 18 else False
print(age_check(14))
print(full_name("Evans", "Robbie"))
print(multiply(5, 2))