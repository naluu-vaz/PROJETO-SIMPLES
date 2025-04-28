valor = int(input("digite um valor"))
if valor>=100:
    print("tem desconto")
    des = int(input("digite o desconto"))
    resultado = valor /100 * des
    pagar = valor - resultado
    print("valor a pagar", pagar)
else:
    print("nao tem desconto") 