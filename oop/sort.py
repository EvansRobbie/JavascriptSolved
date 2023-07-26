# students = ('Evans', 'Robbie', 'Macharia', 'Wachira', "Alice")
# sort() method = used for lists
# sorted function = used for iterables
# students.sort(reverse=True)
# sorted_students = sorted(students, reverse=True)
# for i in sorted_students:
#     print(i)
# students = [
#     ("Robbie", "F", 80),
#     ("SpongeBob", "A", 33),
#     ("Evans", "C", 50),
#     ("Macharia", "D", 20)
# ]
# grade = lambda grade:grade[1]
# students.sort(key=grade)
# for i in students:
#     print(i)

students = (
    ("Robbie", "F", 80),
    ("SpongeBob", "A", 33),
    ("Evans", "C", 50),
    ("Macharia", "D", 20)
)

# students.sort()
# using grade
grade = lambda grade:grade[1]
sorted_students = sorted(students, key=grade)

for i in sorted_students:
    print(i)
