#exibir só as duas primeiras casa após a virgula
valor = 1.23456789
print(f"{valor:.2f}") #<- :.n°f 
#================================================
input_user_1 = input("digit um volor decima: ").replace(",",".") #replace(plavra dentro do str , valor que eu quero supstuir)
#================================================
vars = None 
if vars:#condicional um
    pass#codigo
elif vars != 3:#condicional dois caso a primeira falha
    pass#codigo
else:#casso tudo falha
    pass#codigo

#operadores ternarios
idade = 0 
print("é maior de idade" if idade >= 18 else "é menor de idade")
#outpodo: caso a idade >= 18 seja verdadeiro ele vair imprimir é maior de idade
