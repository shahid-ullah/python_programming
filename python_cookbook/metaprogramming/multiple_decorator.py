from functools import wraps


def decorator1(func):
    """Decorator 1"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    """Decorator 2"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

def decorator3(func):
    """Decorator 3"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 3')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
@decorator3
def add(x, y):
    """Add two numbers"""
    return x + y
