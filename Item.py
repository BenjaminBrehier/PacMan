import pygame

class Point:
    def __init__(self, fen, x, y):
        self.x = x
        self.y = y
        self.fen = fen
        jaune = (255,255,0)
        pygame.draw.circle(fen, jaune, (self.x, self.y), 5, 9)

    def reload(self):
        jaune = (255,255,0)
        pygame.draw.circle(self.fen, jaune, (self.x, self.y), 5, 9)