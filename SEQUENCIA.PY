n = int(input("digite um numero"))

a = 0 
b = 1 

contador = 0 
print ("sequencia de fibonacci") 

while contador < n: 
    print(a, end=" ")
    proximo = a + b
    a = b 
    b = proximo 
    contador += 1 