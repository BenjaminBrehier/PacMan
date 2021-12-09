import pygame

class Pac:
    def __init__(self, fen, x, y):
        self.fen = fen
        self.x = x
        self.y = y
        self.preX = ""
        self.preY = ""
        self.height = 34
        self.width = 34
        self.score = 0
        self.image = pygame.image.load("/Users/benjaminbrehier/Documents/PacMan/img/Pac.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image2 = pygame.image.load("/Users/benjaminbrehier/Documents/PacMan/img/PacFerme2.png").convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (self.width, self.height))
        self.direction = ""
        self.super = False
        self.compteurSuper = 0
        fen.blit(self.image, (x, y))

    def changeImg(self):        #Alterne l'image entre le PacMan bouche ouverte et bouche fermée
        img = self.image
        self.image = self.image2
        self.image2 = img
        
    def turnLeft(self):         #Oriente le PacMan vers la gauche
        image = pygame.transform.rotate(self.image, 180)
        self.fen.fill(0x000)
        self.fen.blit(image, (self.x, self.y))
        self.direction = "left"

    def turnRight(self):        #Oriente le PacMan vers la droite
        self.fen.fill(0x000)
        self.fen.blit(self.image, (self.x, self.y))
        self.direction = "right"

    def turnUp(self):           #Oriente le PacMan vers le haut
        image = pygame.transform.rotate(self.image, 90)
        self.fen.fill(0x000)
        self.fen.blit(image, (self.x, self.y))
        self.direction = "up"

    def turnDown(self):         #Oriente le PacMan vers le bas
        image = pygame.transform.rotate(self.image, -90)
        self.fen.fill(0x000)
        self.fen.blit(image, (self.x, self.y))
        self.direction = "down"

    def move(self, walls):             #Déplace le PacMan
        self.preX = self.x
        self.preY = self.y
        if (self.direction == "left"):  
            if (self.thereNoWallOn(walls, self.direction)):
                if (self.isSuper()):
                    self.x -= 2
                else:
                    self.x -= 1
                self.turnLeft()
        elif (self.direction == "right"):
            if (self.thereNoWallOn(walls, self.direction)):
                if (self.isSuper()):
                    self.x += 2
                else:
                    self.x += 1
                self.turnRight()
        elif (self.direction == "up"):
            if (self.thereNoWallOn(walls, self.direction)):
                if (self.isSuper()):
                    self.y -= 2
                else:
                    self.y -= 1
                self.turnUp()
        elif (self.direction == "down"):
            if (self.thereNoWallOn(walls, self.direction)):
                if (self.isSuper()):
                    self.y += 2
                else:
                    self.y += 1
                self.turnDown()

    def thereNoWallOn(self, walls, direction):         #Vérifie si un mur se trouve devant le PacMan
        for wall in walls:
            if (self.y < wall.y1 and self.y+self.height > wall.y):
                if (direction == "left"):
                    if (abs(self.x - wall.x1) < 3):
                        return False
                elif (direction == "right"):
                    if (abs((self.x+self.width) - wall.x) < 3):
                        return False
            elif (self.x < wall.x1 and self.x+self.width > wall.x):
                if (direction == "up"):
                    if (abs(self.y - wall.y1) < 2):
                        return False
                elif (direction == "down"):
                    if (abs((self.y+self.height) - wall.y) < 2):
                        return False
        return True

    def pointPlace(self, points):       #Incrémente le score lorsque le PacMan se trouve sur un point
        for pt in points:
            if (pt.x >= self.x and pt.x <= self.x+self.height and pt.y >= self.y and pt.y <= self.y+self.height):
                if (pt.type == "point"):
                    self.score += 1
                else:
                    self.super = True
                    self.compteurSuper += 500
                points.remove(pt)

    def isMoving(self):     #True si PacMan se déplace
        if (self.x == self.preX and self.y == self.preY):
            return False
        else:
            return True

    def isSuper(self):      #True si PacMan est en mode super (peut manger les fantômes)
        return self.super