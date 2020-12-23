# test.py

def decorator(func):
    func()
    return 10


# @decorator
def print_hello_world():
    print("Hello World")

print_hello_world = decorator(print_hello_world)
