import pygame
running = True
#Määrab värvid mida kasutada
MUST = (0, 0, 0)
VALGE = (255, 255, 255)
ORANZ = (250, 147, 30)
#Joonistab akna suuruses 300x300
screen=pygame.display.set_mode([300,300])
#Määrab akna nime
pygame.display.set_caption("Lumememm - Laura Kramp")
#määrab taustavärvi
screen.fill([0, 0, 0])

#defineerib lumememme ringid ja värvid

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

draw_lumememm(screen,75, 30)
pygame.display.flip()

#võimaldab akna lahti hoida ja sulgeda ristist
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False