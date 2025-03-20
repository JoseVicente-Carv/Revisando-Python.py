numeros = []

while True:
    num = int(input("Digite o numero: "))
    if(num==0):
        break
    else:
        numeros.append(num)

soma = sum(numeros)

print(f'A soma de todos os números é {soma}.')