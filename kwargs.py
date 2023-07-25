# kwargs = parameters that will pack all arguments into a dictionary

def hello(**kwargs):
    print(f"hello {kwargs['first_name']} {kwargs['last_name']} ")
    print('Hello', end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

print(hello(first_name="Evans",  last_name="Macharia"))