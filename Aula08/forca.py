#bibliotecas
import random
import json 
from time import sleep as delay

#abre o arquivo
with open("Aula08/palavras.json", "r", encoding="utf-8") as f:
    cadegorias = dict(json.load(f))

#como são dois comandos não pode ser lambada; só server para limpar o terminal
def clear(): delay(1); return print('\033[H\033[J')

#var
tema = ""

#função
def menu():
    p = [['1 - Animal'],
        ['2 - Comida'], 
        ['3 - Cep'], 
        ['4 - Sair']]
    for i in p:
        print(i[0])
    #menu de fato
    while True:
        opcao = input('Digite a opção desejada: ')
        #necessario para python modificar 
        global tema
        match opcao:
            case '1':
               tema = "Animal"
               #retonar a palavra empralhada
               return random.choice(cadegorias["animal"])
            case '2':
               tema = "Comida"
               return random.choice(cadegorias["comida"])
            case'3':
                tema = "CEP(cidade estado país)"
                return random.choice(cadegorias["cep"])
            case '4':
                print("saindo")
                exit()
            case _:
                print("Opção invalida")
                clear()

#ver se o user que sair
def sair():
    while True:
        input_user = input("você deseja jogar denovo(s/n): ").strip().upper()
        if input_user == "S":
            menu()
        elif input_user == "N": 
            print("saindo")
            exit()
        else:
            print("Opção invalida")
       

def jogar_forca():
    #var
    palavra = menu()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    while True:
        palavra_escondida = ''
        #pecorre a palavra
        for letra in palavra:
            #supestui a possição na string
            if letra in letras_corretas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'
        
        clear()
        #print infos
        print(f"Tema: {tema}")
        print('Palavra:', palavra_escondida)
        print('Letras erradas:', letras_erradas)
        print('Tentativas restantes:', tentativas)

        #ver se user acertou
        if palavra_escondida == palavra:
            print('Parabéns! Você ganhou!!!')
            sair()
        #ver se user perdeu
        elif tentativas == 0:
            clear()
            print('Você perdeu! A palavra era:', palavra)
            sair()

        letra_usuario = input('Digite uma letra: ').lower()

        #ver se o user acertou uma letra 
        if letra_usuario in palavra:
            print('Letra correta!')
            letras_corretas.append(letra_usuario)
            clear()    
        else:
            print('Letra errada!')
            letras_erradas.append(letra_usuario)
            tentativas -= 1
            clear()

if __name__ == '__main__':
    print('\033[H\033[J')
    print('-'*20, 'Bem vindo ao jogo da forca', 20*'-')
    jogar_forca()
