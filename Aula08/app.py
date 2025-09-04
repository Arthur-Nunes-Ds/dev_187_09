import random
import string
#string permite fazer manipulação de str

def gera_shena(comprimento=12, incluir_maiusculo=True,incluir_menusculo=True,incluir_numero=True,incluir_caracter=True):
    caracter = ""
    if incluir_maiusculo:
        #add no caracter todas letras maiusucula
        caracter += string.ascii_uppercase
            #string.ascii_uppercase => ABCDEFGHIJKLMNOPQRSTUVWXYZ

    if incluir_menusculo:
        #add no caracter todas letras minusculas
        caracter += string.ascii_lowercase
        #string.ascii_lowercase => abcdefghijklmnopqrstuvwxyz
    
    if incluir_numero:
        #add no caracter todas letras digitos
        caracter += string.digits
        #string.digits => 0123456789

    if incluir_caracter:
        #srtring.punctuation = caracter
        #add no caracter todos caracter
        caracter +=  string.punctuation
        #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    if not caracter:
        #isso criar um erro como o VauleErro
        return ValueError("deve ter pelo menos um caractar")
    
    #emparalha a senha dentro da str; o: _ quer dizer que o proprio random.choice... 
    senha = "".join(random.choice(caracter) for _ in range(comprimento))

    return senha

def main():
    print(gera_shena())

#__name__ <= var especial
#isso aponta que esse arquivo principal
if __name__ == "__main__":
    main()