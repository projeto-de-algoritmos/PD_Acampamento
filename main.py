impor = []
peso = []
n = int(input("Peso da mochila: "))

for i in range(n):
    valor = input(f"digite o peso do {i + 1}º item: ")
    peso.append(valor)
    valor = input(f"digite a importância do {i + 1}º item: ")
    impor.append(valor)

for i in range(n):
    print(f"{peso[i]},{impor[i]}")