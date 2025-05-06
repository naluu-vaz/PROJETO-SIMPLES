n = int(input("digite um numero:"))
fatorial = 1 
if n < 0:
    print("nao e possivel calcular numero negativo")
else: 
    for i in range (1,n + 1 ):
        fatorial *= i 
        print(f"o fator de {n} e {fatorial}")