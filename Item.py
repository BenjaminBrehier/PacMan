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
        if (type == "cerise"):
            self.value = 100
            self.image = pygame.image.load("/Users/benjaminbrehier/Documents/PacMan/img/Cerise.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.fen.blit(self.image, (self.x+4, self.y))

    def reload(self):
        self.fen.blit(self.image, (self.x, self.y))