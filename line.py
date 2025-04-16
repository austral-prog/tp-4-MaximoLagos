def line():
    print("TO DO")
import math

# Ingreso de datos
A = float(input("Ingrese el coeficiente A: "))
B = float(input("Ingrese el coeficiente B: "))
X1 = float(input("Ingrese el coeficiente X1: "))
X2 = float(input("Ingrese el coeficiente X2: "))

# Mostrar los coeficientes ingresados
print("\nEl coeficiente A de su ecuación de la recta es:", A)
print("El coeficiente B de su ecuación de la recta es:", B)
print("El coeficiente X1 de su ecuación de la recta es:", X1)
print("El coeficiente X2 de su ecuación de la recta es:", X2)

# Mostrar la ecuación de la recta
print("\nPara la siguiente ecuación:")
print(f"\tY = {A}X + {B}")

# Calcular Y1 y Y2 usando la ecuación de la recta
Y1 = A * X1 + B
Y2 = A * X2 + B

# Mostrar los puntos sobre la recta
print("\nDados los siguientes puntos:")
print(f"\tP1 ({X1}, {Y1})")
print(f"\tP2 ({X2}, {Y2})")

# Calcular la distancia entre los dos puntos
distancia = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

# Mostrar la distancia
print("\nLa distancia entre ellos es:", distancia)
