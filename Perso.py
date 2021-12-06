import pygame

class Pac:
    def __init__(self, fen, x, y):
        self.fen = fen
        self.x = x
        self.y = y
        self.preX = ""
        self.preY = ""
        self.height = 35
        self.width = 36
        self.score = 0
        self.image = pygame.image.load("/Users/benjaminbrehier/OneDrive/ProjetDev/Python/PacMan/img/Pac.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image2 = pygame.image.load("/Users/benjaminbrehier/OneDrive/ProjetDev/Python/PacMan/img/PacFerme2.png").convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (self.width, self.height))
        self.direction = ""
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
                self.x -= 1
                self.turnLeft()
        elif (self.direction == "right"):
            if (self.thereNoWallOn(walls, self.direction)):
                self.x += 1
                self.turnRight()
        elif (self.direction == "up"):
            if (self.thereNoWallOn(walls, self.direction)):
                self.y -= 1
                self.turnUp()
        elif (self.direction == "down"):
            if (self.thereNoWallOn(walls, self.direction)):
                self.y += 1
                self.turnDown()

    def thereNoWallOn(self, walls, direction):         #Vérifie si un mur se trouve devant le PacMan
        for wall in walls:
            if (self.y < wall.y1 and self.y+self.height > wall.y):
                if (direction == "left"):
                    if (abs(self.x - wall.x1) < 1):
                        return False
                elif (direction == "right"):
                    if (abs((self.x+self.width) - wall.x) < 1):
                        return False
            elif (self.x < wall.x1 and self.x+self.width > wall.x):
                if (direction == "up"):
                    if (abs(self.y - wall.y1) < 1):
                        return False
                elif (direction == "down"):
                    if (abs((self.y+self.height) - wall.y) < 1):
                        return False
        return True

    def pointPlace(self, points):       #Incrémente le score lorsque le PacMan se trouve sur un point
        for pt in points:
            if (pt.x >= self.x and pt.x <= self.x+self.height and pt.y >= self.y and pt.y <= self.y+self.height):
                self.score += 1
                print("Score: ", self.score)
                points.remove(pt)

    def isMoving(self):
        if (self.x == self.preX and self.y == self.preY):
            return False
        else:
            return True