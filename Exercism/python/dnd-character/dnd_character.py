from math import ceil
class Character:
    def __init__(self):
        self.name = None

class modifier:
    def __init__(self, constitution):
        return ceil((10 - constitution)//2)

