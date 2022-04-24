import pygame
running = True

MUST = (0, 0, 0)
VALGE = (255, 255, 255)
ORANZ = (250, 147, 30)

screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumememm - Laura Kramp")
screen.fill([0, 0, 0])


def draw_lumememm(screen, x, y):
    #Keha
    pygame.draw.circle(screen, VALGE, [60 + x, 20 + y], 30)
    pygame.draw.circle(screen, VALGE, [60 + x, 90 + y], 45)
    pygame.draw.circle(screen, VALGE, [60 + x, 180 + y], 60)
    #Silmad
    pygame.draw.circle(screen, MUST, [54 + x, 19 + y], 3)
    pygame.draw.circle(screen, MUST, [66 + x, 19 + y], 3)
    #Nina
    pygame.draw.polygon(screen, ORANZ, [[55 + x, 30 + y], [65 + x, 30 + y], [60 + x, 45 + y]], 0)

pygame.display.flip()

draw_lumememm(screen,75, 30)
pygame.display.flip()


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False