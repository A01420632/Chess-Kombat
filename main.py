from pygame import *
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN
init()

screen = display.set_mode((800,800))

mixer.init()
comer = mixer.Sound("assets/sounds/comer.wav")

epic=mixer.Sound("assets/sounds/musica epica.mp3")
cancion=mixer.Sound("assets/sounds/Waltz_nocturne.mp3")

def play_song(song_index):
    mixer.music.load(playlist[song_index])
    mixer.music.play()


matriz_posiciones = [[(20 + i*100, 15 + j*100) for i in range(8)] for j in range(8)]

imagenes=[['TN','CN','AN','QN','RN','AN','CN','TN'],
          ['PN','PN','PN','PN','PN','PN','PN','PN']]

Equipo_blanco=['TB','CB','AB','RB','QB','PB']
Equipo_negro=['TN','CN','AN','QN','RN','PN']

turno_actual = "blanco"

for i in range(4):
    imagenes.append(['' for j in range(8)])
#imagenes.append([['' for i in range(8)] for j in range(4)])
imagenes.append(['PB','PB','PB','PB','PB','PB','PB','PB'])
imagenes.append(['TB','CB','AB','QB','RB','AB','CB','TB'])
print(imagenes)

def get_pieza(x, y):
    fila = y // 100
    columna = x // 100
    return imagenes[fila][columna]

def get_pos(x, y):
    fila = y // 100
    columna = x // 100
    return matriz_posiciones[fila][columna],columna,fila

def set_pieza(x, y, pieza):
    fila = y // 100
    columna = x // 100
    imagenes[fila][columna] = pieza
    
def cambiar_turno():
    global turno_actual
    if turno_actual == 'blanco':
        turno_actual = 'negro'
    else:
        turno_actual = 'blanco'

def mover_pieza(x0, y0, xf, yf):
    global turno_actual
    pieza = imagenes[y0][x0]
    
    # Asegurarse de que la pieza seleccionada coincida con el turno actual
    if (turno_actual == 'blanco' and pieza in Equipo_blanco) or \
       (turno_actual == 'negro' and pieza in Equipo_negro):
       
        movimiento_valido = False

        # Supongamos que tienes funciones como mover_peon, mover_torre, etc.
        if 'PB' in pieza:
            movimiento_valido = mov_peon_b(x0, y0, xf, yf)
        elif 'PN' in pieza:
            movimiento_valido = mov_peon_n(x0, y0, xf, yf)
        if 'CB' in pieza:
            movimiento_valido = mov_caballo_b(x0, y0, xf, yf)
        elif 'CN' in pieza:
            movimiento_valido = mov_caballo_n(x0, y0, xf, yf)
        if 'RB' in pieza:
            movimiento_valido = mov_rey_b(x0, y0, xf, yf)
        elif 'RN' in pieza:
            movimiento_valido = mov_rey_n(x0, y0, xf, yf)
        if 'QB' in pieza:
            movimiento_valido = mov_reina_b(x0, y0, xf, yf)
        elif 'QN' in pieza:
            movimiento_valido = mov_reina_n(x0, y0, xf, yf)
        if 'AB' in pieza:
            movimiento_valido = mov_alfil_b(x0, y0, xf, yf)
        elif 'AN' in pieza:
            movimiento_valido = mov_alfil_n(x0, y0, xf, yf)
        if 'TB' in pieza:
            movimiento_valido = mov_torre_b(x0, y0, xf, yf)
        elif 'TN' in pieza:
            movimiento_valido = mov_torre_n(x0, y0, xf, yf)
        

        
        if movimiento_valido:
            # Realiza el movimiento y actualiza el tablero aquí
            
            # Cambia el turno después de un movimiento exitoso
            cambiar_turno()
            imagenes[y0][x0]=''
            return movimiento_valido
        else:
            print("Movimiento inválido.")
    else:
        print(f"Es el turno del equipo {turno_actual}, por favor selecciona una pieza del equipo {turno_actual}.")


# Límites de movimientos:
def mov_torre_b(x0, y0, xf, yf):
    # Verificar si el movimiento es en línea recta horizontal o vertical
    if x0 == xf or y0 == yf:
        # Determinar la dirección del movimiento
        if x0 == xf:  # Movimiento vertical
            mov=y0-yf
            if mov<0: #mov negativo
                #print("Abajo")
                for y in range(y0+1,y0+(mov*-1)): #me detengo uno antes del final
                    print(x0,y,imagenes[y][x0])
                    if imagenes[y][x0]!='': #si encuentra una pieza,  no se mueve
                        return False
                print(imagenes[yf][x0])
                print(imagenes[yf][x0] in Equipo_blanco)
                if imagenes[yf][x0] in Equipo_negro:
                    return True
                if imagenes[yf][x0]!='': #si encuentra pieza aliada, no se mueve
                    return False #en y-1 le doy el último
                return True #equivalente a else
            else: #mov positivo
                #print("Arriba")
                for y in range(y0-1,y0+mov*-1,-1): #me detengo uno antes del final
                    print(x0,y)
                    if imagenes[y][x0]!='': #si encuentra una pieza,  no se mueve
                        return False
                print(imagenes[yf][x0])
                if imagenes[yf][x0] in Equipo_negro:
                    return True
                if imagenes[yf][x0]!='': #si encuentra pieza aliada, no se mueve
                    return False #en y-1 le doy el último
                return True #equivalente a else
        else:  # Movimiento vertical
            mov=x0-xf
            if mov<0: #mov negativo
                #print("Derecha")
                for x in range(x0+1,x0+(mov*-1)): #me detengo uno antes del final
                    print(y0,x,imagenes[y0][x])
                    if imagenes[y0][x]!='': #si encuentra una pieza,  no se mueve
                        return False
                if imagenes[yf][xf] in Equipo_negro:
                    return True
                if imagenes[yf][xf]!='': #si encuentra pieza aliada, no se mueve
                    return False #en y-1 le doy el último
                return True #equivalente a else
            else: #mov positivo
                for x in range(x0-1,x0+mov*-1,-1): #me detengo uno antes del final
                    print(x,y0)
                    if imagenes[y0][x]!='': #si encuentra una pieza,  no se mueve
                        return False
                if imagenes[yf][xf] in Equipo_negro:
                    return True
                if imagenes[yf][xf]!='': #si encuentra pieza aliada, no se mueve
                    return False #en y-1 le doy el último
                return True #equivalente a else
    else:
        return False

def mov_torre_n(x0, y0, xf, yf):
    # Verificar si el movimiento es en línea recta horizontal o vertical
    if x0 == xf or y0 == yf:
        # Determinar la dirección del movimiento
        if x0 == xf:  # Movimiento vertical
            mov=y0-yf
            if mov<0: #mov negativo
                #print("Abajo")
                for y in range(y0+1,y0+(mov*-1)): #me detengo uno antes del final
                    print(x0,y,imagenes[y][x0])
                    if imagenes[y][x0]!='': #si encuentra una pieza,  no se mueve
                        return False
                print(imagenes[yf][x0])
                print(imagenes[yf][x0] in Equipo_negro)
                if imagenes[yf][x0] in Equipo_blanco:
                    return True
                if imagenes[yf][x0]!='': #si encuentra pieza aliada, no se mueve
                    return False #en y-1 le doy el último
                return True #equivalente a else
            else: #mov positivo
                #print("Arriba")
                for y in range(y0-1,y0+mov*-1,-1): #me detengo uno antes del final
                    print(x0,y)
                    if imagenes[y][x0]!='': #si encuentra una pieza,  no se mueve
                        return False
                print(imagenes[yf][x0])
                if imagenes[yf][x0] in Equipo_blanco:
                    return True
                if imagenes[yf][x0]!='': #si encuentra pieza aliada, no se mueve
                    return False #en y-1 le doy el último
                return True #equivalente a else
        else:  # Movimiento vertical
            mov=x0-xf
            if mov<0: #mov negativo
                #print("Derecha")
                for x in range(x0+1,x0+(mov*-1)): #me detengo uno antes del final
                    print(y0,x,imagenes[y0][x])
                    if imagenes[y0][x]!='': #si encuentra una pieza,  no se mueve
                        return False
                if imagenes[yf][xf] in Equipo_blanco:
                    return True
                if imagenes[yf][xf]!='': #si encuentra pieza aliada, no se mueve
                    return False #en y-1 le doy el último
                return True #equivalente a else
            else: #mov positivo
                for x in range(x0-1,x0+mov*-1,-1): #me detengo uno antes del final
                    print(x,y0)
                    if imagenes[y0][x]!='': #si encuentra una pieza,  no se mueve
                        return False
                if imagenes[yf][xf] in Equipo_blanco:
                    return True
                if imagenes[yf][xf]!='': #si encuentra pieza aliada, no se mueve
                    return False #en y-1 le doy el último
                return True #equivalente a else
    else:
        return False
    
def mov_caballo_b(x0, y0, xf, yf):
    # Verificar si el movimiento es en línea recta horizontal o vertical
    if ((abs(xf-x0))==1 and (abs(yf-y0))==2) or (abs((xf-x0))==2 and (abs(yf-y0))==1):
        # Determinar la dirección del movimiento
        print(imagenes[yf][xf])
        if imagenes[yf][xf] in Equipo_blanco:  # Movimiento vertical
            return False
        return True
    return False

def mov_caballo_n(x0, y0, xf, yf):
    # Verificar si el movimiento es en línea recta horizontal o vertical
    if ((abs(xf-x0))==1 and (abs(yf-y0))==2) or (abs((xf-x0))==2 and (abs(yf-y0))==1):
        # Determinar la dirección del movimiento
        print(imagenes[yf][xf])
        if imagenes[yf][xf] in Equipo_negro:  # Movimiento vertical
            return False
        return True
    return False

def mov_peon_b(x0, y0, xf, yf):
    if x0 == xf:
        if y0 - 1 == yf and imagenes[yf][xf] == '':
            return True
        elif y0 == 6 and yf == y0 - 2 and imagenes[yf][xf] == '' and imagenes[y0-1][xf] == '':
            return True
    elif abs(xf - x0) == 1 and yf == y0 - 1:
        if imagenes[yf][xf] in Equipo_negro:
            return True
    return False


def mov_peon_n(x0, y0, xf, yf):
    if x0 == xf:
        if y0 + 1 == yf and imagenes[yf][xf] == '':
            return True
        elif y0 == 1 and yf == y0 + 2 and imagenes[yf][xf] == '' and imagenes[y0+1][xf] == '':
            return True
    elif abs(xf - x0) == 1 and yf == y0 + 1:
        if imagenes[yf][xf] in Equipo_blanco:
            return True
    return False


def mov_alfil_n(x0, y0, xf, yf):
    if abs(xf - x0) == abs(yf - y0):
        if xf > x0:
            dir_x = 1
        else:
            dir_x = -1
        if yf > y0:
            dir_y = 1
        else:
            dir_y = -1
        steps = abs(xf - x0)
        for i in range(1, steps):
            x = x0 + dir_x * i
            y = y0 + dir_y * i
            if imagenes[y][x] != '':
                return False
        if imagenes[yf][xf] == '' or imagenes[yf][xf] in Equipo_blanco:
            return True
    return False

def mov_alfil_b(x0, y0, xf, yf):
    if abs(xf - x0) == abs(yf - y0):
        if xf > x0:
            dir_x = 1
        else:
            dir_x = -1
        if yf > y0:
            dir_y = 1
        else:
            dir_y = -1
        steps = abs(xf - x0)
        for i in range(1, steps):
            x = x0 + dir_x * i
            y = y0 + dir_y * i
            if imagenes[y][x] != '':
                return False
        if imagenes[yf][xf] == '' or imagenes[yf][xf] in Equipo_negro:
            return True
    return False 

def mov_rey_n(x0, y0, xf, yf):
    if max(abs(xf - x0), abs(yf - y0)) == 1:
        if imagenes[yf][xf] == '' or imagenes[yf][xf] in Equipo_blanco:
            return True
    return False

def mov_rey_b(x0, y0, xf, yf):
    if max(abs(xf - x0), abs(yf - y0)) == 1:
        if imagenes[yf][xf] == '' or imagenes[yf][xf] in Equipo_negro:
            return True
    return False

def mov_reina_n(x0, y0, xf, yf):
    if mov_torre_n(x0, y0, xf, yf) or mov_alfil_n(x0, y0, xf, yf):
        return True
    return False

def mov_reina_b(x0, y0, xf, yf):
    if mov_torre_b(x0, y0, xf, yf) or mov_alfil_b(x0, y0, xf, yf):
        return True
    return False

def inicio(screen):
    clock = time.Clock()
    inicio = image.load("assets/images/Inicio.png")
    inicio = transform.scale(inicio, (800, 800))
    start = image.load("assets/images/start.png")
    start = transform.scale(start, (200, 150))
    
    start_rect = start.get_rect(topleft=(300, 450))  # Obtener rectángulo de la imagen "start"
    
    while True:
        for e in event.get():
            if e.type == QUIT: 
                quit()
                sys.exit()
            elif e.type == MOUSEBUTTONDOWN:  # Detectar clic del mouse
                if start_rect.collidepoint(e.pos):  # Verificar si el clic fue dentro del rectángulo
                    return 2
                
        screen.blit(inicio, (0, 0))
        screen.blit(start, (300, 450))
        display.flip()
        clock.tick(60)
    
def tablero(screen):
    xi, yi = 20, 15
    xp, yp = 20, 15
    xa, ya = xi, yi
    x0,y0,xf,yf=0,0,0,0
    pos=0
    move = False
    seleccionado = False
    moving = False
    clock = time.Clock()
    fondo = image.load("assets/images/Tablero_imagen.jpg")
    fondo = transform.scale(fondo, (800, 800))
    
    TN = transform.scale(image.load("assets/images/Torre_negra.png"), (60, 75))
    TB = transform.scale(image.load("assets/images/Torre_blanca.png"), (60, 75))
    PB = transform.scale(image.load("assets/images/Peón_blanco.png"), (60, 75))
    PN = transform.scale(image.load("assets/images/Peón_negro.png"), (60, 75))
    RN = transform.scale(image.load("assets/images/Rey_negro.png"), (60, 75))
    RB = transform.scale(image.load("assets/images/Rey_blanco.png"), (60, 75))
    CB = transform.scale(image.load("assets/images/Caballo_blanco.png"), (60, 75))
    CN = transform.scale(image.load("assets/images/Caballo_negro.png"), (60, 75))
    AN = transform.scale(image.load("assets/images/Alfil_negro.png"), (60, 75))
    AB = transform.scale(image.load("assets/images/Alfil_blanco.png"), (60, 75))
    QB = transform.scale(image.load("assets/images/Reina_blanca.png"), (60, 75))
    QN = transform.scale(image.load("assets/images/Reina_negra.png"), (60, 75))
    
    while True:
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if not seleccionado and not move:
                    xa, ya = mouse.get_pos()
                    pieza = get_pieza(xa, ya)
                    pos, x0, y0 = get_pos(xa, ya)
                    xa, ya = pos
                    if not(pieza == "") :
                        seleccionado = True
                        print(xa,ya,x0,y0)
                elif not move:
                    xp, yp = mouse.get_pos()
                    pos, xf, yf = get_pos(xp, yp)
                    xp, yp = pos
                    print(xp,yp,xf,yf)
                    seleccionado = False
                    #Comprobar movimiento por pieza
                    moving = mover_pieza(x0,y0,xf,yf)
                    """
                    if pieza=='TB':
                        if mov_torre_b(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='TN':
                        if mov_torre_n(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='CB':
                        if mov_caballo_b(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='CN':
                        if mov_caballo_n(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='PB':
                        if mov_peon_b(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='PN':
                        if mov_peon_n(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='AN':
                        if mov_alfil_n(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='AB':
                        if mov_alfil_b(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='RN':
                        if mov_rey_n(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='RB':
                        if mov_rey_b(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='QN':
                        if mov_reina_n(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    if pieza=='QB':
                        if mov_reina_b(x0,y0,xf,yf):
                            moving = True
                            imagenes[y0][x0]=''
                    """
        
        sonido_reproducido = False
        
        if moving:
            if(not move):
                mvx = (xp//100*100+xi - xa)/100
                mvy = (yp//100*100+yi - ya)/100
                
            if((int(xa) > xp//100*100+xi-2) or (int(xa) < xp//100*100+xi+2)):
                move = True
                xa+=mvx
            if((int(ya) > yp//100*100+yi-2) or (int(ya) < yp//100*100+yi+2)):
                move = True
                ya+=mvy
            if(int(xa) == xp//100*100+xi and int(ya) == yp//100*100+yi):
                move = False
                moving = False
                imagenes[yf][xf]=pieza
                if not sonido_reproducido:  # Añadir esta condición
                    comer.play()
                    sonido_reproducido = True
        
            
        screen.fill((255, 255, 255))
        screen.blit(fondo, (0, 0))
                        
        for i in range(8):
            for j in range(8):
                if imagenes[i][j] == 'TB':
                    screen.blit(TB, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'TN':
                    screen.blit(TN, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'PB':
                    screen.blit(PB, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'PN':
                    screen.blit(PN, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'RN':
                    screen.blit(RN, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'RB':
                    screen.blit(RB, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'CB':
                    screen.blit(CB, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'CN':
                    screen.blit(CN, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'AN':
                    screen.blit(AN, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'AB':
                    screen.blit(AB, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'QB':
                    screen.blit(QB, matriz_posiciones[i][j])
                elif imagenes[i][j] == 'QN':
                    screen.blit(QN, matriz_posiciones[i][j])
                    
        if(move):
            if pieza == 'TB':
                screen.blit(TB, (xa,ya))
            elif pieza == 'TN':
                screen.blit(TN, (xa,ya))
            elif pieza == 'PB':
                screen.blit(PB, (xa,ya))
            elif pieza == 'PN':
                screen.blit(PN, (xa,ya))
            elif pieza == 'RN':
                screen.blit(RN, (xa,ya))
            elif pieza == 'RB':
                screen.blit(RB, (xa,ya))
            elif pieza == 'CB':
                screen.blit(CB, (xa,ya))
            elif pieza == 'CN':
                screen.blit(CN, (xa,ya))
            elif pieza == 'AN':
                screen.blit(AN, (xa,ya))
            elif pieza == 'AB':
                screen.blit(AB, (xa,ya))
            elif pieza == 'QB':
                screen.blit(QB, (xa,ya))
            elif pieza == 'QN':
                screen.blit(QN, (xa,ya))
        
        display.flip()
        clock.tick(60)
        
        end1=True
        end2=True
        for x in range (len(imagenes)):
            for y in range (len(imagenes[x])):
                if(imagenes[x][y] == "RB"):
                    end1 = False
                if imagenes[x][y] == "RN":
                    end2 = False
        if moving:
            end1=False
            end2=False
        if end1:
            clock.tick(60)
            comer.play()
            return 3
        if end2:
            clock.tick(60)
            comer.play()
            return 4
        
def gana_negro(screen):
    clock = time.Clock()
    V_negro=image.load("assets/images/V_negro.png")
    V_negro=transform.scale(V_negro,(800,800))
    while True:
        for e in event.get():
            if e.type == QUIT: sys.exit()
        screen.blit(V_negro,(0,0))
        display.flip()
        clock.tick(60)
        
def gana_blanco(screen):
    clock = time.Clock()
    V_blanco=image.load("assets/images/V_blanco.png")
    V_blanco=transform.scale(V_blanco,(800,800))
    while True:
        for e in event.get():
            if e.type == QUIT: sys.exit()
        screen.blit(V_blanco,(0,0))
        display.flip()
        clock.tick(60)


escena = 1
epic.play()
while True:
    for ev in event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()
    if escena == 1:
        escena = inicio(screen)
    elif escena == 2:
        epic.stop()
        cancion.play()
        escena = tablero(screen)
    elif escena == 3:
        cancion.stop()
        epic.play()
        escena = gana_negro(screen)
    elif escena == 4:
        cancion.stop()
        epic.play()
        escena = gana_blanco(screen)
