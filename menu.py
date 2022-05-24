from productos import *
from modific import modifica
from userconfig import *

def menu_product (user):
    pro_dispo = []
    va1 = Auto(10000,"Nisan",10000)
    va2 = Auto(10000,"Nisan",25000)
    va3 = Auto(0,"Tesla",550000) 
    va4 = Camioneta(50000,"Ford",1000000)
    va5 = Camion(100000,"Volkswagen",500000000)
    va6 = Camion(0,"Ford",250000)
    va7 = Camion(0,"Ford",100000)
    va8 = Bicicleta("Nuevo","Playera",50000)
    va9 = Bicicleta("Usado","Mountain Bike",70000)
    va10 = Motos(500,"Yamaha",300000)
    pro_dispo.append(va1)
    pro_dispo.append(va2)
    pro_dispo.append(va3)
    pro_dispo.append(va4)
    pro_dispo.append(va5)
    pro_dispo.append(va6)
    pro_dispo.append(va7)
    pro_dispo.append(va8)
    pro_dispo.append(va9)
    pro_dispo.append(va10)
    d = 0
    while d != 3:
        if user.seguridad < 3:
            print("Elige una de las siguentes opciones\n 1-Productos\n 2-Desconectarse\n---------------\n")
            x = int(input())
            j = 1
            while j != 0:
                if x == 1:
                    print("Seleccione una categoria\n 1- Autos\n 2- Camiones\n 3- Motos\n 4- Camionetas \n 5- Acoplados\n 6- Bicicletas\n 7-Salir\n---------------\n")
                    c = int(input())
                    if c == 1:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Auto:
                                print(f"Auto = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif  c == 2:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Camion:
                                print(f"Camion = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif  c == 3:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Motos:
                                print(f"Moto = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif  c == 4:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Camioneta:
                                print(f"Camioneta = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif c == 5:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Acoplado:
                                print(f"Acoplado = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                            else:
                                print("No hay disponibles\n---------------\n")
                    elif c == 6:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Bicicleta:
                                print(f"Bicicleta = {pro_dispo[i].modelo}\nuso = {pro_dispo[i].uso}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif c == 7:
                        print("Vuelva Pronto\n---------------\n")
                        j = 0
                        d = 3
                    else:
                        print("Opcion Invalida\n---------------\n")
                elif x == 2:
                    j = 0
                    d = 3
                else:
                    print("Opcion Invalida\n---------------\n")
        elif user.seguridad == 3:
            print("Elige una de las siguentes opciones\n 1-Productos\n 2-Desconectarse\n 3-Editar\n---------------\n")
            x = int(input())
            f = 1
            while f != 0:
                if x == 1:
                    print("Seleccione una categoria\n 1- Autos\n 2- Camiones\n 3- Motos\n 4- Camionetas \n 5- Acoplados\n 6- Bicicletas\n 7-Salir\n---------------\n")
                    c = int(input())
                    if c == 1:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Auto:
                                print(f"Auto = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif  c == 2:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Camion:
                                print(f"Camion = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif  c == 3:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Motos:
                                print(f"Moto = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif  c == 4:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Camioneta:
                                print(f"Camioneta = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif c == 5:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Acoplado:
                                print(f"Acoplado = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                            else:
                                print("No hay disponibles\n---------------\n")
                    elif c == 6:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Bicicleta:
                                print(f"Bicicleta = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = {pro_dispo[i].precio}\n---------------\n")
                    elif c == 7:
                        print("Vuelva Pronto\n---------------\n")
                        f = 0
                        d = 3
                    else:
                        print("Opcion Invalida\n---------------\n")
                elif x == 2:
                    f = 0
                    d = 3
                elif x == 3:
                    pro_dispo = modifica(pro_dispo)
                    f = 0
                else:
                    print("Opcion Invalida\n---------------\n")
    return d