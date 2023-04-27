from core.base import Base

class Test(Base):
    def initialize(self):
        print("Initializing program...")

    def update(self):
        #Dentro del método, verifica si la tecla "espacio" se mantiene presionada
        # actualmente usando el método isKeyDown del objeto de entrada.
        if self.input.isKeyDown("space"):
            print("The 'space' key was just pressed down.")
        #el código comprueba si se ha pulsado la tecla "derecha" desde el último fotograma,
        # utilizando el método isKeyPressed del objeto de entrada.
        if self.input.isKeyPressed("right"):
            print("The 'right' key is currently beingpressed.")
            #if len(self.input.keyDownList) > 0:
         #   print("Keys down:", self.input.keyDownList)
        #if len(self.input.keyPressedList) > 0:
         #   print("Keys pressed:", self.input.keyPressedList)
        #if len(self.input.keyUpList) > 0:
         #   print("Keys up:", self.input.keyUpList)
Test().run()
