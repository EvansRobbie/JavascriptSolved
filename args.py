# args = parameters that willpack all arguments into a tuple

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(2,3,4))