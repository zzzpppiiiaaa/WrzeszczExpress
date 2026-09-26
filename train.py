
class Train:
    def __init__(self, number, localisation, route=None):
        if route is None: self.route = []
        self.number = number
        self.localisation = localisation
        self.clock = 0
        self.iswaiting = False

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

    def move(self):
        if self.localisation != self.route[-1]:
            self.localisation = self.route[1]
            self.route.pop(0)
        else:
            self.waiting()

    def waiting(self):
        self.iswaiting = True

    def update(self):
        if self.iswaiting: print("WAITING")
        self.clock += 1
        if self.localisation in ["block1", "block2", "block3", "block4", "block51" "block52", "block53", "block54", "block5", "block6", "block7", "block55", "block56", "block57","block21", "block22", "block23"]:
            if self.clock >= 120:
                self.clock = 0
                self.move()