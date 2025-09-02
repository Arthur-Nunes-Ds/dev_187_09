from time import sleep as delay

contas = {
    "NOME":[],
    "CPF":[],
    "DATA_NACIMENTO":[],
    "SALDO":[],
}

def criar_conta(inome, cpf, data_nacimento):
    contas["NOME"].append(inome)
    contas["CPF"].append(cpf)
    contas["DATA_NACIMENTO"].append(data_nacimento)
    contas["SALDO"].append(0)
    return

def exibir_dados(i):
    print(f"Nome: {contas["NOME"][i]} | CPF: {contas["CPF"][i]} \n"\
          f"Data de Nacimento : {contas["DATA_NACIMENTO"][i]} | Saldo: {contas["SALDO"][i]} R$")
    return

def sacar_valor(i, valor):
    if contas["SALDO"][i] > 0:
        contas["SALDO"][i] -= valor
        print(f"Foi sacado {valor} R$ da tua conta com sucesso \n \
              Você possui de saldo {contas["SALDO"][i]} R$")
    else:
        print("Saldo insuficiente")
    return

def depositar_valor(i, valor):
    contas["SALDO"][i] += valor
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

while True:
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