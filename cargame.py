#uvoz knjiznice pygame
import pygame
from pygame.locals import *
import random

#nastavimo velikost zaslona in ceste
size = width, height = (1050,1050)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
#dolocimo pozicijo levega in desnega pasu
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
#nastavimo hitrost nasprotnega avtomobila
speed = 1

#nastavimi pygame na runing true
pygame.init()
running = True

#velikost zaslona
screen = pygame.display.set_mode(size)
#naslov igre
pygame.display.set_caption("dirkaska igra")
#barva ozadja
screen.fill((60, 220, 0))
#posodobitev sprememb
pygame.display.update()

# vstavljanje igralcevega vozila
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

# vstavljanje nasprotnega vozila
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

#nastavljanje pisave
pygame.font.init()
font = pygame.font.SysFont('Arial', 30)

#točkovalnik
score = 0
counter = 0

# zanka tockovnika
while running:
    counter += 1

    # povisanje tezavnosti pri dosezenem levelu
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)

    # premikanje nasprotnega vozila
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # povecanje tock ko igralec izogne nasprotnemu avtomobilu
        score += 1

        # nakljucna izbira pasa
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    #kdaj se igra konca
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        running = False

    # delovanje igre
    for event in pygame.event.get():
        if event.type == QUIT:
            #konec igre
            running = False
        if event.type == KEYDOWN:
            # premikanje avta 1 na levo
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            # premikanje avta 1 na desno
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])

    #narisi cesto
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
    #narisi sredinsko crto ceste
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
    # narisi levo oznako ceste
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    # narisi desno oznako ceste
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

    # postavljanje avtov na cesto
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)

    # prikaz tockovanja
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    #ozadje za tockovnik
    text_rect = score_text.get_rect(topleft=(10, 10))
    pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(10, 10))
    screen.blit(score_text, text_rect)

    # posodobi spremembe
    pygame.display.update()

#zaprtje igre
pygame.quit()
