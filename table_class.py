import pygame

class Table:
    def __init__(self):
        self.x = 1200
        self.y = 700
        self.trains = []

    def update_draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 170), pygame.Rect(self.x, self.y, 920, self.x))
        for train in self.trains:
            ...


    def add_del_train(self, number,location, direction):
        id = 0
        id_lists = []
        for train in self.trains:
            for id in train[5]:
                id_lists.append(id)

        id = max(id_lists) + 1

        origin = ""
        line = 202
        if location == "block55":
            origin = "Gdańsk Oliwa SKM"
            line = 250

        self.trains.append([number, location, direction, origin, line, id])