import random
import time
import pygame
from pygame.locals import *
from train_class import Train
from block_class import Block
from table_class import Table
pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
FPS = 60

speed = 10
spawn_timer = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wrzeszcz Express")
pygame.display.set_icon(screen)
clock = pygame.time.Clock()
font = pygame.font.Font("assets/Bahnschrift.ttf", 18)

#obrazki
kierunek_blokady_left = pygame.image.load('assets/kierunek blokadyv3.png')#rozmiar 45 na 35
kierunek_blokady_right = pygame.image.load('assets/kierunek blokady 2v3.png')
semafor_right = pygame.image.load('assets/semafor.png')
semafor_right = pygame.transform.flip(semafor_right, True, False)
semafor_left = pygame.image.load('assets/semafor.png')

class Triangle:
    def __init__(self, x, y, scale, name, left=True, invisible=False):
        self.invisible = invisible
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
        if not self.invisible:
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
    # nie skm
    Triangle(275, 400, 15, "L", left=False),
    Triangle(275, 473, 15, "M", left=False),
    Triangle(1670, 400, 15, "B", left=True),
    Triangle(1670, 473, 15, "A", left=True),
    Triangle(280, 403, 12, "", left=True),
    Triangle(280, 473, 12, "", left=True),
    Triangle(1665, 400, 12, "", left=False),
    Triangle(1665, 473, 12, "", left=False),
    Triangle(880,415, 5, "K11", left=False, invisible=True),
    Triangle(880, 485, 5, "K12", left=False, invisible=True),
    Triangle(1480, 415, 5, "C1", left=False, invisible=True),
    Triangle(1480, 485, 5, "C2", left=False, invisible=True),
    Triangle(1300, 415, 5, "D1", left=False, invisible=True),
    Triangle(1300, 485, 5, "D2", left=False, invisible=True),
    Triangle(1190, 415, 5, "E11", left=False, invisible=True),
    Triangle(1190, 485, 5, "E12", left=False, invisible=True),

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
    Block(10, 400, 60, 6, "block55"),
    Block(75, 400, 60, 6, "block56"),
    Block(140, 400, 60, 6, "block57"),
    Block(10, 470, 60, 6, "block58"),
    Block(75, 470, 60, 6, "block59"),
    Block(140, 470, 60, 6, "block60"),
    Block(1870, 400, 40, 6, "block65"),
    Block(1870, 470, 40, 6, "block66"),
    Block(1825, 400, 40, 6, "block67"),
    Block(1825, 470, 40, 6, "block68"),
    Block(1780, 400, 40, 6, "block69"),
    Block(1780, 470, 40, 6, "block70"),
    Block(1735, 400, 40, 6, "block71"),
    Block(1735, 470, 40, 6, "block72"),
    Block(300, 400, 550, 6, "block72"),
    Block(300, 470, 550, 6, "block72"),
    Block(300, 470, 550, 6, "block72"),
    Block(1490, 400, 150, 6, "block72"),
    Block(1490, 470, 150, 6, "block72"),
    Block(1305, 400, 150, 6, "block72"),
    Block(1305, 470, 150, 6, "block72"),
    Block(1205, 400, 65, 6, "block72"),
    Block(1205, 470, 65, 6, "block72"),
    Block(885, 400, 285, 6, "block72"),
    Block(885, 470, 285, 6, "block72"),
]

trains = [
    Train(123, "block55", blocks ,"Gdansk Glowny SKM"),
]



TRAIN_CONFIG = {
    "R": {
        "weight": 2,  # Waga prawdopodobieństwa (odpowiednik dwukrotnego powtórzenia na liście)
        "prefixes": ["55", "50", "59", "95", "96", "97"],
        "num_range": (100, 999),
        "routes": {
            "Bretowo": "block65",
            "Gdansk Glowny": "block5",
            "Sopot": "block12",  # Uzupełnij właściwy blok
        },
    },
    "SKM": {
        "weight": 3,
        "prefixes": ["59", "95"],
        "num_range": (100, 999),
        "routes": {
            "Gdansk Glowny SKM": "block11",
            "Gdansk Oliwa": "block14",  # Uzupełnij właściwy blok
        },
    },
    "TLK": {
        "weight": 1,
        "num_range": (10000, 99999),
        "routes": {
            "Gdansk Glowny": "block5",
            "Sopot": "block12",  # Uzupełnij właściwy blok
        },
    },
    "IC": {
        "weight": 1,
        "num_range": (1000, 99999),
        "routes": {
            "Gdansk Glowny": "block5",
            "Sopot": "block12",  # Uzupełnij właściwy blok
        },
    },
    "EIP/EIC": {
        "weight": 1,
        "num_range": (1000, 9999),
        "routes": {
            "Gdansk Glowny": "block5",
            "Sopot": "block12",  # Uzupełnij właściwy blok
        },
    },
    "cargo": {
        "weight": 1,
        "num_range": (100000, 999999),
        "routes": {
            "Gdansk Glowny": "block5",
            "Sopot": "block12",  # Uzupełnij właściwy blok
        },
    },
}


def _generate_train_number(cfg: dict) -> str:
    """Pomocnicza funkcja generująca numer pociągu na podstawie konfiguracji."""
    min_val, max_val = cfg["num_range"]
    number_body = str(random.randint(min_val, max_val))

    if "prefixes" in cfg:
        return random.choice(cfg["prefixes"]) + number_body
    return number_body


def spawn_train(blocks):
    """Generuje i zwraca nową instancję obiektu Train."""
    # 1. Losowanie typu pociągu na podstawie wag z TRAIN_CONFIG
    train_types = list(TRAIN_CONFIG.keys())
    weights = [cfg["weight"] for cfg in TRAIN_CONFIG.values()]
    train_type = random.choices(train_types, weights=weights, k=1)[0]

    cfg = TRAIN_CONFIG[train_type]

    # 2. Generowanie numeru pociągu
    number = _generate_train_number(cfg)

    # 3. Losowanie kierunku wraz z odpowiadającym mu blokiem
    direction, place = random.choice(list(cfg["routes"].items()))

    # 4. Zwrot gotowej instancji pociągu
    # table.add_train(number, place, direction)
    return Train(number, place, blocks, direction)

table = Table()

running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    spawn_timer += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if spawn_timer >= 1200 / speed:
        trains.append(spawn_train(blocks))
        spawn_timer = 0

    screen.blit(kierunek_blokady_left, (205,80))
    screen.blit(kierunek_blokady_right, (205,150))
    screen.blit(kierunek_blokady_left, (1685,80))
    screen.blit(kierunek_blokady_left, (1685,150))
    screen.blit(kierunek_blokady_left, (1685,380))
    screen.blit(kierunek_blokady_right, (1685,450))
    screen.blit(kierunek_blokady_left, (205,380))
    screen.blit(kierunek_blokady_right, (205,450))
    screen.blit(semafor_left, (855,391))
    screen.blit(semafor_left, (855,462))
    screen.blit(semafor_right, (1455,391))
    screen.blit(semafor_right, (1455,462))
    screen.blit(semafor_left, (1275,391))
    screen.blit(semafor_left, (1275,462))
    screen.blit(semafor_right, (1170,391))
    screen.blit(semafor_right, (1170,462))

    table.update_draw(screen)
    for triangle in semaphores:
        triangle.draw()

    for block in blocks:
        block.draw(screen)
        # To debug nazwy odcinków torowych
        # text = font.render(f"{block.name}"[-3:], True, (255, 255, 255))
        # screen.blit(text, ((block.left + 10), block.top - 10))
        if block.state == "zajety":
            for train in trains:
                if train.location == block.name:
                    font.set_bold(True)
                    screen.blit(font.render(" "+ str(train.number)+" ", True, "white", "black"), (block.left + (len(str(train.number))*5)%block.width, block.top-6))
                    font.set_bold(False)


    for train in trains:
        train.update(blocks)


    pygame.display.update()
pygame.quit()
