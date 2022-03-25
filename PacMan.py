import pygame
from Map import Map
import pygame.time

clock = pygame.time.Clock()
pygame.init()
width = 684
height = 770
fen = pygame.display.set_mode((width, height))
pygame.display.update()

map = Map(fen, width, height)
pacman = map.pacman


nbPoints = len(map.points)
fruitSpawned = False
run = True
i = 0
font = pygame.font.Font(None, 32)
var = []
var.append(i)       #Rend i modifiable dans toutes fonctions
var.append(fruitSpawned)


def continu():      #Réaffiche tous les éléments 
    var[0]+=1    
    if (var[0]%10 == 0):
        pacman.changeImg()
        
    pacman.pointPlace(map.points)

    if (pacman.isSuper() == True):
        pacman.compteurSuper -=1
        if (pacman.compteurSuper == 0):
            pacman.super = False

    pacman.move(map.walls)
    for pt in map.points:
        pt.reload()

    if (len(map.points)*2 == nbPoints):
        var[1] = True

    if (var[1] == True):
        pacman.fruitPlace(map.fruits)
        for fruit in map.fruits:
            fruit.reload()

    for wall in map.walls:
        wall.reload()

    textsurface = font.render('Score: '+str(pacman.score), False, pygame.Color('#39FFF9'))
    textRect = textsurface.get_rect()
    textRect.center = (0.9*width, 0.03*height)
    fen.blit(textsurface, textRect)

    # print("x = ", pacman.x, " y = ", pacman.y)
    pygame.display.update()

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                while(not pacman.thereNoWallOn(map.walls, "left") and pacman.isMoving()):
                    continu()
                pacman.turnLeft()
            if event.key == pygame.K_RIGHT:
                while(not pacman.thereNoWallOn(map.walls, "right") and pacman.isMoving()):
                    continu()    
                pacman.turnRight()

            if event.key == pygame.K_UP:
                while(not pacman.thereNoWallOn(map.walls, "up") and pacman.isMoving()):
                    continu()    
                pacman.turnUp()

            if event.key == pygame.K_DOWN:
                while(not pacman.thereNoWallOn(map.walls, "down") and pacman.isMoving()):
                    continu()    
                pacman.turnDown()

    continu()

pygame.quit()
