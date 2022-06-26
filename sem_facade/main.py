from nokia import Nokia
from apple import Apple
from motorola import Motorola

class Celular:
    def __init__(self,modelo,marca):
        self.modelo = modelo
        self.marca = marca
        self.motorola = Motorola()
        self.apple = Apple()
        self.nokia = Nokia()

    def getInfo(self):

        if self.marca == 'Motorola':
            print(f"Modelo: {self.modelo}")
            print(f"Marca: {self.marca}")
            self.motorola.getFabricacao()
            self.motorola.getLoja()
        elif self.marca == 'Apple':
            print(f"Modelo: {self.modelo}")
            print(f"Marca: {self.marca}")
            self.apple.getFabricacao()
            self.apple.getLoja()
        if self.marca == 'Nokia':
            print(f"Modelo: {self.modelo}")
            print(f"Marca: {self.marca}")
            self.nokia.getFabricacao()
            self.nokia.getLoja()
        else:
            print("Marca não cadastrada")
