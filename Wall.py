import pygame

class Wall:
    def __init__(self, fen, x, y, x1, y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.fen = fen
        blue = (0,0,255)
        pygame.draw.rect(fen,blue,[x,y,x1-x, y1-y])


    def reload(self):       #Replace le mur
        blue = (0,0,255)
        pygame.draw.rect(self.fen,blue,[self.x,self.y,self.x1-self.x, self.y1-self.y])
