# importar modulos necesarios 
import pygame, sys
from pygame.locals import *

# heredar constructor y sobrecargarlo
class Ventana: 

    # fijar dims de ventanas y fijar titulo
    def __init__(self,ancho, alto,titulo):
        pygame.init()
        self.pantalla =  pygame.display.set_mode( (ancho, alto) )
        pygame.display.set_caption(titulo)
        self.clock = pygame.time.Clock()
    

    # fijar imagen de fondo 
    def cargar_Fondo (self,rutaImagen):
        self.imagenFondo = pygame.image.load(rutaImagen)
        self.imagenFondo = self.imagenFondo.convert()
        ##color = self.imagenFondo.get_at( (0,0) )
        ##self.imagenFondo.set_colorkey(color,RLEACCEL)
        self.pantalla.blit(self.imagenFondo, (0,0))

    # ciclo principal
    def ejecutar_Principal (self, coleccionBolasSup, coleccionBolasInf, coleccionMonos, volmeter):
        while True:
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                    sys.exit(0)
            tiempo = self.clock.tick(60)
            
            self.actualizar_OcilacionObjetos(coleccionBolasSup,tiempo,120, 270)
            self.actualizar_OcilacionObjetos(coleccionBolasInf,tiempo,550, 690)
            self.actualizar_OcilacionObjetos(coleccionMonos,tiempo,350,420)
            #self.cargar_Fondo('/home/frodo/Documentos/PyGames/fondo.jpg')
            self.cargar_Fondo('/home/frodo/Documentos/PyGames/OperacionPIla/Images/PilaVect.png')
            self.insertar_Objetos(coleccionBolasSup)
            self.insertar_Objetos(coleccionBolasInf)
            self.insertar_Objetos(coleccionMonos)
            self.insertar_Objeto(volmeter)
            pygame.display.flip()

    # conseguir la pantalla principal
    def conseguir_Instancia(self):
        return self.pantalla
        
    # insertar un objeto en la ventana
    def insertar_Objeto(self, objetoNuevo):
        self.pantalla.blit(objetoNuevo.imagenFondo, objetoNuevo.rectangulo_Pos)

     # insertar una coleccion de objetos en la ventana
    def insertar_Objetos(self,coleccionObejtos):
        for objetoNuevo in coleccionObejtos:
            self.pantalla.blit(objetoNuevo.imagenFondo, objetoNuevo.rectangulo_Pos)

    def actualizar_OcilacionObjetos(self, coleccion, tiempo,yTop, yBot):
        for bol in coleccion:
            bol.ocilar_Objeto(tiempo, yTop, yBot)
            