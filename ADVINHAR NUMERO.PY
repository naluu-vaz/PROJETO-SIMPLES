numeror = 10 
naleatorio = int(input("digite um numero"))

while naleatorio != numeror:
    print("nao e o real") 
    if naleatorio <=5:
        print("puts quase")
    elif naleatorio == 9:
        print("quase")
    elif naleatorio >=11:
        print("mais baixo") 
    naleatorio = int(input("digite um numero:")) 
    print("acertou")