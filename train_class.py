from block_class import Block
class Train:
    def __init__(self, number, localisation, blocks, direction, track_stop, route=None):
        self.route = [] if route is None else list(route)  # bloki, które pociąg ma jeszcze przed sobą
        self.number = number
        self.location = localisation
        self.clock = 0
        self.iswaiting = False
        self.destination = direction  # nazwa kierunku (np. "Gdansk Oliwa") - do tabeli
        self.direction = direction    # niżej nadpisywane na "left" / "right"
        self.track_stop = track_stop

        self.current_route = None   # przebieg dyżurnego, którym pociąg aktualnie jedzie
        self.leaving = False        # True, gdy pociąg jedzie już szlakiem za stacją
        self.finished = False       # True, gdy dojechał do końca szlaku (main.py go wtedy usuwa)

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

        self.change_block_state(blocks, self.location, "zajety")

    # Funkcja pomocnicza do szukania bloku po nazwie i zmiany jego stanu
    def change_block_state(self, blocks, nazwa_bloku, nowy_stan):
        for block in blocks:
            if block.name == nazwa_bloku:
                block.state = nowy_stan
                break

    def take_route(self, active_routes):
        """Pociąg stoi przed semaforem. Jeśli dyżurny ustawił dla niego przebieg, pociąg go przejmuje."""
        for r in active_routes.values():
            if r["train"] is None and r["from_block"] == self.location and r["direction"] == self.direction:
                r["train"] = self                       # przebieg należy teraz do tego pociągu
                self.current_route = r
                exit_blocks = r.get("exit_blocks", [])  # szlak za stacją (tylko przebiegi wyjazdowe)
                self.route = list(r["blocks_block"]) + list(exit_blocks)
                self.leaving = bool(exit_blocks)
                return

    def move(self, blocks, active_routes):
        # Skończyła się lista bloków: pociąg stoi przed semaforem i szuka ustawionego przebiegu
        if not self.route and not self.leaving:
            self.take_route(active_routes)

        if not self.route:
            if self.leaving:
                # Koniec szlaku za stacją: pociąg znika z planszy
                self.change_block_state(blocks, self.location, "wolny")
                self.iswaiting = False
                self.finished = True
            else:
                # Brak przebiegu: pociąg czeka przed semaforem
                self.waiting()
            return

        next_block_name = self.route[0]

        # Szukamy obiektu następnego bloku w liście bloków
        next_block = None
        for block in blocks:
            if block.name == next_block_name:
                next_block = block
                break

        # Sprawdzamy, czy następny blok istnieje i czy jest wolny (albo zarezerwowany przebiegiem)
        if next_block and next_block.state in ("wolny", "przebieg"):
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

    def waiting(self):
        self.iswaiting = True

    def update(self, blocks, active_routes):
        if self.finished: return

        if self.iswaiting:
            self.move(blocks, active_routes)
            if not self.iswaiting: self.clock = 0
            return

        self.clock += 1
        szlakowe_bloki = ["block1", "block2", "block3", "block4", "block51", "block52", "block53", "block54", "block5",
                          "block6", "block7", "block55", "block56", "block57", "block21", "block22", "block23"]

        if self.location in szlakowe_bloki:
            if self.clock >= 120:
                self.clock = 0
                self.move(blocks, active_routes)
        else:
            if self.clock >= 300:
                self.clock = 0
                self.move(blocks, active_routes)