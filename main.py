import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

version = pygame.version.ver

def main():
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}\n
            Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()