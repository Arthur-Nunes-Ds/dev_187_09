from random import randint 
from time import sleep as delay
TETNTATIVAS_MAX = 10
numero_s = randint(0,10)
tentativas = 0

print("Estou pensando em um número entre 0 á 10. \nAdivinhe o número que estrou pesnado!")
while tentativas < TETNTATIVAS_MAX:
    numero_i = input("Qual é o número? ")

    try:
        numero_i = int(numero_i)
    except ValueError:
        while not numero_i.isdigit():
            numero_i = input("Por favor digite apenas número inteiro: ")
    delay(1.5)
    #limpa o temnial pela sequência ANSI
    print('\033[H\033[J')
    if numero_i == numero_s:
        print(f"Você ganhou parabêns só com: {tentativas} de tentivas")
        numero_i = input("Você quer jogar denovo ^.^?(s - sim| n -não): ").lower()
        while numero_i != "s" or numero_i != "n":
            print("Selecione uma opção valida")
            numero_i = input("Se sim digite s Se não digite n: ").lower()
        else:
            if numero_i == "s":
                print("Vamos lá")
                break
            elif numero_i == "n":
                print("ok tachu")
                exit()
    elif numero_i > numero_s:
        print("Tente um número menor")
        tentativas += 1
    elif numero_i < numero_s:
        print("Tente um número maior")
        tentativas += 1
    else:
        print(f"Você perdeu >:) hahaa \n O número era : {numero_s}")
        numero_i = input("Você quer jogar denovo ^.^?(s - sim| n - não): ").lower()
        while numero_i != "s" or numero_i != "n":
            print("Selecione uma opção valida")
            numero_i = input("Se sim digite s Se não digite n: ").lower()
        else:
            if numero_i == "s":
                print("Vamos lá")
                break
            elif numero_i == "n":
                print("ok tachu")
                exit()