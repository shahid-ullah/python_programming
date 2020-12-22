class Chair:
    """Another Chair"""
    max_occupants = 4

    def __init__(self, id):
        breakpoint()
        self.id = id
        self.count = 0

    def load(self, number):
        self.count += number

    def unload(self, number):
        self.count -= number
