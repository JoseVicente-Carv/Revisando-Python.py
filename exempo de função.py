def verificar(numero):
    if (numero > 0):
        print('Numero positivo.')
    elif (numero == 0):
        print('Numero neutro.')
    else:
        print('Numero Negativo.')

numeroDigitado = int(input('Digite um numero: '))

verificar(numeroDigitado)