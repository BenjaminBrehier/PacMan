from Perso import Pac
from Wall import Wall
from Item import Point
from Item import Fruit

class Map:
    def __init__(self, fen, width, height):
        self.fen = fen
        self.width = width
        self.height = height
        self.pacman = ""
        self.MAP = [
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
        ]
        self.points = []
        self.walls = []
        self.fruits = []
        for i in range(len(self.MAP)):
            for j in range(len(self.MAP[i])):
                if (self.MAP[i][j] == 1):
                    pt = Point(self.fen, (j+0.5)*self.width/19, (i+0.5)*self.height/22, "point")
                    self.points.append(pt)
                elif (self.MAP[i][j] == 0):
                    wall = Wall(self.fen, j*self.width/19, i*self.height/22, (j+1)*self.width/19, (i+1)*self.height/22)
                    self.walls.append(wall)
                elif (self.MAP[i][j] == 5):
                    self.pacman = Pac(self.fen, j*self.width/19, i*self.height/22)
                elif (self.MAP[i][j] == 4):
                    pt = Point(self.fen, (j+0.5)*self.width/19, (i+0.5)*self.height/22, "power")
                    self.points.append(pt)

            
        cerise = Fruit(fen, 9*width/19, 12*height/22, "cherry")
        self.fruits.append(cerise)
        


    def reload(self):
        self.fen.fill(0x000)
        strawberry = Fruit(self.fen, 9*self.width/19, 12*self.height/22, "strawberry")
        orange = Fruit(self.fen, 9*self.width/19, 12*self.height/22, "orange")
        apple = Fruit(self.fen, 9*self.width/19, 12*self.height/22, "apple")
        melon = Fruit(self.fen, 9*self.width/19, 12*self.height/22, "melon")
        if (self.pacman.round == 2):
            self.fruits.append(strawberry)
        elif (self.pacman.round == 3):
            self.fruits.append(orange)
        elif (self.pacman.round == 4):
            self.fruits.append(apple)
        elif (self.pacman.round == 5):
            self.fruits.append(melon)

        self.points = []
        self.walls = []
        self.fruits = []
        for i in range(len(self.MAP)):
            for j in range(len(self.MAP[i])):
                if (self.MAP[i][j] == 1):
                    pt = Point(self.fen, (j+0.5)*self.width/19, (i+0.5)*self.height/22, "point")
                    self.points.append(pt)
                elif (self.MAP[i][j] == 0):
                    wall = Wall(self.fen, j*self.width/19, i*self.height/22, (j+1)*self.width/19, (i+1)*self.height/22)
                    self.walls.append(wall)
                # elif (self.MAP[i][j] == 5):
                #     self.pacman = Pac(self.fen, j*self.width/19, i*self.height/22)
                elif (self.MAP[i][j] == 4):
                    pt = Point(self.fen, (j+0.5)*self.width/19, (i+0.5)*self.height/22, "power")
                    self.points.append(pt)
        


