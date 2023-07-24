# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break
phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")