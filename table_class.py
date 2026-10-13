import pygame
pygame.init()
font = pygame.font.Font("assets/Bahnschrift.ttf", 18)
title_font = pygame.font.SysFont("Calibri", 24)

class Table:
    def __init__(self):
        self.x = 1200
        self.y = 700
        self.trains = []

    def update_draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 170), pygame.Rect(self.x, self.y, 920, self.x))
        text = title_font.render("  NR                    ZE STACJI                              NR LINI                   DO STACJI", True, "black")
        screen.blit(text, (self.x, self.y+10))
        for train in self.trains:
            text_number = font.render(str(train[0]), True, "black")
            text_direction = font.render(train[2], True, "black")
            text_origin = font.render(train[3], True, "black")
            text_line_number = font.render(str(train[4]), True, "black")
            screen.blit(text_number, (self.x+10, self.y + (train[5] * 25 + 40))) # numer
            screen.blit(text_direction, (self.x+10 + 500, self.y + (train[5] * 25+ 40))) # kierunek
            screen.blit(text_line_number, (self.x+10 + 400, self.y + (train[5] * 25 +40))) # numer linii
            screen.blit(text_origin, (self.x+ 10 + 100, self.y + (train[5] * 25 + 40))) # z kąd


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
        if location == "block65":
            origin = "Gdansk Glowny SKM"
            line = 250

        self.trains.append([number, location, direction, origin, line, id])