
while True:
    print("menu pricipal")

    print("1.cadastrar usuario")

    print("2.ver dados cadastrados")

    print("3.sair do sistema")

    opçao = int(input("escolha uma opçao:")) 

    if opçao == 1:
        nome = input("digite seu nome")

        idade = int(input("digite sua idade")) 

        print("dados cadastrado") 

    elif opçao == 2:
           
        print(f'nome cadastrado: {nome}')

        print(f'idade cadastrada: {idade}')

    elif opçao == 3:
        print("saindo")
        break
    else:
        print("opçao invalida")

        