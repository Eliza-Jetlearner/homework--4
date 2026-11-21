import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img = pygame.image.load("backgroundone.jpg")
image = pygame.transform.scale(img, (WIDTH,HEIGHT))

time.sleep(3)
font = pygame.font.SysFont("Times New Roman",72)
text = font.render("Happy Birthday",True,(0,0,0))
display_surface.fill((255,255,255))
display_surface.blit(image,(0,0))
display_surface.blit(text,(210,180))
pygame.display.update()