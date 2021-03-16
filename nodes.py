import pygame
from vector import Vector2
from constants import *

class Node(object):
    def __init__(self, row, column):
        self.row = row          # } Tile_location
        self.column = column    # }
        self.location = Vector2(column * Tile_Width,row * Tile_Height) #App_location
        self.near = {UP:None, DOWN:None, RIGHT:None, LEFT:None} #nearby neighbors

    def draw_near(self,screen):
        for i in self.near.keys():
            if (self.near[i] is not None):
                start = (self.location.x,self.location.y) #start point line
                end = (self.near[i].location.x,self.near[i].location.y) #finish point line
                pygame.draw.line(screen,white,start,end,4)
                pygame.draw.circle(screen,red,start,12)

class Group_Nodes(object):
    def __init__(self):
        self.points = []
    def create_nodes(self):
        A = Node(5, 5)
        B = Node(5, 10)
        C = Node(10, 5)
        D = Node(10, 10)
        E = Node(10, 13)
        F = Node(20, 5)
        G = Node(20, 13)
        A.near[RIGHT] = B
        A.near[DOWN] = C
        B.near[LEFT] = A
        B.near[DOWN] = D
        C.near[UP] = A
        C.near[RIGHT] = D
        C.near[DOWN] = F
        D.near[UP] = B
        D.near[LEFT] = C
        D.near[RIGHT] = E
        E.near[LEFT] = D
        E.near[DOWN] = G
        F.near[UP] = C
        F.near[RIGHT] = G
        G.near[UP] = E
        G.near[LEFT] = F
        self.points = [A, B, C, D, E, F ,G]
    def refresh(self,screen):
        for i in self.points:
            i.draw_near(screen)
        pygame.draw.line(screen,green,(3*Tile_Width,5*Tile_Height),(3*Tile_Width,10*Tile_Height),2)

