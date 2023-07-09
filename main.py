def knapsack(pesoMochila, pesoItens, impor, item):
    memo = [[0 for i in range(pesoMochila + 1)] for j in range(item + 1)]
    
    for i in range (item):
        for j in range (1, pesoMochila + 1):
            if int(pesoItens[i]) > j:
                memo[i+1][j] = memo[i][j]
            else:
                memo[i+1][j] = max(memo[i][j], int(impor[i]) + memo[i][j-int(pesoItens[i])])
                
    return memo

impor = []
pesoItens = []
pesoMochila = int(input("Peso da mochila: "))
contador = int(input("quantidade de itens: "))

for i in range(contador):
    valor = input(f"digite o peso do {i + 1}º item: ")
    pesoItens.append(valor)
    valor = input(f"digite a importância do {i + 1}º item: ")
    impor.append(valor)


m = knapsack(pesoMochila, pesoItens, impor, contador)

for i in range(0, contador + 1):
    for j in range(0, pesoMochila + 1):
        print(f"[{m[i][j]}]", end='')
    print("\n")