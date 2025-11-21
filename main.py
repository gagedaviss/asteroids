import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    version = pygame.version.ver
    
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = float(0)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0

        for sprite in drawable:
            sprite.draw(screen)

        updatable.update(dt)
        log_state()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        clock.tick(60)

        #print(dt)



if __name__ == "__main__":
    main()