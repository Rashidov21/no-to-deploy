import pygame 
import sys

pygame.init()

game_window = pygame.display.set_mode((320,240))

WHITE = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    game_window.fill(WHITE)
    pygame.display.flip()