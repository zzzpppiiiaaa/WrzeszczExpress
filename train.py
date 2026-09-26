
class Train:
    def __init__(self, number, localisation, route=None):
        if route is None: self.route = []
        self.number = number
        self.localisation = localisation

        if self.localisation == "block1":
            self.route=["block2", "block3", "block4"] # z Gdańska Głównego LK202
            self.direction = "left"
        if self.localisation == "block51":
            self.route=["block52", "block53", "block54"] # z Gdańska Głównego LK250 (SKM)
            self.direction = "left"
        if self.localisation == "block5":
            self.route=["block6", "block7"] # Z Sopotu
            self.direction = "right"
        if self.localisation == "block55":
            self.route=["block56", "block57"] # Z Gdańska Oliwy (SKM)
            self.direction = "right"
        if self.localisation == "block21":
            self.route=["block22", "block23"] # Z PKM
            self.direction = "right"