# importar modulos necesarios 
import pygame, sys, random, objetoSprite
from pygame.locals import *

class Mono(objetoSprite.ObjetoSprite):
    def __init__(self,x,y,rutaImagen):
        objetoSprite.ObjetoSprite.__init__(x,y,rutaImagen)

    