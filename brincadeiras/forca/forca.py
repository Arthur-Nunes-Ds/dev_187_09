def is_iput_valido(var:str):
    is_space = var.isspace()
    if is_space:
        print()
    return

palavra = input("Digite a palvara secreta(sem espaço): ")
dica = input("Dica para plavra: ")
#limpa o temnial pela sequência ANSI
print('\033[H\033[J')
n_palvra = len(palavra.strip().replace(" ", ""))
palavra_dic = [i for i in palavra]
l_digitidado = []
vida = 6

while True:
    print(f"Quantidade de letra: {n_palvra}")
    print(f"A dica da palavra é: \"{dica}\"")
    print(f"Você tem {vida} vida(s)")
    i_user = input("digite uma letra: ")
    if i_user in palavra_dic:
        for i in palavra_dic:
            if i_user == i:
                l_digitidado.append(i_user)
                palavra_dic.remove(i_user)
    elif i_user in l_digitidado:
        print("Letra já digitado")
    else:
        print("Não tem essa letra \n Você perdeu uma vida")
        vida -= 1 

    if palavra == [] and vida >= 1:
        print("você ganho")
    elif vida <= 0:
        print("Você perdeu") 
        print(f"A palavra erra {vida}") 
        
    print(f"letras já digitadas: {l_digitidado}")
        

