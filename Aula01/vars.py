print("hello, word")#hello word é um pardigna
print(fr"\n \' \" \\") #fr vala para o python ingniroa o 'comando str' da \
print("linha \n nova linha \' \" \\ ")
print(f"str {"var"}"); print("str ", "var") #contenação
print(sep=" ", end="\n") 
'''
sep=#<- fala como vai separa
end=#<- fala como terminar
'''

print(30*"====")#<- repte no teminal "====" 30 veze

#vars simples:
nome = "" #str
numero = 0 #int
nvirgula = 0.0 #float
is_verdade = True #bool
var_vazia = None #não tem valor
print("nome", type(nome), sep="\n")#<-type() == fala o tipo que ele é
print("numero", type(numero), sep="\n")
print("nvirgula", type(nvirgula), sep="\n")
print("is_verdade", type(is_verdade), sep="\n")
print("var_vazia", type(var_vazia), sep="\n")

#operadortes matématicos
x = 10
y = 5 
soma = x+y
divi = x/ y #<- retorna float
divi_int = x//y #<- retonar int, não aredonda
mult = x*y
sub = x-y
resto = x % 2
expoende = x ** y
print(f"soma : {x} + {y} = {soma} \n", 
      f"divi: {x} / {y} = {divi}, o tipo é: {type(divi)}", 
      f"\n  mult: {x} x {y} = {divi}",
      f" \n sub: {x} - {y} = {sub}",
      f"\n divi int: {x} / {y} = {divi_int}, o tipo é: {type(divi_int)}",
      f"\n resto: {x} / {2} = {resto}, o tipo é: {type(resto)}",
      f"\n expoende: {x} ^ {y} : {expoende}")

#operadores de comparação
print(f"x>y = {x>y}",
      f"\n x<y = {x<y}",
      f"\n x>=y {x>=y}",
      f"\n x<=y {x<=y}",
      f"\n x==y {x==y}",
      f"\n x != y {x != y}")

n =1 
n += 1 # = {n = n + 1}
n -= 1 # = {n = n - 1}
#n /= ...

'''
 operadores logicos:
    and, or, not
'''

user_input = input("insira um valor: ") #<- retornar str

