lado1 = int(input("digite o primeiro lado"))
lado2 = int(input("digite o segundo lado")) 
lado3 = int(input("digite o terceiro lado")) 
if lado1 == lado2 == lado3:
    print("ele e equilatero")
elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2:
    print("ele e equilatero")
else:
    print("ele e escaleno")