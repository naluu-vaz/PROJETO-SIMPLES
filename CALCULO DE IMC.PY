peso = float(input("digite seu peso em kg")) 
altura = float(input("digite sua altura em metros").replace(",", ".")) 
resultado = peso / (altura * altura) 
print("o seu imc e:", resultado) 