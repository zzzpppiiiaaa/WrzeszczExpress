from block_class import Block
class Train:
    def __init__(self, number, localisation, blocks, direction, track_stop, route=None):
        if route is None: self.route = []
        self.number = number
        self.location = localisation
        self.clock = 0
        self.iswaiting = False
        self.direction = direction
        self.track_stop = track_stop

        if self.location == "block11":
            self.route = ["block67", "block69", "block71"]  # z Gdańska Głównego LK202
            self.direction = "left"
        elif self.location == "block65":
            self.route = ["block67", "block69", "block71"]  # z Gdańska Głównego LK250 (SKM)
            self.direction = "left"
        elif self.location == "block5":
            self.route = ["block6", "block7"]  # Z Sopotu
            self.direction = "right"
        elif self.location == "block58":
            self.route = ["block59", "block60"]  # Z Gdańska Oliwy (SKM)
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
            next_block_name = self.route[0]

            # Szukamy obiektu następnego bloku w liście bloków
            next_block = None
            for block in blocks:
                if block.name == next_block_name:
                    next_block = block
                    break

            # Sprawdzamy, czy następny blok istnieje i czy jest wolny
            if next_block and next_block.state == "wolny":
                self.iswaiting = False

                # 1. Zwalniamy obecny blok (zmieniamy na 'wolny')
                self.change_block_state(blocks, self.location, "wolny")

                # 2. Przechodzimy na nowy blok z listy route
                self.location = self.route.pop(0)

                # 3. Zajmujemy nowy blok (zmieniamy na 'zajety')
                self.change_block_state(blocks, self.location, "zajety")
            else:
                # Następny blok jest zajęty – pociąg czeka i nie zmienia pozycji
                self.iswaiting = True
        else:
            # Jeśli trasa się skończyła, pociąg czeka
            self.waiting()

    def waiting(self):
        self.iswaiting = True

    def update(self, blocks):
        # Jeśli pociąg czeka na wolny blok, próbujemy ruszyć w każdym cyklu (update)
        if self.iswaiting and len(self.route) > 0:
            self.move(blocks)
            if not self.iswaiting:
                self.clock = 0  # Resetujemy zegar, gdy pociąg pomyślnie ruszył
            return

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