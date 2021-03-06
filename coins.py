import random
import humanize



class Coin:
    """Class to represent a Coin.

    Attributes:
        original_value (int): The value of the coin
        clean_color (str): The color of the coin when it is clean(not rusted)
        rusty_color (str): The color of the coin when it has been rusted
        num_edges (int): The number of edges the coin has
        diameter (int): The diameter in millimeters of the coin
        thickness (int): The thickness in millimeters of the coin
        mass (int): The mass in grams of the coin
        heads (boolean): Whether the coin is face up heads or not
        is_rare (boolean): Whether the coin is rare or not
        is_clean (boolean): Whether the coin is clean. If the coin is not clean, it is rusted

    Methods:
        rust: Used to rust a coin. This method is not available for silver coins, since silver coins do not rust
        clean: Used to clean a coin and not make it be rusted anymore
        flip: Used to flip a coin and change it's face up heads state
    """

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
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        """ This wil rust the coin """
        self.color = self.rusty_color

    def clean(self):
        """ This will clean the coin """
        self.color = self.clean_color

    def flip(self):
        """ This will change the head state of the coin to either heads or tails """
        options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            ap = str(humanize.apnumber(int(self.original_value)))
            cap = ap.capitalize()

            return "{} Pound Coin".format(cap)
        else:
            ap = humanize.apnumber(int(self.original_value*100))
            cap = ap.capitalize()
            return "{} Pence Coin".format(cap)


class One_Pence(Coin):
    """ Class to represent a one pence coin """
    def __init__(self):
        data = {
        "original_value": 0.01,
        "clean_color": "bronze",
        "rusty_color": "brownish",
        "num_edges": 1,
        "diameter": 20.3,
        "thickness": 1.52,
        "mass": 3.56,
        }
        super().__init__(**data)


class Two_Pence(Coin):
    """ Class to represent a two pence coin """
    def __init__(self):
        data = {
        "original_value": 0.02,
        "clean_color": "bronze",
        "rusty_color": "brownish",
        "num_edges": 1,
        "diameter": 25.9,
        "thickness": 1.85,
        "mass": 7.12,
        }
        super().__init__(**data)


class Five_Pence(Coin):
    """ Class to represent a five pence coin """
    def __init__(self):
        data = {
        "original_value": 0.05,
        "clean_color": "silver",
        "rusty_color": None,
        "num_edges": 1,
        "diameter": 18.0,
        "thickness": 1.77,
        "mass": 3.25,
        }
        super().__init__(**data)

    def rust():
        self.color = self.clean_color


class Ten_Pence(Coin):
    """ Class to represent a ten pence coin """
    def __init__(self):
        data = {
        "original_value": 0.10,
        "clean_color": "silver",
        "rusty_color": None,
        "num_edges": 1,
        "diameter": 24.5,
        "thickness": 1.85,
        "mass": 6.50,
        }
        super().__init__(**data)

    def rust():
        self.color = self.clean_color


class Twenty_Pence(Coin):
    """ Class to represent a twenty pence coin """
    def __init__(self):
        data = {
        "original_value": 0.20,
        "clean_color": "silver",
        "rusty_color": None,
        "num_edges": 7,
        "diameter": 21.4,
        "thickness": 1.7,
        "mass": 5.00,
        }
        super().__init__(**data)

    def rust():
        self.color = self.clean_color


class Fifty_Pence(Coin):
    """ Class to represent a fifty pence coin """
    def __init__(self):
        data = {
        "original_value": 0.50,
        "clean_color": "silver",
        "rusty_color": None,
        "num_edges": 7,
        "diameter": 27.3,
        "thickness": 1.78,
        "mass": 8.00,
        }
        super().__init__(**data)

    def rust():
        self.color = self.clean_color


class One_Pound(Coin):
    """ Class to represent a one pound coin """
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


class Two_Pound(Coin):
    """ Class to represent a two pound coin """
    def __init__(self):
        data = {
        "original_value": 2.00,
        "clean_color": "gold & silver",
        "rusty_color": "greenish",
        "num_edges": 1,
        "diameter": 28.4,
        "thickness": 2.50,
        "mass": 12.00,
        }
        super().__init__(**data)


coins = [One_Pence(), Two_Pence(), Five_Pence(), Ten_Pence(), Twenty_Pence(),
         Fifty_Pence(), One_Pound(), Two_Pound()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]

    string = """Created a {} - color: {}, Value: £{}, Diameter(mm): {}, Thickness(mm): {}, Number of Edges: {}, Mass(g): {}
    """.format(*arguments)

    print(string)

print("""
Explore the docstring for the Coin class to understand it's features.
To do so type: help(Coin)
You may create an instance of a £1 coin and then flip the coin with the flip() function to change it's head up state.
To create an instance of a £1 coin, type into the terminal while in python interactive mode: one_pound_coin = One_Pound()
Then flip the coin by typing: one_pound_coin.flip()
You may rust the coin by typing: one_pound_coin.rust()
You many clean the coin by typing: one_pound_coin.clean())

To see what other coin classes are available, type in the terminal while in python interactive mode: help(coins)
""")
