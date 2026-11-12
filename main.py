import random
import pygame
from pygame.locals import *
from train_class import Train
from block_class import Block
from table_class import Table
from triangle_class import Triangle
from rozjady_class import Rozjazd
pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
FPS = 60

speed = 1
spawn_timer = 1000
toleration = 100
train_counter = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wrzeszcz Express")
pygame.display.set_icon(screen)
clock = pygame.time.Clock()
font = pygame.font.Font("assets/Bahnschrift.ttf", 18)
big_font = pygame.font.Font("assets/Bahnschrift.ttf", 64)
calibri_font = pygame.font.SysFont("Calibri", 64)

#obrazki
kierunek_blokady_left = pygame.image.load('assets/blokada w lewo.png')#rozmiar 45 na 35
kierunek_blokady_right = pygame.image.load('assets/blokada w prawo.png')
semafor_right = pygame.image.load('assets/semafor duzy w lewo.png')
semafor_right = pygame.transform.flip(semafor_right, True, False)
semafor_left = pygame.image.load('assets/semafor duzy w lewo.png')
rozjazd_right = pygame.image.load('assets/rozjazd w prawo.png')
rozjazd_left = pygame.image.load('assets/rozjazd w prawo.png')
rozjazd_left = pygame.transform.flip(rozjazd_left, True, False)
train_icon = pygame.image.load("assets/ikona pociągu.png")
train_icon = pygame.transform.scale(train_icon, (120,90))


semaphores = [
    #skm
    Triangle(277, 103, 15, "R501", left=False),
    Triangle(277, 173, 15, "R502", left=False),
    Triangle(285, 103, 12, "exR501", left=True, exit=True),
    Triangle(285, 173, 12, "exR502", left=True, exit=True),
    Triangle(450, 103, 15, "H501", left=True),
    Triangle(450, 173, 15, "H502", left=True),
    Triangle(1665, 103, 15, "B501", left=True),
    Triangle(1665, 173, 15, "B502", left=True),
    Triangle(1660, 103, 12, "exB501", left=False, exit=True),
    Triangle(1660, 173, 12, "exB502", left=False, exit=True),
    Triangle(1430, 103, 15, "C501", left=False),
    Triangle(1430, 173, 15, "C502", left=False),
    Triangle(1080, 103, 15, "G501", left=True),
    Triangle(1080, 173, 15, "G502", left=True),
    Triangle(875, 103, 15, "J501", left=False),
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
    #pod nie skm
    Triangle(275, 600, 15, "O", left=False, invisible=False),
    Triangle(275, 673, 15, "P", left=False, invisible=False),
    Triangle(280, 600, 12, "", left=True, invisible=False),
    Triangle(280, 673, 12, "", left=True, invisible=False),
    Triangle(345, 600, 15, "Y", left=True, invisible=False),
    Triangle(345, 673, 15, "X", left=True, invisible=False),

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
    Block(950, 250, 150, 6, "block72"),
    Block(950, 320, 150, 6, "block72"),
    Block(715, 250, 200, 6, "block72"),
    Block(1135, 250, 50, 6, "block72"),
    Block(1220, 250, 270, 6, "block72"),
    Block(840, 320, 75, 6, "block72"),
    Block(1135, 320, 75, 6, "block72"),
    #nisze nie skm
    Block(10, 600, 60, 6, "block55"),
    Block(75, 600, 60, 6, "block56"),
    Block(140, 600, 60, 6, "block57"),
    Block(10, 670, 60, 6, "block58"),
    Block(75, 670, 60, 6, "block59"),
    Block(140, 670, 60, 6, "block60"),
    Block(300, 600, 40, 6, "block60"),
    Block(300, 670, 40, 6, "block60"),
    Block(360, 600, 342, 6, "block60"),
    Block(360, 670, 600, 6, "block60"),
    Block(995, 670, 200, 6, "block60"),
    Block(1230, 670, 40, 6, "block60"),
    Block(1300, 670, 140, 6, "block60"),
    Block(930, 540, 200, 6, "block60"),
    Block(1165, 540, 60, 6, "block60"),
    Block(835, 540, 60, 6, "block60"),
    #bloki do rozjazdów
    Block(700, 280, 7, 320, "block100"),
]

rozjazdy = [
    Rozjazd(400, 112, 12, 55, right=True),
    Rozjazd(1550, 112, 12, 55, right=False),
    Rozjazd(1500, 112, 12, 55, right=True),
    Rozjazd(1550, 410, 12, 55, right=False),
    Rozjazd(1500, 410, 12, 55, right=True),
    Rozjazd(450, 410, 12, 55, right=True),
    Rozjazd(800, 410, 12, 55, right=True),
    Rozjazd(550, 610, 12, 55, right=True),
    Rozjazd(650, 610, 12, 55, right=False),
    Rozjazd(697, 564, 12, 45, right=True),
    Rozjazd(697, 224, 12, 45, right=True),

]

trains = [

]


TRAIN_CONFIG = {
    "R": {
        "weight": 0,
        "prefixes": ["55", "50", "59", "95", "96", "97"],
        "num_range": (1000, 9999),
        "routes": {
            "Bretowo": "block65",
            "Gdansk Glowny": "block58",
            "Sopot": "block66",
        },
    },
    "SKM": {
        "weight": 100,
        "prefixes": ["59", "95"],
        "num_range": (100, 999),
        "routes": {
            "Gdansk Glowny SKM": "block65",
            "Gdansk Oliwa": "block58",
        },
    },
    "TLK": {
        "weight": 0,
        "num_range": (10000, 99999),
        "routes": {
            "Gdansk Glowny": "block58",
            "Sopot": "block65",
        },
    },
    "IC": {
        "weight": 0,
        "num_range": (1000, 99999),
        "routes": {
            "Gdansk Glowny": "block58",
            "Sopot": "block65",
        },
    },
    "EIP/EIC": {
        "weight": 0,
        "num_range": (1000, 9999),
        "routes": {
            "Gdansk Glowny": "block58",
            "Sopot": "block65",
        },
    },
    "cargo": {
        "weight": 0,
        "num_range": (100000, 999999),
        "routes": {
            "Gdansk Glowny": "block58",
            "Sopot": "block65",
        },
    },
}


def _generate_train_number(cfg: dict) -> str:
    min_val, max_val = cfg["num_range"]
    number_body = str(random.randint(min_val, max_val))
    if "prefixes" in cfg:
        return random.choice(cfg["prefixes"]) + number_body
    return number_body


def spawn_train(blocks, table):
    train_types = list(TRAIN_CONFIG.keys())
    weights = [cfg["weight"] for cfg in TRAIN_CONFIG.values()]
    train_type = random.choices(train_types, weights=weights, k=1)[0]

    cfg = TRAIN_CONFIG[train_type]
    number = _generate_train_number(cfg)
    for train in trains:
        if number == train.number:
            number = _generate_train_number(cfg)
    direction, place = random.choice(list(cfg["routes"].items()))

    track_stop = ""
    if direction == "Gdansk Glowny SKM": track_stop = 502
    if direction == "Gdansk Oliwa": track_stop = 501

    table.add_train(number, place, direction, track_stop)
    return Train(number, place, blocks, direction, track_stop)
table = Table()

# testowy pociąg
trains.append(Train(123, "block65", blocks ,"Gdansk Glowny SKM", 501))
table.add_train(123, "block65", "Gdansk Glowny SKM", 501)

clicked_semaphores = []

# Przebiegi. Nazwa = semafor początkowy + semafor końcowy (klikane po kolei myszką).
#   from_block      - blok, na którym stoi pociąg przed semaforem początkowym
#   direction       - kierunek jazdy tego pociągu: "left" / "right"
#   blocks_block    - bloki przebiegu W KOLEJNOŚCI JAZDY
#   exit_blocks     - (tylko przebiegi wyjazdowe) szlak za stacją, którym pociąg odjeżdża i znika
#   semaphore_block - semafory zastawiane na czas przebiegu (deny)
#   semaphore_allow - semafory, które dają zielone
przebiegi = {
    "R501J501": {
        "from_block": "block57", "direction": "right",
        "blocks_block": ["block161", "block163"],
        "semaphore_block": ["H501", "G501", "J501"],
        "semaphore_allow": ["R501"]
    },
    "R502J502": {
        "from_block": "block60", "direction": "right",
        "blocks_block": ["block162", "block164"],
        "semaphore_block": ["H502", "J502"],
        "semaphore_allow": ["R502"]
    },
    # SKM w prawo
    "J501C501": {
        "from_block": "block163", "direction": "right",
        "blocks_block": ["block179", "block177"],
        "semaphore_block": ["G501", "C501"],
        "semaphore_allow": ["J501"]
    },
    "J502C502": {
        "from_block": "block164", "direction": "right",
        "blocks_block": ["block180", "block178"],
        "semaphore_block": ["G502", "C502"],
        "semaphore_allow": ["J502"]
    },
    "C501exB501": {
        "from_block": "block177", "direction": "right",
        "blocks_block": ["block173"],
        "exit_blocks": ["block71", "block69", "block67", "block65"],
        "semaphore_block": ["C501", "B501"],
        "semaphore_allow": ["C501", "exB501"]
    },
    "C502exB502": {
        "from_block": "block178", "direction": "right",
        "blocks_block": ["block174"],
        "exit_blocks": ["block72", "block70", "block68", "block66"],
        "semaphore_block": ["C502", "B502"],
        "semaphore_allow": ["C502", "exB502"]
    },
    # SKM w lewo
    "B501G501": {
        "from_block": "block71", "direction": "left",
        "blocks_block": ["block173", "block177"],
        "semaphore_block": ["C501", "G501"],
        "semaphore_allow": ["B501"]
    },
    "B502G502": {
        "from_block": "block72", "direction": "left",
        "blocks_block": ["block174", "block178"],
        "semaphore_block": ["C502", "G502"],
        "semaphore_allow": ["B502"]
    },
    "G501H501": {
        "from_block": "block177", "direction": "left",
        "blocks_block": ["block179", "block163"],
        "semaphore_block": ["H501", "J501"],
        "semaphore_allow": ["G501"]
    },
    "G502H502": {
        "from_block": "block178", "direction": "left",
        "blocks_block": ["block180", "block164"],
        "semaphore_block": ["H502", "J502"],
        "semaphore_allow": ["G502"]
    },
    "H501exR501": {
        "from_block": "block163", "direction": "left",
        "blocks_block": ["block161"],
        "exit_blocks": ["block57", "block56", "block55"],
        "semaphore_block": ["R501"],
        "semaphore_allow": ["H501", "exR501"]
    },
    "H502exR502": {
        "from_block": "block164", "direction": "left",
        "blocks_block": ["block162"],
        "exit_blocks": ["block60", "block59", "block58"],
        "semaphore_block": ["R502"],
        "semaphore_allow": ["H502", "exR502"]
    }
}

# Przebiegi ustawione przez dyżurnego: nazwa -> dane (z przebiegi + start, end, train, entered).
# Pociągi same z nich korzystają (Train.take_route).
active_routes = {}

# Semafory, którymi sterują przebiegi - tylko te są resetowane w update_routes()
ROUTE_SIGNALS = {
    name
    for info in przebiegi.values()
    for name in info["semaphore_block"] + info["semaphore_allow"]
}


def przebieg(sem1, sem2):
    print(f"Przebieg z {sem1} do {sem2}")
    name = sem1 + sem2
    info = przebiegi.get(name)
    if info is None or name in active_routes: return

    route_blocks = [b for b in blocks if b.name in info["blocks_block"]]
    if any(b.state != "wolny" for b in route_blocks):
        print(f"Przebieg {name} niemożliwy: odcinek zajęty albo zarezerwowany")
        return

    for b in route_blocks:
        b.state = "przebieg"
    active_routes[name] = dict(info, start=sem1, end=sem2, train=None, entered=False)



def update_routes():
    """Zwalnia przebiegi, z których pociąg już zjechał, i liczy stany semaforów od nowa."""
    for name, r in list(active_routes.items()):
        train = r["train"]
        if train is None:
            continue                              # przebieg czeka na pociąg
        if train.location in r["blocks_block"]:
            r["entered"] = True                   # pociąg jedzie po przebiegu
        elif r["entered"]:
            del active_routes[name]               # pociąg zjechał z przebiegu -> zwolniony

    for s in semaphores:
        if s.name in ROUTE_SIGNALS:
            s.state = "default"
    for r in active_routes.values():
        for s in semaphores:
            if s.name in r["semaphore_block"] and s.state == "default":
                s.state = "deny"
    for r in active_routes.values():
        for s in semaphores:
            # semafor początkowy gaśnie, gdy pociąg wjechał na przebieg
            if s.name in r["semaphore_allow"] and not (r["entered"] and s.name == r["start"]):
                s.state = "allow"


running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    spawn_timer += speed

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        #Klikanie myszką
        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for semaphore in semaphores:
                if semaphore.is_clicked(mouse_x, mouse_y):
                    clicked_semaphores.append(semaphore.name)


    if len(clicked_semaphores) > 2:
        clicked_semaphores = []
    elif len(clicked_semaphores) == 2:
        przebieg(clicked_semaphores[0], clicked_semaphores[1])
        clicked_semaphores = []

    if speed > 0 and spawn_timer % (3000 // speed) == 0:
        trains.append(spawn_train(blocks, table))

    screen.blit(kierunek_blokady_left, (205,80))
    screen.blit(kierunek_blokady_right, (205,150))
    screen.blit(kierunek_blokady_left, (1685,80))
    screen.blit(kierunek_blokady_left, (1685,150))
    screen.blit(kierunek_blokady_left, (1685,380))
    screen.blit(kierunek_blokady_right, (1685,450))
    screen.blit(kierunek_blokady_left, (205,380))
    screen.blit(kierunek_blokady_right, (205,450))
    screen.blit(kierunek_blokady_left, (205,580))
    screen.blit(kierunek_blokady_right, (205,650))
    screen.blit(semafor_left, (855,391))
    screen.blit(semafor_left, (855,462))
    screen.blit(semafor_right, (1455,391))
    screen.blit(semafor_right, (1455,462))
    screen.blit(semafor_left, (1275,391))
    screen.blit(semafor_left, (1275,462))
    screen.blit(semafor_right, (1170,391))
    screen.blit(semafor_right, (1170,462))
    screen.blit(semafor_right, (1170,462))
    screen.blit(semafor_right, (1170,462))
    screen.blit(semafor_left, (920,242))
    screen.blit(semafor_left, (920,312))
    screen.blit(semafor_right, (1100,242))
    screen.blit(semafor_right, (1100,312))
    screen.blit(semafor_left, (1190,242))
    screen.blit(semafor_left, (965,662))
    screen.blit(semafor_right, (1195,662))
    screen.blit(semafor_left, (1275,662))
    screen.blit(semafor_right, (1440,662))
    screen.blit(semafor_left, (900,532))
    screen.blit(semafor_right, (1130,532))

    table.update_draw(screen)
    for triangle in semaphores:
        triangle.draw(screen)


    for train in trains[:]:
        train.update(blocks, active_routes)
        if train.finished:
            trains.remove(train)
            train_counter +=1
    update_routes()

    for rozjazd in rozjazdy:
        rozjazd.draw(screen)


    for block in blocks:
        block.draw(screen)
        # To debug nazwy odcinków torowych
        screen.blit(font.render(f"{block.name}".replace("block", ""), True, "gray"), ((block.left + 10), block.top - 10))
        if block.state == "zajety":
            for train in trains:
                if train.location == block.name:
                    font.set_bold(True)
                    screen.blit(font.render(" "+ str(train.number)+" ", True, "white", "black"), (block.left + (len(str(train.number))*5)%block.width, block.top-6))
                    font.set_bold(False)

    # Pasek Tolerancji
    for train in trains:
        if train.iswaiting:
            toleration += -0.3
    pygame.draw.rect(screen, "orange", (50, 10, toleration * 18, 30))
    pygame.draw.rect(screen, "blue", (50, 10, 1800, 30), width=2)

    # licznik pociągów
    screen.blit(train_icon, (100, SCREEN_HEIGHT-200))
    screen.blit(big_font.render(str(train_counter), True, (255, 255, 255)), (50, SCREEN_HEIGHT-150))

    # Przegrywanie
    if toleration <= 0:
        screen.fill("black")
        screen.blit(calibri_font.render("Przegrałeś                    ", True, "red"), (-100 +SCREEN_WIDTH/2, -300+SCREEN_HEIGHT/2))
        screen.blit(calibri_font.render("Wygenerowałeś za dużo opóźnień", True, (255, 255, 255)), (-400 +SCREEN_WIDTH/2, -200+SCREEN_HEIGHT/2))
        screen.blit(calibri_font.render(f"Twój wynik to {train_counter}", True, (255, 255, 255)), (-200 +SCREEN_WIDTH/2, -100+SCREEN_HEIGHT/2))
        screen.blit(calibri_font.render("Słabiutko :P", True, "green"), (-120 + SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    pygame.display.update()
pygame.quit()