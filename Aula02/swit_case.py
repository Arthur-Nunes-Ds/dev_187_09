while True:
    try:
        etanol = float(input("Digite o valor da gosolinaentanol em real: ").replace(",","."))
        gasolina = float(input("Digite o valor da gosolina em real: ").replace(",","."))
        calculo = (etanol/gasolina)*100
        restudado = "gasolina" if calculo > 70 else "etanol"
        print(f"Resultado = {calculo:.2f}%. Compensa abstecer com{restudado}.")
        #sprit() -> tira os " "antes e depois do texto
        opecao = input("Deseja refazer o calculo? (s/n) ").lower().strip()
        #swit/match case
        match opecao:
            case "s":
                continue
            case "n":
                break
            #_ -> todas var sem nada
            case _:
                print("opção invalida")
                continue
    except Exception as e:
        print(f"não foi posivel escuda a operação: {e}")
        continue