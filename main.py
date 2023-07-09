import os


def knapsack(pesoMochila, pesoItens, impor, item):
    memo = [[0 for i in range(pesoMochila + 1)] for j in range(item + 1)]
    
    for i in range (item):
        for j in range (1, pesoMochila + 1):
            if int(pesoItens[i]) > j:
                memo[i+1][j] = memo[i][j]
            else:
                memo[i+1][j] = max(memo[i][j], int(impor[i]) + memo[i][j-int(pesoItens[i])])
                
    return memo

def findSolution(pesoMochila, pesoItens, impor, contador):
    memo = knapsack(pesoMochila, pesoItens, impor, contador)
    resposta = []
    i = contador
    j = pesoMochila
    while i != 0 and j != 0:
        if memo[i][j] == int(impor[i - 1]) + memo[i - 1][j-int(pesoItens[i - 1])]:
            resposta.append(i)
            memo[i][j] = memo[i - 1][j-int(pesoItens[i - 1])]
            j = j-int(pesoItens[i - 1])
            i = i - 1
        else:
            memo[i][j] = memo[i - 1][j]
            i = i - 1

    return resposta


def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

clear_screen()

print("===========================================================================================================================================================================")
print("Bem vindos, escoteiros! Antes de vocês saírem, precisamos decidir quais itens vamos levar. A ideia é que você pode levar quantos itens quiser, mas classifique a importância desse item, de 1 a 10 de preferência, e isso será um dos fatores que usaremos para calcular o que levar.")
print("===========================================================================================================================================================================\n")
impor = []
pesoItens = []
pesoMochila = int(input("Para começar nos diga o peso da mochila: "))
contador = int(input("Quantos itens temos para classificar? "))

for i in range(contador):
    valor = input(f"digite o peso do {i + 1}º item: ")
    pesoItens.append(valor)
    valor = input(f"digite a importância do {i + 1}º item: ")
    impor.append(valor)

resposta = findSolution(pesoMochila, pesoItens, impor, contador)

print("\nConsiderando a nossas opções, eu calculo que os itens mais importantes para levar com essa capacidade e com esses índices de importância serão:")
for i in range(len(resposta)):
    print(f"- o {resposta[i]}º item")