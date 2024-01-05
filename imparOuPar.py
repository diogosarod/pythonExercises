num = int(input("Digite um número: ")) 

def cal(a): 
    rest = a % 2 
    if rest == 0: 
        print(f"{a} é par") 
    else: 
        print(f"{a} é ímpar") 

cal(num)
