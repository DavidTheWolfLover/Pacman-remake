import pygame
import numpy as np


def main():
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 51, 0)
    RED = (255, 0, 0)
    pygame.init()

    screen_height = 600
    screen_width = 900

    DISPLAY = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    DISPLAY.fill(WHITE)

    #pygame.draw.rect(DISPLAY, BLACK, (200, 150, 10, 10))
    dist = 50  #real dist between two squares is 40 (40 + 10 from the top left corner of the square)
    marg = 20  # margin
    square_size = 10
    n = screen_height // dist
    m = screen_width // dist
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        for i in range(n):
            for j in range(m):
                """
                if (.............) : #is path => put food there
                    pygame.draw.rect(DISPLAY, BLACK,(j * dist + marg, i * dist + marg, square_size, square_size))
                else if (...........) : #is special skill 
                    ................................
                else: #is wall
                    ............................... """
                if (i == 1 and j == 2) or (i == n - 2 and j == m - 3): # is_food
                    pygame.draw.circle(DISPLAY, RED, (j * dist + marg + square_size / 2, i * dist + marg + square_size / 2),7)
                else:
                    pygame.draw.rect(DISPLAY, BLUE,(j * dist + marg, i * dist + marg, square_size, square_size))
        pygame.display.update()

main()
