numero = int(input('Digite um número: '))


if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print('Não é primo')
            
            break
    else:
        print('É primo')
else:
    print('Não é primo')