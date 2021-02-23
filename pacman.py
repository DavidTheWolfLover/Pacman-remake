import pygame
import numpy as np


def main():
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 51, 0)
    pygame.init()

    screen_height = 600
    screen_width = 900

    DISPLAY = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    DISPLAY.fill(WHITE)

    #pygame.draw.rect(DISPLAY,BLACK,(200,150,10,10))
    dist = 50  #real dist between two squares is 40 (40 + 10 from the top left corner of the square)
    marg = 20  # margin
    n = screen_height // dist
    m = screen_width // dist
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for i in range(n):
            for j in range(m):
                pygame.draw.rect(DISPLAY, BLACK,(j * dist + marg, i * dist + marg, 10, 10))
        pygame.display.update()

main()