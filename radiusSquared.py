def calc(raio):
 area = 3.14 * raio ** 2
 return area

raio = float(input("Digite o raio do círculo: "))
area = calc(raio)
print(f"A área do círculo é: {area:.3f}")
