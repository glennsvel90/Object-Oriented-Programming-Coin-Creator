import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True):
        self.rare = rare
        self.clean = clean
        self.heads = heads

        if self.rare:
            self.value
