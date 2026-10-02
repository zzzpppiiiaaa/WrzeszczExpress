import pygame



class Block:
    def __init__(self, left, top, width, height, name):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.name = name
        self.state = "wolny" # / "zajety"/ "przebieg"
    def draw(self, screen):
        if self.state == "wolny": color = (102, 102, 102)
        elif self.state == "przebieg": color = (0, 200, 130)
        else: color =(237, 0, 0)
        pygame.draw.rect(screen, color, pygame.Rect(self.left, self.top, self.width, self.height))