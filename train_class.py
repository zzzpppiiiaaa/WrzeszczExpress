from block_class import Block
class Train:
    # Dodajemy argument 'blocks', aby pociąg mógł od razu zająć swój blok startowy
    def __init__(self, number, localisation, blocks, direction, route=None):
        if route is None: self.route = []
        self.number = number
        self.location = localisation
        self.clock = 0
        self.iswaiting = False
        self.direction = direction

        if self.location == "block11":
            self.route = ["block67", "block69", "block71"]  # z Gdańska Głównego LK202
            self.direction = "left"
        elif self.location == "block65":
            self.route = ["block67", "block53", "block54"]  # z Gdańska Głównego LK250 (SKM)
            self.direction = "left"
        elif self.location == "block5":
            self.route = ["block6", "block7"]  # Z Sopotu
            self.direction = "right"
        elif self.location == "block55":
            self.route = ["block56", "block57"]  # Z Gdańska Oliwy (SKM)
            self.direction = "right"
        elif self.location == "block21":
            self.route = ["block22", "block23"]  # Z PKM
            self.direction = "right"

        # Ustawiamy początkowy blok jako zajęty od razu przy pojawieniu się pociągu
        self.change_block_state(blocks, self.location, "zajety")

    # Funkcja pomocnicza do szukania bloku po nazwie i zmiany jego stanu
    def change_block_state(self, blocks, nazwa_bloku, nowy_stan):
        for block in blocks:
            if block.name == nazwa_bloku:
                block.state = nowy_stan
                break

    def move(self, blocks):
        if len(self.route) > 0:
            # 1. Zwalniamy obecny blok (zmieniamy na 'wolny')
            self.change_block_state(blocks, self.location, "wolny")

            # 2. Przechodzimy na nowy blok z listy route
            self.location = self.route.pop(0)

            # 3. Zajmujemy nowy blok (zmieniamy na 'zajety')
            self.change_block_state(blocks, self.location, "zajety")
        else:
            # Jeśli trasa się skończyła, pociąg czeka
            self.waiting()

    def waiting(self):
        self.iswaiting = True

    # Do update przekazujemy 'blocks', żeby móc je podać dalej do 'move'
    def update(self, blocks):
        if self.iswaiting: print("Waiting")
        self.clock += 1
        szlakowe_bloki = ["block1", "block2", "block3", "block4", "block51", "block52", "block53", "block54", "block5",
                         "block6", "block7", "block55", "block56", "block57", "block21", "block22", "block23"]

        if self.location in szlakowe_bloki:
            if self.clock >= 120:
                self.clock = 0
                self.move(blocks)
        else:
            if self.clock >= 300:
                self.clock = 0
                self.move(blocks)