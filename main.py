import random
import time
import pygame
from pygame.locals import *
from train_class import Train
from block_class import Block

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
        screen.blit(text, ((self.x1-10), self.y1 - 50))
semaphores = [
    #skm
    Triangle(277, 103, 15, "R501", left=False),
    Triangle(277, 173, 15, "R502", left=False),
    Triangle(285, 103, 12, "", left=True),
    Triangle(285, 173, 12, "", left=True),
    Triangle(450, 103, 15, "H501", left=True),
    Triangle(450, 173, 15, "H502", left=True),
    Triangle(1665, 103, 15, "B501", left=True),
    Triangle(1665, 173, 15, "B502", left=True),
    Triangle(1660, 103, 12, "", left=False),
    Triangle(1660, 173, 12, "", left=False),
    Triangle(1430, 103, 15, "B501", left=False),
    Triangle(1430, 173, 15, "B502", left=False),
    Triangle(1080, 103, 15, "G501", left=True),
    Triangle(1080, 173, 15, "G502", left=True),
    Triangle(875, 103, 15, "J502", left=False),
    Triangle(875, 173, 15, "J502", left=False),
    #nie skm
]

blocks = [
    #skm
    Block(10, 100, 60, 6, "block55"),
    Block(75, 100, 60, 6, "block56"),
    Block(140, 100, 60, 6, "block57"),
    Block(10, 170, 60, 6, "block58"),
    Block(75, 170, 60, 6, "block59"),
    Block(140, 170, 60, 6, "block60"),  # Bloki Gdańsk Oliwa SKM
    Block(305, 100, 140, 6, "block161"),
    Block(305, 170, 140, 6, "block162"),
    Block(470, 100, 380, 6, "block163"),
    Block(470, 170, 380, 6, "block164"),
    Block(1870, 100, 40, 6, "block65"),
    Block(1870, 170, 40, 6, "block66"),
    Block(1825, 100, 40, 6, "block67"),
    Block(1825, 170, 40, 6, "block68"),
    Block(1780, 100, 40, 6, "block69"),
    Block(1780, 170, 40, 6, "block70"),
    Block(1735, 100, 40, 6, "block71"),
    Block(1735, 170, 40, 6, "block72"),
    Block(1435, 100, 200, 6, "block173"),
    Block(1435, 170, 200, 6, "block174"),
    Block(1100, 100, 300, 6, "block177"),
    Block(1100, 170, 300, 6, "block178"),
    Block(885, 100, 190, 6, "block179"),
    Block(885, 170, 190, 6, "block180"),
    #nie skm
    Block(10, 300, 60, 6, "block55"),
    Block(75, 300, 60, 6, "block56"),
    Block(140, 300, 60, 6, "block57"),
    Block(10, 370, 60, 6, "block58"),
    Block(75, 370, 60, 6, "block59"),
    Block(140, 370, 60, 6, "block60"),
    Block(1870, 300, 40, 6, "block65"),
    Block(1870, 370, 40, 6, "block66"),
    Block(1825, 300, 40, 6, "block67"),
    Block(1825, 370, 40, 6, "block68"),
    Block(1780, 300, 40, 6, "block69"),
    Block(1780, 370, 40, 6, "block70"),
    Block(1735, 300, 40, 6, "block71"),
    Block(1735, 370, 40, 6, "block72"),
]

trains = [
    Train(1111, "block65", blocks),
]

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

    screen.blit(kierunek_blokady_left, (205,80))
    screen.blit(kierunek_blokady_right, (205,150))
    screen.blit(kierunek_blokady_left, (1685,80))
    screen.blit(kierunek_blokady_right, (1685,150))

    for triangle in semaphores:
        triangle.draw()

    for block in blocks:
        block.draw(screen)
        # To debug nazwy odcinków torowych
        # text = font.render(f"{block.name}"[-3:], True, (255, 255, 255))
        # screen.blit(text, ((block.left + 10), block.top - 10))

    for train in trains:
        train.update(blocks)


    pygame.display.update()
pygame.quit()
