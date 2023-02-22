#Fórmula de Bhaskara
import math
print("Calcule a equação de segundo grau: (ax² + bx + c = 0)")
while True:
  try:
    a = float(input("Qual o valor de a? "))
    b = float(input("Qual o valor de b? "))
    c = float(input("Qual o valor de c? "))
    delta = (b ** 2) - (4 * a * c)
    if isinstance(a, float) and isinstance(b, float) and isinstance (c, float):
      break
  except ValueError:
    print("Por favor, digite um número válido!")

if a == 0:
  print("\na não pode ser igual à zero!!")
elif delta < 0:
  print("\nEsta equação não possui raízes reais!")
elif delta == 0:
  x = (- b + math.sqrt(delta)) / (2 * a)
  print(f"\nA única raíz real é {x}")
else:
  x1 = (- b + math.sqrt(delta)) / (2 * a)
  x2 = (- b - math.sqrt(delta)) / (2 * a)
  print(f"\nExistem duas raízes reais: \nA primeira raíz é = {x1}.\nA segunda raíz é = {x2}.")

#print(f"\nO valor de delta é {delta}")