inicio = int(input("digite um numero")) 
fim = int(input("digite um numero")) 

if inicio > fim: 
    inicio, fim = fim, inicio 

atual = inicio + 1 

print(f"numros pares entre {inicio} e {fim}:") 

while atual < fim: 
    if atual % 2 == 0: 
        print(atual)
    atual += 1 