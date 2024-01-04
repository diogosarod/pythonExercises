def sum(a, b, c, d):
    soma = a + b + c + d
    print(f"A soma de todos os valores é: {soma}")

def main():
    valores = []

    for i in range(4):
        valores.append(int(input(f"Digite o {i+1}º número: ")))

    sum(*valores)

if __name__ == "__main__":
    main()
