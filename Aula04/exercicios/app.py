'''import = importa a biblioteca toda
from = importa só o metedo que vc vai usar
as = renomeia o metedo/biblioteca'''

from time import sleep as delay
from os import system as cmd

while True:
    cont = input("Digite um n°: ")
    try:
        cont = int(cont)
        while cont >= 0:
           cmd("cls")
           print(f"Contagem regrasiva: {cont}...")
           delay(1)
           cont -= 1
           cmd("cls")
        break
    except:
        print("Digite um n° válido")

print("Fim")