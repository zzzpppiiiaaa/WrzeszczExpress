import pygame
pygame.init()
font = pygame.font.Font("assets/Bahnschrift.ttf", 18)

class Table:
    def __init__(self):
        self.x = 1200
        self.y = 700
        self.trains = []

    def update_draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 170), pygame.Rect(self.x, self.y, 920, self.x))
        for train in self.trains:
            text_number = font.render(train[0], True, "black")
            screen.blit(text_number, (self.x, self.y + (train[5] * 20)))


    def add_train(self, number,location, direction):
        id = 0
        id_list = [0]
        for train in self.trains:
                id_list.append(train[5])
        id = max(id_list) + 1

        origin = ""
        line = 202
        if location == "block55":
            origin = "Gdańsk Oliwa SKM"
            line = 250

        self.trains.append([number, location, direction, origin, line, id])