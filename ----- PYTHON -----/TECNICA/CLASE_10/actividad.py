class padre():
    def __init__(self, ojos,_forma_cara, altura):
        self._ojos = ojos
        self._forma_cara = _forma_cara
        self._altura = altura
        if self._altura <= 0:
            self._altura = 1.60
    def presentar_rasgos(self):
        print(f"color de los ojos: {self._ojos}\nforma de la cara: {self._forma_cara}\naltura: {self._altura}")

class hija(padre):
    htalento = ""
    def estado(self):
        print(self._ojos)
    def talento(self):
        self.htalento = "tocar el piano"
    def presentar_rasgos(self):
        super().presentar_rasgos()
        print(self.htalento)

mipadre = padre("azules", "ovalada" , 1.70)
mipadre.presentar_rasgos()

print("----------------------")

persona_hija = hija("azules", "ovalada" , -5)
persona_hija.talento()
persona_hija.presentar_rasgos()
