import pygame
pygame.init()

class Rozjazd:
    rozjazd_right = pygame.image.load('assets/rozjazd w prawo.png')
    rozjazd_left = pygame.transform.flip(pygame.image.load('assets/rozjazd w prawo.png'), True, False)

    def __init__(self, x, y, width=1, height=1, right=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.right = right
        if self.right:
            self.img = Rozjazd.rozjazd_right
        else:
            self.img = Rozjazd.rozjazd_left
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def draw(self, screen):
         screen.blit(self.img, (self.x, self.y))


