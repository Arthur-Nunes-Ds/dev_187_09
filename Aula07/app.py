from time import sleep as delay
import sqlite3
from bcrypt import checkpw,hashpw,gensalt

#conecta o python e já abre e fecha 
with sqlite3.connect("Aula07/CONTAS.db") as contas:
    #um objeto para eu boter manipular via SQL o db
    db = contas.cursor()
    #seleciona a tabela dentro do DB via; seleciona a tabale 

#cripitografia a senha núm padrão aleatorio
senha_nova = lambda senha: str(hashpw(str(senha).encode(encoding="utf-8"), gensalt(8)))
id_db = 0

def verificador_senha_and_user(CPF, senha):
    #pega os dado da db
    db.execute("SELECT SENHA FROM CONTAS WHERE CPF = ?", (CPF,))
    dado = db.fetchall()

    #já ver se o user existe
    if dado:
        senha_m = dado[0][0]
        #remove as parte "b'" e á "'" 
        senha_modfication = senha_m.replace("b'","")
        senha_modfication = senha_modfication.replace("'","")
        #jogue a senha para byte
        byte_senha = senha_modfication.encode(); 
        user_senha_crypito = senha.encode(encoding="utf-8")
        #ver se a senha é valida
        if checkpw(user_senha_crypito, byte_senha):
           #pega o ID tentro da db
           db.execute("SELECT ID FROM CONTAS WHERE CPF = ?", (CPF,))
           #necessario para o python não criar uma var de scope
           global id_db
           id_db = db.fetchall()[0][0]
           return True
        else:
            print("senha invalida")
            return False
    else:
        print("usuário não encontrado")
        return False

def criar_conta(inome, cpf, data_nacimento, senha):
    db.execute("SELECT CPF FROM CONTAS")
    cpf_db = db.fetchall()
    for i in cpf_db:
        print(cpf in i)
        if not cpf in i:
            #salva tudo na db nás sua derterminadas colunas
            db.execute("INSERT INTO CONTAS (NOME, CPF, SALDO, DATA_NACIMENTO, SENHA) VALUES (?, ?, ?, ?, ?)",(inome, cpf, 0, data_nacimento, senha_nova(senha),))
            contas.commit()
            print("Cadastrado com sucesso.")
            return
    
    print("CPF já cadastrado!")
    return

def exibir_dados(i):
    db.execute("SELECT * FROM CONTAS WHERE ID = ?", (i,))
    dados = db.fetchall()
    print(f"Nome: {dados[0][1]} | CPF: {dados[0][2]} | Conta_ID :{i}\n"\
          f"Data de Nacimento : {dados[0][4]} | Saldo: {dados[0][3]} R$")
    return

def sacar_valor(i, valor):
    db.execute("SELECT SALDO FROM CONTAS WHERE ID = ?", (i,))
    dbsaldo = db.fetchall()
    dbsaldo = float(dbsaldo[0][0])
    if dbsaldo > 0:
        dbsaldo -= valor
        print(type(dbsaldo))
        print(f"Foi sacado {valor} R$ da tua conta com sucesso \n Você possui de saldo {str(dbsaldo).replace(".",",")} R$")
    else:
        db.execute("",(dbsaldo, 1))
        print(f"Saldo insuficiente \n Você tem só {str(dbsaldo).replace(".",",")}")
    return
sacar_valor(1,1)

def depositar_valor(i, valor):
    db.execute("SELECT SALDO FROM CONTAS WHERE ID = ?", (i,))
    dados = db.fetchall()
    dados[0][3] += valor
    print(f"Foi adicionado {valor} R$ na tua conta \n \
      Você possui de saldo {contas["SALDO"][i]} R$")
    return

def encerra_conta(i):
    del(contas["NOME"][i])
    del(contas["CPF"][i])
    del(contas["DATA_NACIMENTO"][i])
    del(contas["SALDO"][i])
    print("Conta deleta com sucesso")
    return

def cpf_ok (cpf:str):
    cpf = cpf.replace(".","")
    cpf = cpf.replace("-","")
    if len(cpf) == 11 and cpf.isdigit():
        return True
    return False
    
def data_nacimento_ok(data_nacimento:str):
    dt = data_nacimento.replace("/","")
    if len(dt) == 8 and dt.isdigit():
        return True
    return False

def str_int(vaule: str):
    vaule = vaule.replace(",",".")
    try:
        return float(vaule)
    except:
        str_int(input("Dgite o valor").replace(",","."))

"""while True:
    print("1- Cria conta")
    print("2- Dados da conta")
    print("3- Depositar conta")
    print("4- Sacar conta")
    print("5- Excluir conta")
    print("6- Sair")
    op = input("digite uma opção: ").strip()
    inome = input("Me fala o seu nome: ").strip()

    if contas["NOME"] != []:
        i = contas["NOME"].index(inome)
        match op:
            case "2":
                exibir_dados(i)
                delay(3.5)
                print('\033[H\033[J')
            case "3":
                valor = input("Fala o Volor para deposito")
                depositar_valor(i, int(valor))
                delay(3.5)
                print('\033[H\033[J')
            case "4":
                valor = input("Fala o Volor para deposito")
                sacar_valor(i, int(valor))
                delay(3.5)
                print('\033[H\033[J')
            case "5":
                encerra_conta(i)
                delay(3.5)
                print('\033[H\033[J')
            case "6":
                exit()
            case _:
                print("opção invalida/inesetente")
    elif op == "1":
        cpf = input("digite o seu cpf(123.456.789-01): ").strip()
        data_nacimento = input("digite a sua data de nacimento(dd/mm/aaaa): ").strip()
        if cpf_ok(cpf) and data_nacimento_ok(data_nacimento):
            criar_conta(inome, cpf,data_nacimento)
        else:
            print("digite um cpf/data de nacimento validos")
        delay(3.5)
        print('\033[H\033[J') 
    elif op == "6":
        exit()
    else:
        print("opção invalida ou Você não tem conta para acessar as outras opção")
        delay(3.5)
        print('\033[H\033[J')
"""
