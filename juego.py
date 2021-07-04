import pygame
import time
import numpy as np
windows=pygame

pygame.init()
pantalla=pygame.display.set_mode((800,475))



Blanco=(255,255,255)
Rojo=(0,0,255)
Amarillo=(255,255,0)
Azul=(0,255,0)

TrikiTriki=np.zeros((3,3))





def inicio():
    presentar=pygame.image.load("parte3\Triki-Triki\Imagenes/Inicio.png")
    pantalla.blit(presentar,(0,0))
    pygame.display.update()
    time.sleep(5)

def menu():
    menu=pygame.image.load("parte3/Triki-Triki/Imagenes/Menu.png")
    pantalla.blit(menu,(0,0))
    pygame.display.update()
    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                x,y= eventos.pos
                print(x," ",y," ")
                if (x>=84 and y>= 131 and x<=351 and y<=188):
                        print("jugar")
                        jugar("x")
                if (x>=84 and y>= 207 and x<=351 and y<=263):
                    print("help me")
                if (x>=84 and y>= 281 and x<=351 and y<=338):
                    print("about")
                if (x>=84 and y>= 356 and x<=351 and y<=414):
                    print("quit")
                    exit()
        pantalla.blit(menu,(0,0))
        pygame.display.update()

#inicio()

def jugar(turno):
    jugar=pygame.image.load("parte3\Triki-Triki\Imagenes/Game.png")
    pantalla.blit(jugar,(0,0))
    pygame.display.update() 
    while(True):
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                TrikiTriki[:,:]=0
                menu()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                x,y= eventos.pos
                print(x," ",y," ")    
                if (x >= 255 and y >=93 and x<=337 and y<=172):
                   turno= marcar([255,90],turno,[0,0])
                if (x>=361 and y>=90 and x<=443 and y<=169):
                    turno= marcar([361,90],turno,[0,1])
                if (x>=468 and y>=90 and x<=553 and y<=174):
                    turno= marcar([468,90],turno,[0,2])
                if (x>=257 and y>=188 and x<=339 and y<=264):
                    turno= marcar([257,188],turno,[1,0])
                if (x>=355 and y>=188 and x<=453 and y<=264):
                    turno= marcar([355,188],turno,[1,1])
                if (x>=466 and y>=188 and x<=552 and y<=264):
                    turno= marcar([466,188],turno,[1,2])
                if (x>=257 and y>=281 and x<=339 and y<=361):
                    turno= marcar([257,281],turno,[2,0])
                if (x>=358 and y>=287 and x<=439 and y<=363):
                    turno= marcar([358,287],turno,[2,1])
                if (x>=470 and y>=284 and x<=550 and y<=359):
                    turno= marcar([470,284],turno,[2,2]) 
                validarJuego()

def marcar(ini,turno,pos):
    if(TrikiTriki[pos[0]][pos[1]]==0):
        if(turno == "x"):
            TrikiTriki[pos[0]][pos[1]]=1
            print(TrikiTriki)
            marca=pygame.image.load("parte3\Triki-Triki\Imagenes/equis.png")
            turno="o"
        elif(turno=="o"):
            TrikiTriki[pos[0]][pos[1]]=2
            print(TrikiTriki)
            marca=pygame.image.load("parte3\Triki-Triki\Imagenes/circulo.png")
            turno="x"
        pantalla.blit(marca,(ini[0],ini[1]))
        pygame.display.update()
        return turno
    else:
         print("ya tiene una marca dibujada")
    return turno      
def validarJuego():
    cruzIzquierda=0
    Lado=0
    for i in range(3):
        if(TrikiTriki[i][i]>0):
            cruzIzquierda+=1
        if(cruzIzquierda==3):
            print("gano")
            cruzIzquierda=0
            TrikiTriki[:,:]=0
    
    for j in range (3):
        if(TrikiTriki[0][j]==1):
            Lado+=1
            print("x= ",Lado)
        elif(TrikiTriki[1][j]==1):
            Lado+=1 
            print("x= ",Lado)
        elif(TrikiTriki[2][j]==1):
            Lado+=1    
            print("x= ",Lado)
    if(Lado==3):
            print("gano")
            Lado=0
              
    
menu()
jugar("x")
#validarJuego()

