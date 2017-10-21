import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True):
        self.rare = rare
        #check if error is present for self.clean instead of self.is_clean
        self.clean = clean
        #Check if error comes if self.heads is present
        self.heads = heads

        if self.rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

#check if error for is clean
        if self.clean:
            self.color = clean_color
        else:
            self.color = rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

class Pound(Coin):
    def __init__(self):
        data = {''}
