import random
 
class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
 
        for key,value in kwargs.items():
            setattr(self,key,value)
 
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads
 
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
 
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour
 
    def rust(self):
        self.colour = self.rusty_colour
 
    def clean(self):
        self.colour = self.clean_colour
 
    def __del__(self):
        print("Coin Spent!")
 
    def flip(self):
        options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice


class One_pence(Coin):
    def __init__(self):
        data = {
        "original_value": 0.01,
        "clean_colour": "bronze",
        "rusty_colour": "brownish",
        "num_edges": 1,
        "diameter": 20.3,
        "thickness": 1.52,
        "mass": 3.56,
        }
        super().__init__(**data)


class Two_pence(Coin):
    def __init__(self):
        data = {
        "original_value": 0.02,
        "clean_colour": "bronze",
        "rusty_colour": "brownish",
        "num_edges": 1,
        "diameter": 25.9,
        "thickness": 1.85,
        "mass": 7.12,
        }
        super().__init__(**data)
        
class Pound(Coin):
    def __init__(self):
        data = {
        "original_value": 1.00,
        "clean_colour": "gold",
        "rusty_colour": "greenish",
        "num_edges": 1,
        "diameter": 22.5,
        "thickness": 3.15,
        "mass": 9.5,
        }
        super().__init__(**data)
