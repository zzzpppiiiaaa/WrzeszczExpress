from block_class import Block
class Train:
    def __init__(self, number, localisation, route=None):
        if route is None: self.route = []
        self.number = number
        self.location = localisation
        self.clock = 0
        self.iswaiting = False

        if self.location == "block1":
            self.route=["block2", "block3", "block4"] # z Gdańska Głównego LK202
            self.direction = "left"
        if self.location == "block51":
            self.route=["block52", "block53", "block54"] # z Gdańska Głównego LK250 (SKM)
            self.direction = "left"
        if self.location == "block5":
            self.route=["block6", "block7"] # Z Sopotu
            self.direction = "right"
        if self.location == "block55":
            self.route=["block56", "block57"] # Z Gdańska Oliwy (SKM)
            self.direction = "right"
        if self.location == "block21":
            self.route=["block22", "block23"] # Z PKM
            self.direction = "right"

    def move(self, block:"Block"):
        if self.location != self.route[-1]:
            self.location = self.route[1]
            self.route.pop(0)
        else:
            self.waiting()

        if self.location in ["Sopot", "Gdansk Oliwa", "Bretowo", "Gdansk Glowny"] and self.clock >= 1200:
            del self
        for i in range(55, 1000):
            temp_name = "block" + str(i)
            if self.location == temp_name and block.name == temp_name: block.state = "zajety"


    def waiting(self):
        self.iswaiting = True

    def update(self):
        if self.iswaiting: print("WAITING")
        self.clock += 1
        if self.location in ["block1", "block2", "block3", "block4", "block51" "block52", "block53", "block54", "block5", "block6", "block7", "block55", "block56", "block57", "block21", "block22", "block23"]:
            if self.clock >= 1200:
                self.clock = 0
                self.move()
        else:
            if self.clock >= 300:
                self.clock = 0
                self.move()