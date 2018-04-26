# importar modulos necesarios
import  objetoSprite


class Bola(objetoSprite.ObjetoSprite):
    def __init__(x,y,rutaImagen):
        objetoSprite.ObjetoSprite.__init__(self,x,y,rutaImagen)
        
