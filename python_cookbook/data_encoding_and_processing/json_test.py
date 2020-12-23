import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    breakpoint()
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d
