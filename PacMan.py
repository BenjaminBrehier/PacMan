import pygame
from Perso import Pac
from Wall import Wall
from Item import Point
pygame.init()
width = 684
height = 770
fen = pygame.display.set_mode((width, height))
image = pygame.image.load("/Users/benjaminbrehier/OneDrive/ProjetDev/Python/PacMan/img/background.jpg").convert_alpha()
image = pygame.transform.scale(image, (900, 900))
pygame.display.update()




MAP = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 4, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 4, 0],
	[0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
	[0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
	[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
	[2, 2, 2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2, 2, 2],
	[0, 0, 0, 0, 1, 0, 1, 0, 0, 3, 0, 0, 1, 0, 1, 0, 0, 0, 0],
	[2, 2, 2, 2, 1, 1, 1, 0, 3, 3, 3, 0, 1, 1, 1, 2, 2, 2, 2],
	[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
	[2, 2, 2, 0, 1, 0, 1, 1, 1, 5, 1, 1, 1, 0, 1, 0, 2, 2, 2],
	[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
	[0, 4, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 4, 0],
	[0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
	[0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
];

points = []
walls = []
for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if (MAP[i][j] == 1):
            pt = Point(fen, (j+0.5)*width/19, (i+0.5)*height/22)
            points.append(pt)
        elif (MAP[i][j] == 0):
            wall = Wall(fen, j*width/19, i*height/22, (j+1)*width/19, (i+1)*height/22)
            walls.append(wall)
        elif (MAP[i][j] == 5):
            pacman = Pac(fen, j*width/19, i*height/22)
    

run = True
i = 0
font = pygame.font.Font(None, 32)

def continu():
    pacman.pointPlace(points)
    
    pacman.move(walls)
    for pt in points:
        pt.reload()

    for wall in walls:
        wall.reload()

    textsurface = font.render('Score: '+str(pacman.score), False, pygame.Color('#39FFF9'))
    textRect = textsurface.get_rect()
    textRect.center = (620, 20)
    fen.blit(textsurface, textRect)

    #print("x = ", pacman.x, " y = ", pacman.y)
    pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                while(not pacman.thereNoWallOn(walls, "left") and pacman.isMoving()):
                    i+=1    
                    if (i%10 == 0):
                        pacman.changeImg()
                    continu()
                pacman.turnLeft()
            if event.key == pygame.K_RIGHT:
                while(not pacman.thereNoWallOn(walls, "right") and pacman.isMoving()):
                    i+=1    
                    if (i%10 == 0):
                        pacman.changeImg()
                    continu()    
                pacman.turnRight()

            if event.key == pygame.K_UP:
                while(not pacman.thereNoWallOn(walls, "up") and pacman.isMoving()):
                    i+=1    
                    if (i%10 == 0):
                        pacman.changeImg()
                    continu()    
                pacman.turnUp()

            if event.key == pygame.K_DOWN:
                while(not pacman.thereNoWallOn(walls, "down") and pacman.isMoving()):
                    i+=1    
                    if (i%10 == 0):
                        pacman.changeImg()
                    continu()    
                pacman.turnDown()

    i+=1    
    if (i%10 == 0):
        pacman.changeImg()
    continu()

pygame.quit()
