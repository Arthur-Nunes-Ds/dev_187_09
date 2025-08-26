#manipulação de aquivos
#abre o arquivo no modo de leitura
import json
with open("Aula05/arquivo.txt","r", encoding="utf-8") as f: 
    #open(arquivo, modo_de_leitura)
    #pasa a var para o arquivo
    texto = f.read()

print(texto)

#abre o arquivo para ser complemetado
with open("Aula05/arquivo.txt", "a", encoding="utf-8") as f:
    #add a str com base no ultimo poteiro
    f.write("\nbom dia")

#delta tudo dentro do txt e refasa ele
with open("Aula05/arquivo.txt","w", encoding="utf-8") as f:
    f.write("python :)")



with open("Aula05/json.json", "r") as f:
    dic_sjon = dict(json.load(f))

#pega os elemntos do arquivo
print(dic_sjon.get("dic"))
print(dic_sjon["list"][1])