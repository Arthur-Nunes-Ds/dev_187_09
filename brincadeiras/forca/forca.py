def is_iput_valido(var:str):
    is_space = var.isspace()
    if is_space:
        print()
    return

palavra = input("Digite a palvara secreta(sem espaço): ")
dica = input("Dica para plavra: ")
#limpa o temnial pela sequência ANSI
print('\033[H\033[J')
#converte a str para uma lista já com a palavra
palavra = [i for i in palavra]

while True:
    print(f"A dica da palavra é: \"{dica}\"")