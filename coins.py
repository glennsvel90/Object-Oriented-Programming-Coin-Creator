import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

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
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5,
        }
        super().__init__(**data)
