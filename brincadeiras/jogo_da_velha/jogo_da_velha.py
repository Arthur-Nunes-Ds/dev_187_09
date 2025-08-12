tabuleiro = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def print_tabuleiro():
    for i in tabuleiro:
        print(i)
    return

#aultualiza com o input do user
def slect(is_x: False, input_user: int):
    #passa pela lista toda(Linha)
    for i in range(0,3):
        #passa pela lista toda(Coluna)
        for n in range(0,3):
                #ver a onde é o input do user dentro da matrix caso o play seja o X
                if input_user == tabuleiro[i][n] and is_x:
                     #adribui um valor
                     tabuleiro[i][n] = "X"
                elif input_user == tabuleiro[i][n] and is_x == False:
                    tabuleiro[i][n] = "O"
                else:
                     #ver se o X ou O já ná posição do user
                     if tabuleiro[i][n] == "X" or tabuleiro[i][n] == "O":
                          print("valor já digitado")
    print_tabuleiro()


