import pygame
class Input(object):
    def __init__(self):
        self.keyDownList = []
        self.keyPressedList = []
        self.keyUpList = []
        # has the user quit the application?
        self.quit = False

    def update(self):
        self.keyDownList = []
        self.keyUpList = []

        # iterate over all user input events (such as keyboard or mouse)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                self.keyDownList.append(keyName)
                self.keyPressedList.append(keyName)
            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.keyPressedList.remove(keyName)
                self.keyUpList.append(keyName)
        # that occurred since the last time events were checked
            if event.type == pygame.QUIT:
                self.quit = True

#Esta funcion toma el parametro keyCode y lo verifica si esta presente
#en keyDownList, si esta presente la tecla correspondiente se mantiene
# presionada actualmente y el método devuelve True. De lo contrario, devuelve False
    def isKeyDown(self, keyCode):
        return keyCode in self.keyDownList
#Se define un metodo isKeyPressed donde toma el parametro keyCode y se
#verifica si esta prsente en keyPressedList, KeyPressedList es
#una lista de teclas que se han presionado desde la última vez que se llamó a este método,
#mantenida por el objeto que contiene este método.
    def isKeyPressed(self, keyCode):
        return keyCode in self.keyPressedList
#Al igual que lo anterior define un método llamado isKeyUp que toma
#un parámetro keyCode y verifica si está presente en keyUpList.
#keyUpList es la lista de claves que se han registrado desde la última vez
#que se llamó a este método, mantenida por el objeto que contiene este método.
#Si se encuentra keyCode en keyUpList, entonces la clave correspondiente
#se ha liberado desde la última vez que se llamó a isKeyUp y el método devuelve True.
#De lo contrario, devuelve False.
    def isKeyUp(self, keyCode):
        return keyCode in self.keyUpList 