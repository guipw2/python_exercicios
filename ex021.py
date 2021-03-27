import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('roses.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
while(pygame.mixer.music.get_busy()): pass
