from os import name 
from os import system as cmd

cmd("git add .")
comit = input("comit: ")
cmd(f"git commit -m \"{comit}\"")
branch = input("à tua breanch é diferente de main?\n se sim informe a breanch se não só de um espaço vazio.\n :")
cmd(f"git push -u origin {"main" if branch != "" else branch}")
cmd("cls" if name == "nt" else "clear")