class vehiculo():
    def __init__(self,marca,modelo):
        self._marca = marca
        self._modelo = modelo
        self._enMarcha = False
        self._acelera = False
        self._frenos = False

    def arrancar(self):
        self._enMarcha = True
    def acelerar(self):
        self._acelera = True
    def frenar(self):
        self._frenos = True
    def estado(self):
        print(f"marca: {self._marca} \nModelo: {self._modelo} \nEn marcha: {self._enMarcha} \nAcelerando: {self._acelera} \nFrenando: {self._frenos}")

class  moto(vehiculo):
    hcaballitos = ""
    ruedas = 3

    def caballitos(self):
        self.hcaballitos = "voy haciendo caballitos"
    def estado(self):
        super().estado()
        print(self.hcaballitos)

micoche = vehiculo("ford","fiesta")
micoche.estado()

print("----------------------")

mimoto = moto("HONDA","CBR")
mimoto.caballitos()
mimoto.estado()
#el "__" sirve para dejar en una sola clase los parametros dados, o los "self" dados