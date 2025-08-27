a = {
    "nome" : "nome",
    "idade": 0,
    "list" : ["0",1],
    "aultura" : 0.3,
    "dic":{
        "nome2": "nome2",
        "idade2": "idade2"
    },
    1 : 1,
    0.5 : False
}

print(a['nome'])
print(a.get("dic"))
print(a["list"][1])