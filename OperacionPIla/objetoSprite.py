# importar modulos necesarios 
import pygame, sys, random
from pygame.locals import *

# heredar de la clase sprite 
class ObjetoSprite(pygame.sprite.Sprite):

    # llamar a los constructores necesarios
    def __init__(self, x,y,rutaImagen):
        pygame.sprite.Sprite.__init__(self)
        self.imagenFondo = self.cargar_Fondo(rutaImagen)
        self.rectangulo_Pos = self.imagenFondo.get_rect()
        self.rectangulo_Pos.centerx = x
        self.rectangulo_Pos.centery = y
        self.velocidad = [0.085, -0.085]

    def cargar_Fondo(self,rutaImagen):
        imagenFondo = pygame.image.load(rutaImagen)
        imagenFondo = imagenFondo.convert()
        color = imagenFondo.get_at( (0,0) )
        imagenFondo.set_colorkey(color,RLEACCEL)
        return imagenFondo

    def ocilar_Mono(self,tiempo):
        #self.rectangulo_Pos.centerx += tiempo * self.velocidad[1]
        self.rectangulo_Pos.centery += tiempo * self.velocidad[0]

        if (self.rectangulo_Pos.bottom >= 400):
            self.velocidad[0] = self.velocidad[1]
        elif (self.rectangulo_Pos.top <= 360):
            self.velocidad[0] = -self.velocidad[1]


    def ocilar_Bola(self,tiempo,yTop, yBot):
        #self.rectangulo_Pos.centerx += tiempo * self.velocidad[1]
        self.rectangulo_Pos.centery += tiempo * self.velocidad[0]

        if (self.rectangulo_Pos.bottom >= yBot):
            self.velocidad[0] = self.velocidad[1]
        elif (self.rectangulo_Pos.top <= yTop):
            self.velocidad[0] = -self.velocidad[1]


    
            
        



        

        
            


        

                


    @classmethod
    def crear_Objetos(self,xEnt, yEnt, numeroObjetos, rutaImagen):
        
        coleccionObjetos = []
        ##x = 20; y = 105
        x = xEnt; y = yEnt
        for n in range(numeroObjetos):
            x = 20; y += 25
            for numeroX in range(numeroObjetos+10):
                nuevoObjeto = ObjetoSprite(x, y,rutaImagen)
                coleccionObjetos.append(nuevoObjeto)
                x += 30
       

           
            

            #x += 50 #random.randint(0,500)
            #y += 50 #random.randint(0,700)
            
        return coleccionObjetos


