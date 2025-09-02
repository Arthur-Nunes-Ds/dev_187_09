#def / func
# se tive duas palavras deve ser usar a pratica do Snake Case => palavra1_palvra2_pala...
def test(parametro1,parameto2 = None, parametro3 = None):#nesse caso o parameto2 e 3 não são brigadorios
    #none = null
    #função sem retorno
    print("código dentro de test")

def soma(a , b):
    return a+b #ele pode retorna nada; pode retorna qualquer tipo de dado

def test_1():
    yield f"situação 1" #<- uma espece de retonor só fuciona se timver o next ou um for
    yield f"situação 2"
    yield f"situação 3"

#usando o print
print(f"situação 1 = {next(test_1())}")
print(f"situação 2 = {next(test_1())}")
print(f"situação 3 = {next(test_1())}")

#usando o for
n = test_1()
for i in n:
    print(i)

def sub(x,y):
    return print(x-y)

subtra = lambda x,y : x-y #é a mesma coisa do sub


lmbd = lambda x: x * 2
numeros = [1,2,3,4,5]
#map ele vai executar a função por cada número da lista
print(list(map(lmbd, numeros)))
# retorna => [2,4,6,8,10]


#pytube