# list comprehension is a way to create a new list with less syntax 
# can mimic certsi la,bada functions 
# list = [expression for item in iterables ]

# squares = []

# for i in range (1,11):
#     squares.append(i**2)
# print (squares)

# list = [expression for item in iterables ]
# squares = [i**2 for i in range(1,11)]
# print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20]

filter_list = list(filter(lambda data:data >= 60, students))
for i in filter_list:
    print(i)

# using list comprehension
# list = [expression for item in iterables if condition ]
passed_students = [i for i in students if i >=60]
print(passed_students)

# if you need an else statement
# list = [expression (if/else) for item in iterables ]
passed_students = [i if i >=60 else "Failed" for i in students ]
print(passed_students)