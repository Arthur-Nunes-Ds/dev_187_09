#lista
#idex:  0, 1,...
lst = ["a",1,True]
print(lst, type(lst), sep="   ")
#pecorre todos os dados é imprime
for i in lst:
    print(i)

#imprima : a
print(lst[0])

#imprima : [True, 1, "a"]
print(lst[::-1])

#range(inicio,fim,passo) = gera uma espece de intervalo entre (incio até fim)
"""
    o inicio por padrão é de: 0
    passo é tipo se ele pula de 2 em 2
"""

#len() -> retonar a qnt de coisa que tem na var
print("-"*30)
#-------------------------------------------------------------------------------------------
nomes = ["Arthur", "João", "Maria", "Pedro", "Ana", "Carlos"]
    #organiza a lista nesse caso em orde alfabetica
#nomes = sorted(nomes)
nomes.sort()
print(nomes)
# index me retorna o n° do index
print( nomes.index("João") )
print("-"*30)
#------------------------------------------------------------------------------------------
n = [1,1,1,1,1,1,1,1,1,23,4,5,4,4,367,22,528,58,42,57,62,47,254,4,8,254,82,458,6,8]
#list.conut(o que vc que achar)
print(n.count(1))
print("-"*30)
#------------------------------------------------------------------------------------------
#altera o elemto no index 0 para "alex"
n[0] = "alex"
print(n)

print("-"*30)
#-------------------------------------------------------------------------------------------
#tratamento de erro:
i1 = input("i1: ")
try:
    i1 = int(i1)
except ValueError:
    print("Erro")

print(type(i1))
#-------------------------------------------------------------------------------------------
lst1 =["a","b","c","d","e"]
#join junta tudo da lista o "," e o caracter para sepra os elemnteos do arry
print(",".join(lst1))
#-------------------------------------------------------------------------------------------
str1 = "a b c d e"
#criar uma lista separa do pelo caracter
lst_1 = str1.split(" ")
print(lst_1)
#-------------------------------------------------------------------------------------------
