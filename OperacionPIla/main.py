import ventana, mono, bola, volmeter

w1 = ventana.Ventana(800,700, "hola")

v1 = volmeter.Volmeter(650,400,"Images/volmeter.png")
o1 = bola.Bola.crear_Objetos(35,105,6,"Images/blueBall.png")
o2 = bola.Bola.crear_Objetos(35,530,6,"Images/redBall.png")
o3 = mono.Mono.crear_Objetos(35,380,1,"Images/monoRojo.png",)



w1.ejecutar_Principal(o1,o2,o3,v1)
