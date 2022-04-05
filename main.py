import pygame
import sys
from settings import *
import player

#Initialize pygame
pygame.init()

#Create the main window
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Rapid Game")

#Create the clock
clock = pygame.time.Clock()

#Get the screen size
screen_width, screen_height = display_surface.get_size()

#Load in backgrounds
bg_1 = pygame.transform.scale(pygame.image.load("BG_01.png").convert(), (screen_width, screen_height))
bg_1_rect = bg_1.get_rect(topleft = (0,0))
bg_2 = pygame.transform.scale(pygame.image.load("BG_02.png").convert(), (screen_width, screen_height))
bg_2_rect = bg_2.get_rect(topleft = (0,0))
bg_3 = pygame.transform.scale(pygame.image.load("BG_03.png").convert(), (screen_width, screen_height))
bg_3_rect = bg_3.get_rect(topleft = (0,0))
bg_4 = pygame.transform.scale(pygame.image.load("BG_04.png").convert(), (screen_width, screen_height))
bg_4_rect = bg_4.get_rect(topleft = (0,0))

#Create the player
player = player.Player('Knight', (150, screen_height - 50))
player_group = pygame.sprite.GroupSingle(player)

#Create the main game loop
running = True
while running:
    #Get all the events that have occurred and see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit the background to the screen
    display_surface.blit(bg_1, bg_1_rect)

    #Blit the player
    player_group.update()
    player_group.draw(display_surface)

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
