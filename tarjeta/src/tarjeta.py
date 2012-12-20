import pygame
from pygame.locals import *

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 580
blanco = (217,249,244)
verde = (0,255,0)
cafe=(81,48,48)
rojo=(249,8,28)
azul=(10,2,252)
amarillo=(248,252,2)
rosa=(247,18,220)

# ------------------------------
# Funcion principal del juego
# http://sabia.tic.udc.es/gc/Contenidos%20adicionales/trabajos/ProgramacionVideoJuegos/PyGame/modules/draw/rect.html
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    pantalla =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TARJETITA")
    
    salir=False
    reloj1=pygame.time.Clock()
    tipoLetra=pygame.font.Font(None,40)
    texto1=tipoLetra.render('FELIZ NAVIDAD Y PROSPERO 2013',0,(0,0,0))
    texto2=tipoLetra.render('KEVIN CAMPUZANO',0,(0,0,0))
    # el bucle principal del juego
    while salir!=True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(20)
        pantalla.fill(blanco)
        pantalla.blit(texto1,(100,500))
        pantalla.blit(texto2,(200,550))
        pygame.draw.polygon(pantalla,verde,[(200,350),(300,50),(400,350),500])
        pygame.draw.rect(pantalla,cafe,[(290,350),(20,90)])
        pygame.draw.rect(pantalla,rojo,[(200,380),(70,50)])
        pygame.draw.rect(pantalla,amarillo,[(350,380),(70,50)])
        pygame.draw.rect(pantalla,azul,[(290,380),(70,70)])
        pygame.draw.rect(pantalla,rosa,[(250,390),(80,70)])
        pygame.draw.circle(pantalla,rojo,(210,300),9)
        pygame.draw.circle(pantalla,azul,(230,305),9)
        pygame.draw.circle(pantalla,amarillo,(250,295),9)
        pygame.draw.circle(pantalla,rojo,(270,305),9)
        pygame.draw.circle(pantalla,azul,(290,295),9)
        pygame.draw.circle(pantalla,amarillo,(310,290),9)
        pygame.draw.circle(pantalla,rojo,(330,285),9)
        pygame.draw.circle(pantalla,azul,(350,280),9)
        pygame.draw.circle(pantalla,amarillo,(370,275),9)
        pygame.draw.circle(pantalla,rojo,(360,240),9)
        pygame.draw.circle(pantalla,azul,(340,245),9)
        pygame.draw.circle(pantalla,amarillo,(320,240),9)
        pygame.draw.circle(pantalla,rojo,(300,245),9)
        pygame.draw.circle(pantalla,amarillo,(280,240),9)
        pygame.draw.circle(pantalla,azul,(260,245),9)
        pygame.draw.circle(pantalla,rojo,(240,245),9)
        pygame.draw.circle(pantalla,amarillo,(280,200),9)
        pygame.draw.circle(pantalla,azul,(260,210),9)
        pygame.draw.circle(pantalla,rojo,(280,200),9)
        pygame.draw.circle(pantalla,amarillo,(300,210),9)
        pygame.draw.circle(pantalla,azul,(320,200),9)
        pygame.draw.circle(pantalla,rojo,(340,210),9)
        pygame.draw.circle(pantalla,amarillo,(270,160),9)
        pygame.draw.circle(pantalla,azul,(290,165),9)
        pygame.draw.circle(pantalla,rojo,(310,160),9)
        pygame.draw.circle(pantalla,amarillo,(330,165),9)
        pygame.draw.circle(pantalla,azul,(320,120),9)
        pygame.draw.circle(pantalla,rojo,(300,125),9)
        pygame.draw.circle(pantalla,amarillo,(280,120),9)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
