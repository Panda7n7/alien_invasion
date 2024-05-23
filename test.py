import sys

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
