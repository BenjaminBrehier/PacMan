import pygame

class Point:
    def __init__(self, fen, x, y, type):
        self.x = x
        self.y = y
        self.fen = fen
        self.type = type
        self.size = 5
        if (type == "point"):
            self.color = (255,255,0)
        else:
            self.color = (216,223,217)
            self.size = 8
        pygame.draw.circle(fen, self.color, (self.x, self.y), self.size, 9)

    def reload(self):
        pygame.draw.circle(self.fen, self.color, (self.x, self.y), self.size, 9)

class Fruit:
    def __init__(self, fen, x, y, type):
        self.fen = fen
        self.x = x
        self.y = y
        self.type = type
        self.size = 30
        if (type == "cherry"):
            self.value = 100
            self.image = pygame.image.load("/Users/benjaminbrehier/Documents/Dev/PacMan/img/cherry.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            # self.fen.blit(self.image, (self.x+4, self.y))
        elif (type == "strawberry"):
            self.value = 300
            self.image = pygame.image.load("/Users/benjaminbrehier/Documents/Dev/PacMan/img/strawberry.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            # self.fen.blit(self.image, (self.x+4, self.y))
        elif (type == "orange"):
            self.value = 500
            self.image = pygame.image.load("/Users/benjaminbrehier/Documents/Dev/PacMan/img/orange.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            # self.fen.blit(self.image, (self.x+4, self.y))
        elif (type == "apple"):
            self.value = 700
            self.image = pygame.image.load("/Users/benjaminbrehier/Documents/Dev/PacMan/img/apple.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            # self.fen.blit(self.image, (self.x+4, self.y))
        elif (type == "melon"):
            self.value = 1000
            self.image = pygame.image.load("/Users/benjaminbrehier/Documents/Dev/PacMan/img/melon.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            # self.fen.blit(self.image, (self.x+4, self.y))

    def reload(self):
        self.fen.blit(self.image, (self.x, self.y))