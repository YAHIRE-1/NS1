#Suma de Cuadrados y Cubos
class Indice():


    def __init__(self,numero):
        
        self.numero = list(str(numero))
        self.cuadrado = []
        self.cubo = []
        self.entrada = True
        self.suma = 0

        
        i = 0
        while i < len(self.numero):
            self.numero[i] = int(self.numero[i])
            i += 1

   
    def potencia(self,numero):
        if(self.entrada):
            for i in self.numero:
                pot = i ** 2
                i += 1
                self.cuadrado.append(pot)
            return self.cuadrado
        elif(self.entrada == False):
             for i in self.numero:
                    pot = i ** 3
                    i += 1
                    self.cubo.append(pot)
             return self.cubo

class Sumadecuadrados(Indice):


    def __init__(self,numero):
        self.cuadrado = numero
        self.suma = 0

    def sumacuadrados(self,numero):
        for i in self.cuadrado:
            self.suma = self.suma + i
        return self.suma

class Sumadecubos(Indice):


    def __init__(self,numero):
        self.cubo = numero
        self.suma = 0

    def sumacubos(self,numero):
        for i in self.cubo:
            self.suma= self.suma + i
        return self.suma

print('Programa que suma el cuadrado y el cubo de una cadena de numeros')
numero = int(input("Ingresa el numero que quieres calcular: "))

bloque1 = Indice(numero)
alcuadrado = bloque1.potencia(numero)
bloque1.entrada = False
alcubo = bloque1.potencia(numero)
bloque2 = Sumadecuadrados(alcuadrado)
sumacuadrados = bloque2.sumacuadrados(alcuadrado)
bloque3 = Sumadecubos(alcubo)
sumacubos = bloque3.sumacubos(alcubo)

print(f"El resultado de la suma de los cubos y cuadrados es:\n{sumacuadrados+sumacubos}")