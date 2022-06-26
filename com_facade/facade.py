from nokia import Nokia
from apple import Apple
from motorola import Motorola



class Facade:
    def __init__(self):
        self.motorola = Motorola()
        self.apple = Apple()
        self.nokia = Nokia()

    def getMotorola(self):
        self.motorola.getFabricacao()
        self.motorola.getLoja()

    def getNokia(self):
        self.nokia.getFabricacao()
        self.nokia.getLoja()

    def getApple(self):
        self.apple.getFabricacao()
        self.apple.getLoja()