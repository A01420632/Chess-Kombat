import pygame

class peleador():
    def __init__(self, player , x, y,):
        self.player= player
        self.flip = False
        self.rect = pygame.Rect((x,y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.atk_type= 0
        self.vida= 100
        
        
        
    def mov(self, largop, anchop,superficie, target):
        speed = 10
        gravedad = 2
        dx = 0
        dy = 0
        
        if self.attacking==False and self.vida>0:
        
            if self.player==1:
                #movimiento
                key= pygame.key.get_pressed()
                if key[pygame.K_a]:
                    dx = -speed
                if key[pygame.K_d]:
                    dx = speed
                #salto
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
        
            #Ataques
                if key[pygame.K_e] or key[pygame.K_q]:
                    self.atk (superficie, target)
                #para ver que tipo de ataque es    
                    if key[pygame.K_e]:
                        self.atk_type =1
                    if key[pygame.K_q]:
                        self.atk_type =2
                        
            #jugador 2
        
            if self.player==2:
                #movimiento
                key= pygame.key.get_pressed()
                if key[pygame.K_j]:
                    dx = -speed
                if key[pygame.K_l]:
                    dx = speed
                #salto
                if key[pygame.K_i] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
        
            #Ataques
                if key[pygame.K_u] or key[pygame.K_o]:
                    self.atk (superficie, target)
                #para ver que tipo de ataque es    
                    if key[pygame.K_u]:
                        self.atk_type =1
                    if key[pygame.K_o]:
                        self.atk_type =2
        
            
        #salto con gravedad
        self.vel_y += gravedad
        dy+= self.vel_y
            
            
           #mantenerse en pantalla  
        if self.rect.left + dx <0:
            dx = 0-self.rect.left
            
        if self.rect.right + dx >largop:
            dx = largop -self.rect.right
        
        if self.rect.bottom + dy > anchop - 120:
            self.vel_y = 0
            self.jump= False
            dy = anchop - 120 -self.rect.bottom
            
        #jugadores mirarse
        if target.rect.centerx > self.rect.centerx:
            self.flip= False
        else:
            self.flip= True
        
        self.rect.x += dx
        self.rect.y += dy
    
    def atk(self, superficie, target):
        self.attacking= True
        attacking_rect = pygame.Rect(self.rect.centerx- (2*self.rect.width*self.flip), self.rect.y,2*self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.vida -= 1
            self.attacking= False
            
        else:
            self.attacking= False
        
        
        pygame.draw.rect(superficie, (0, 255, 0), attacking_rect)
        
    def draw(self, surface):
        pygame.draw.rect(surface,(255,0,0), self.rect)
        
    