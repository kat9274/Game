<<<<<<< HEAD
import Config
import pygame

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

def Plant(x, y):
    DISPLAYSURF.blit(pygame.image.load('Plant1.png'), (x,y))

pygame.display.set_caption('Tree Game')
x = 0
y = 1
while True: # main game loop
    DISPLAYSURF.fill((0,0,200))
    Plant(x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    x = x+1
    y = y +1
    pygame.display.update()
=======
from Config import *
import pygame, random
pygame.init()

#def PlantGrowImage(grow):
#    if grow <= 25
#       Num = 1
 #  elif grow <= 50
#       Num = 3
 #  elif grow<= 75
#       Num = 4
 #  elif grow <= 100
#       Num = 6
 #  return pygame.image.load(f"Plant{Num}.png")

class Tree:
    def __init__(self, Pos):
        self.Pos = Pos
        self.Img = pygame.image.load("Plant6.png")

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

Plant = Tree((0, 0))

while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (100, 60, 1), pygame.Rect(0, 350, 1000, 150))
    pygame.draw.rect(screen, (0, 128, 200), pygame.Rect(0, 0, 1000, 350))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePos = pygame.mouse.get_pos()
            Plant = Tree((MousePos[0], 125))
    screen.blit(Plant.Img, Plant.Pos)

    pygame.display.flip()
    clock.tick(60)
>>>>>>> e8f460a6d935193c44e55aaa69c369ea3c63ac0e
