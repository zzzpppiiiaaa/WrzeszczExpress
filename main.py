import random
import time
import pygame
from pygame.locals import *
from train import *

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wrzeszcz Express")
pygame.display.set_icon(screen)
clock = pygame.time.Clock()
font = pygame.font.Font("Bahnschrift.ttf", 18)

#obrazki
kierunek_blokady_left = pygame.image.load('kierunek blokadyv3.png')#rozmiar 45 na 35
kierunek_blokady_right = pygame.image.load('kierunek blokady 2v3.png')

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
            self.x1 = x - scale-7
            self.y1 = y + scale
            self.x2 = x - scale-7
            self.y2 = y - scale

    def draw(self):
        pygame.draw.polygon(screen, (102, 102, 102), ((self.x, self.y), (self.x1, self.y1), (self.x2, self.y2)))
        text = font.render(self.name, True, (255, 214, 0))
        screen.blit(text, ((self.x1), self.y1 - 50))

class Block:
    def __init__(self, left, top, width, height, name):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.name = name
        self.state = "wolny" # / "zajęty"/ "przebieg"
    def draw(self):
        if self.state == "wolny": color = (102, 102, 102)
        elif self.state == "przebieg": color = (0, 200, 130)
        else: color =(237, 0, 0)

        pygame.draw.rect(screen, color, pygame.Rect(self.left, self.top, self.width, self.height))

semR501 = Triangle(277, 103, 15, "R501", left=False)
semR502 = Triangle(277, 173, 15, "R502", left=False)
semR501_2 = Triangle(285, 103, 12, "", left=True)
semR502_2 = Triangle(285, 173, 12, "", left=True)
semH501 = Triangle(450, 103, 15, "H501", left=True)
semH502 = Triangle(450, 173, 15, "H502", left=True)

block55 = Block(10, 100, 60, 6, "block55")
block56 = Block(75, 100, 60, 6, "block56")
block57 = Block(140, 100, 60, 6, "block57")
block58 = Block(10, 170, 60, 6, "block58")
block59 = Block(75, 170, 60, 6, "block59")
block60 = Block(140, 170, 60, 6, "block60")  # Bloki Gdańsk Oliwa SKM
block61 = Block(305, 100, 140, 6, "block61")
block62 = Block(305, 170, 140, 6, "block62")
block63 = Block(470, 100, 140, 6, "block63")
block64 = Block(470, 170, 140, 6, "block64")

poc1111 = Train(1111, "block1")

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
            if event.key == pygame.K_ESCAPE:
                running = False


    semR501.draw()
    semR502.draw()
    semR501_2.draw()
    semR502_2.draw()
    semH501.draw()
    semH502.draw()

    block55.draw()
    block56.draw()
    block57.draw()
    block58.draw()
    block59.draw()
    block60.draw()
    block61.draw()
    block62.draw()
    block63.draw()
    block64.draw()

    screen.blit(kierunek_blokady_left, (205,80))
    screen.blit(kierunek_blokady_right, (205,150))

    poc1111.update()
    #print(poc1111.localisation)

    pygame.display.update()
pygame.quit()
