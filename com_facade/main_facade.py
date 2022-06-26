from facade import Facade

class Celular:
    def __init__(self,modelo,marca):
        self.modelo = modelo
        self.marca = marca
        self.celular = Facade()

    def getInfo(self):

        if self.marca == 'Motorola':
            print(f"Modelo: {self.modelo}")
            print(f"Marca: {self.marca}")
            self.celular.getMotorola()

        elif self.marca == 'Apple':
            print(f"Modelo: {self.modelo}")
            print(f"Marca: {self.marca}")
            self.celular.getApple()

        if self.marca == 'Nokia':
            print(f"Modelo: {self.modelo}")
            print(f"Marca: {self.marca}")
            self.celular.getNokia()


