class Carro:
    def __init__(self):
        self.passageiros = 0
        self.combustivel = 0
        self.quilometragem = 0

    def get_Passageiros(self):
        return self.passageiros

    def get_Combustivel(self):
        return self.combustivel

    def get_Quilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros < 2:
            self.passageiros += 1
            return True
        else:
            return False

    def desembarcar(self):
        if self.passageiros > 0:
            self.passageiros -= 1
            return True
        else:
            return False

    def dirigir(self, distancia: int):
        if self.passageiros == 0 or self.combustivel == 0:
            return False

        else:
            if self.combustivel - distancia < 0:
                self.quilometragem += self.combustivel
                self.combustivel = 0
                return False

            else:
                self.combustivel -= distancia
                self.quilometragem += distancia
                return True

    def abastecer(self, quantidade):
        if quantidade > 0:
            self.combustivel = self.combustivel + quantidade
        if self.combustivel > 100:
            self.combustivel = 100
            return True
        else:
            return False
