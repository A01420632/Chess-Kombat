import pygame
from peleadores import peleador
pygame.init()

largop= 800
anchop= 800

fondo= pygame.display.set_mode((largop, anchop))
pygame.display.set_caption("pelea")

#fps
clock = pygame.time.Clock()
FPS= 60

amarillo= (255, 255, 0)
rojo= (255,0,0)
blanco= (255,255,255)
verde= (0,255,0)

P1_tamaño=128
P1_data= [P1_tamaño]
P2_tamaño=128
P2_data= [P2_tamaño]

fondoA = pygame.image.load("assets/images/Fondo1.Jpg").convert_alpha()

#sprites: fueron sacados de internet


#orden: iddle, A1, A2, R, J

p1_animation_steps=[5,5,4,6,6]
p2_animation_steps=[5,5,3,8,7]

#fondo
def draw_fondo():
    #escalar la imagen de fondo a la resolucion deseada
    scale_fondo = pygame.transform.scale(fondoA,(800,800))
    fondo.blit(scale_fondo,(0,0))

#barra de vida
def draw_vida_barra(vida,x,y):
    ratio= vida / 100
    pygame.draw.rect(fondo, rojo, (x,y, 300, 30))
    pygame.draw.rect(fondo, verde, (x,y, 300* ratio, 30))

peleador_1 = peleador(1,200,310)
peleador_2 = peleador(2,500,310)


run= True
while run:
    clock.tick(FPS)
    
    draw_fondo()
    
    #Barras de vida
    draw_vida_barra(peleador_1.vida, 20, 20)
    draw_vida_barra(peleador_2.vida, 480, 20)
    
    #movimiento de los 2 peleadores
    peleador_1.mov(largop,anchop,fondo, peleador_2,)
    peleador_2.mov(largop,anchop,fondo, peleador_1,)
    #los 2 peleadores
    peleador_1.draw(fondo)
    peleador_2.draw(fondo)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
            
    pygame.display.update()
            
pygame.quit()

