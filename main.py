import random
import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wrzeszcz Express")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Bahnschrift SemiBold Condensed", 25)


class Triangle:
    def __init__(self, x, y, scale, name, left=True):
        self.name = name
        self.x = x
        self.y = y
        if left:
            self.x1 = x + scale
            self.y1 = y + scale
            self.x2 = x + scale
            self.y2 = y - scale
        else:
            self.x1 = x - scale
            self.y1 = y + scale
            self.x2 = x - scale
            self.y2 = y - scale

    def draw(self):
        pygame.draw.polygon(screen, (102, 102, 102), ((self.x, self.y), (self.x1, self.y1), (self.x2, self.y2)))
        text = font.render(self.name, True, (255, 214, 2))
        screen.blit(text, ((self.x1), self.y1 - 50))


semR501 = Triangle(220, 103, 15, "R501", left=False)
semR502 = Triangle(220, 173, 15, "R502", left=False)

running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("key a pressed")

    pygame.draw.rect(screen, (102, 102, 102), pygame.Rect(10, 100, 60, 6))
    pygame.draw.rect(screen, (102, 102, 102), pygame.Rect(75, 100, 60, 6))
    pygame.draw.rect(screen, (102, 102, 102), pygame.Rect(140, 100, 60, 6))
    pygame.draw.rect(screen, (102, 102, 102), pygame.Rect(10, 170, 60, 6))
    pygame.draw.rect(screen, (102, 102, 102), pygame.Rect(75, 170, 60, 6))
    pygame.draw.rect(screen, (102, 102, 102), pygame.Rect(140, 170, 60, 6)) #Bloki Gdańsk Oliwa SKM

    semR501.draw()
    semR502.draw()
    #
    # text = font.render("text", True, (255, 0, 0))
    # screen.blit(text, (100, 200))

    pygame.display.update()
pygame.quit()
