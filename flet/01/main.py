import flet as ft
import calc

#tudo do código tem que está dentro desse def
def main(page: ft.Page):
    #titulo da pagina
    page.title = "Caculadora primitiva"
    #campo para o user digita
    txt_input_n1 = ft.TextField(label="N°1")
    txt_input_n2 = ft.TextField(label="N°2")
    txt_result = ft.Text(value="Resultado")
    
    #pega os inputs
    def get_txt():
        n1 = float(txt_input_n1.value.replace(",",".")) if txt_input_n1.value != "" else 0
        n2 = float(txt_input_n2.value.replace(",",".")) if txt_input_n2.value != "" else 0
        return (n1, n2)

    def padrao():
        txt_input_n1.value = ""
        txt_input_n2.value = ""
        txt_input_n1.update()
        txt_input_n2.update()
        return
    
    def soma(e):
        n1, n2 = get_txt()
        resulte = calc.soma(n1, n2)
        #aultualiza á o campo
        txt_result.value = f"{n1:.2f} + {n2:.2f} = {resulte}"
        txt_result.update()
        padrao()
    
    def sub(e):
        n1, n2 = get_txt()
        resulte = calc.sub(n1, n2)
        #aultualiza á o campo
        txt_result.value = f"{n1:.2f} - {n2:.2f} = {resulte}"
        txt_result.update()
        padrao()

    def mult(e):
        n1, n2 = get_txt()
        resulte = calc.mult(n1, n2)
        #aultualiza á o campo
        txt_result.value = f"{n1:.2f} X {n2:.2f} = {resulte}"
        txt_result.update()
        padrao()

    def div(e):
        n1, n2 = get_txt()
        resulte = calc.div(n1, n2)
        #aultualiza á o campo
        txt_result.value = f"{n1:.2f} ÷ {n2:.2f} = {resulte}"
        txt_result.update()
        padrao()


    page.add(
        #criar efitivamente os cambos de input e os butom
        txt_input_n1,txt_input_n2, ft.Button("+", on_click=soma),ft.Button("-",on_click=sub),
        ft.Button("÷", on_click=div),ft.Button("X", on_click= mult), txt_result
    )

#necessario para o comando "flet run ..."
ft.app(main)