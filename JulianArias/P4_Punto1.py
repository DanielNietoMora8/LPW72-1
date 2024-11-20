class Figura:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
      
    def calcular_area(self):
        return 0
    
#---------------------------------------------------
    
class Rectangulo(Figura):
   
   '''
   def __init__(self):
      pass'''

   
   def calcular_area(self):
      return (self.base)*(self.altura)
   
#---------------------------------------------------
   
class Triangulo(Figura):
   
   '''
   def __init__(self):
      pass
      '''
   
   def calcular_area(self):
      return (0.5)*(self.base)*(self.altura)


   
#---------------------------------------------------
   
def funcPrincipal():

   baseR = float(input("Ingrese base del rectangulo: "))
   alturaR = float(input("Ingrese altura del rectangulo: "))
   print("")
   baseT = float(input("Ingrese base del triangulo: "))
   alturaT = float(input("Ingrese altura del triangulo: "))

   rectangulo1 = Rectangulo(baseR, alturaR)
   triangulo1 = Triangulo(baseT, alturaT)

   print("")
   print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')
   print(f'El area del triangulo es: {triangulo1.calcular_area()}')

funcPrincipal()
