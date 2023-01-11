import pygame

from Assets.settings import * 
from Assets.World import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
levle = World(level_map, screen)

def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
            
        screen.fill('white')
        levle.run()
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    run()