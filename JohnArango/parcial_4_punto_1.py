class Figura:
    """Clase base para figuras geométricas"""
    def calcular_area(self):
        """Método base que debe ser sobrescrito por las clases hijas"""
        return 0

class Rectangulo(Figura):
    """Clase para calcular el área de un rectángulo"""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área de un rectángulo: base * altura"""
        return self.base * self.altura

class Triangulo(Figura):
    """Clase para calcular el área de un triángulo"""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área de un triángulo: 0.5 * base * altura"""
        return 0.5 * self.base * self.altura

def main():
    print("Figuras Geométricas")

    # Crear y calcular área de un rectángulo
    print("\nRectángulo")
    base_rectangulo = float(input("Introduce la base del rectángulo: "))
    altura_rectangulo = float(input("Introduce la altura del rectángulo: "))
    rectangulo = Rectangulo(base_rectangulo, altura_rectangulo)
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")

    # Crear y calcular área de un triángulo
    print("\nTriángulo")
    base_triangulo = float(input("Introduce la base del triángulo: "))
    altura_triangulo = float(input("Introduce la altura del triángulo: "))
    triangulo = Triangulo(base_triangulo, altura_triangulo)
    print(f"El área del triángulo es: {triangulo.calcular_area()}")


main()