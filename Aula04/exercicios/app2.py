'''
    Programa Sorteio V.3.0
    Aula 04
'''         

# random.choice(list) -> embralha os elemnto da lsita
from random import choice as randomlst
from os import system as cmd
from time import sleep as delay

list = []
list_s = []
while True:
    candido = input("Digite o nomes para o sorteio ou enter para sair: ")
    if candido:
        #list.append(o desja add na lista) add no ultimo momento
        list.append(candido)
    else:
        break

while True:
    if list:
        cmd("cls")
        print(randomlst(list))
        escolido = randomlst(list)
        list_s.append(escolido)
        '''pop(idex) -> deleta por idex ou o ultimo idex
        del() -> deleta por idex mas pode remove mas de um
            CUIDADO O DEL PODE REMOVER A A LST 
        remove(elemento) -> remove o elemento
        '''
        list.remove(escolido)
        print(f"O escolido foi: {escolido}")
        opecao = input("Deseja sortear outro nomes? \n S - sim | N - não\n: ").lower()
        cmd("cls")
        if opecao != "s":
            break
    else:
        print("Não há nomes para serem sorteados!")
        break

print("End Programe")
print(f"Os candidados são: {list_s}")

