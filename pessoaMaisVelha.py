pessoas = []

def calcmax(pessoas):
 velho = max(pessoas, key=lambda pessoa: pessoa["idade"])
 print(f"A pessoa mais velha é o(a) {velho['nome']}, com {velho['idade']} anos")
 
for i in range(4):
    print(f"{i+1}° usuário")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    pessoas.append({"nome": nome, "idade": idade})
    
calcmax(pessoas)