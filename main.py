from productos import *
from menu import *
from userconfig import *
from validacion import vali
chequeo = []
sel = 0
while sel != 3:
    print("\nseleccione: \n 1-Iniciar Seccion\n 2-Registrarse\n 3-Salir\n")
    sel = int(input())
    if sel == 1:
        chequeo = vali(sel)
        salida = menu_product(chequeo)
        sel = salida
    elif sel == 2:
        vali(sel)
    elif sel == 3:
        print("Adios!")