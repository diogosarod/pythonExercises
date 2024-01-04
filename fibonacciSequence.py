def fibonacci(num):
    if num <= 0:
        print("Tem que ser maior que zero para isso")
    elif num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        fib = [1, 1]
        for i in range(2, num):
            fib.append(fib[i-1] + fib[i-2])
        return fib

num = int(input("Digite um número: "))
print(f"A quantidade de numeros de Fibonacci para {num}:")
print(fibonacci(num))
