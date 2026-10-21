import pygame
pygame.init()
class Triangle:
    def __init__(self, x, y, scale, name, left=True, invisible=False, exit = False):
        self.color = (102, 102, 102)
        self.exit = exit
        self.invisible = invisible
        self.name = name
        self.x = x
        self.y = y
        self.state = "default"
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
        if self.state == "default" : self.color = (102, 102, 102) #gray
        if self.state == "allow" : self.color = (0, 200, 130) #green
        if self.state == "deny": self.color = (237, 0, 0) #red

        if not self.invisible:
            pygame.draw.polygon(screen, self.color, ((self.x, self.y), (self.x1, self.y1), (self.x2, self.y2)))
        if not self.exit:
            text = font.render(self.name, True, (255, 214, 0))
            screen.blit(text, ((self.x1-10), self.y1 - 50))


    def is_clicked(self, mx, my):
        min_x = min(self.x, self.x1, self.x2)
        max_x = max(self.x, self.x1, self.x2)
        min_y = min(self.y, self.y1, self.y2)
        max_y = max(self.y, self.y1, self.y2)

        return min_x <= mx <= max_x and min_y <= my <= max_y
