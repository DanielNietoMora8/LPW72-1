class Figura : 
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
        return 0
    

class Rectangulo(Figura):
    

    def calcular_area(self):
        return self.base*self.altura
    

class Triangulo(Figura):
    def calcular_area(self):
        return self.base*self.altura*0.5
    
def main(): 
    print("calculo de areas de figuras geometricas")
    base = float(input("ingrese la base del rectangulo: "))
    altura = float(input("ingrese la altura del rectangulo: "))
    rectangulo = Rectangulo(base, altura)
    print(f"area del rectangulo: {rectangulo.calcular_area()}")

    base = float(input("ingrese la base del triangulo: "))
    altura = float(input("ingrese la altura del triangulo: "))
    triangulo = Triangulo(base, altura)
    print(f"area del triangulo: {triangulo.calcular_area()}")

main()