from productos import *

def modifica (product):
    var=""
    j=1
    while j != 0:
        print("Seleccione una categoria a modificar\n 1- Autos\n 2- Camiones\n 3- Motos\n 4- Camionetas \n 5- Acoplados\n 6- Bicicletas\n 7-Salir\n---------------\n")
        c = int(input())
        if c == 1:
            for i in range(len(product)):
                if type(product[i]) == Auto:
                    print(f"Auto = {product[i].modelo}\nKm = {product[i].km}\nPrecio = {product[i].precio}\n---------------\n")
                    print("Si desea Modificarlo Escriba [Modificar] en caso contrario escriba [No]\n\n ")
                    var = input()
                    var = var.lower()
                    if var == "modificar":
                        product[i].modelo = input("Ingrese el modelo\n")
                        product[i].km = int(input("Indique los Kilomentros del Vehiculo\n"))
                        product[i].Precio = int(input("Indique el Valor del Vehiculo\n"))
                    elif var == "no":
                        print("Pasando al siguiente Vehiculo...\n")
        elif  c == 2:
            for i in range(len(product)):
                if type(product[i]) == Camion:
                    print(f"Camion = {product[i].modelo}\nKm = {product[i].km}\nPrecio = {product[i].precio}\n---------------\n")
                    print("Si desea Modificarlo Escriba [Modificar] en caso contrario escriba [No]\n\n ")
                    var = input()
                    var = var.lower()
                    if var == "modificar":
                        product[i].modelo = input("Ingrese el modelo\n")
                        product[i].km = int(input("Indique los Kilomentros del Vehiculo\n"))
                        product[i].Precio = int(input("Indique el Valor del Vehiculo\n"))
                    elif var == "no":
                        print("Pasando al siguiente Vehiculo...\n")
        elif  c == 3:
            for i in range(len(product)):
                if type(product[i]) == Motos:
                    print(f"Moto = {product[i].modelo}\nKm = {product[i]}\nPrecio = {product[i].precio}\n---------------\n")
                    print("Si desea Modificarlo Escriba [Modificar] en caso contrario escriba [No]\n\n ")
                    var = input()
                    var = var.lower()
                    if var == "modificar":
                        product[i].modelo = input("Ingrese el modelo\n")
                        product[i].km = int(input("Indique los Kilomentros del Vehiculo\n"))
                        product[i].Precio = int(input("Indique el Valor del Vehiculo\n"))
                    elif var == "no":
                        print("Pasando al siguiente Vehiculo...\n")
        elif  c == 4:
            for i in range(len(product)):
                if type(product[i]) == Camioneta:
                    print(f"Camioneta = {product[i].modelo}\nKm = {product[i].km}\nPrecio = {product[i].precio}\n---------------\n")
                    print("Si desea Modificarlo Escriba [Modificar] en caso contrario escriba [No]\n\n ")
                    var = input()
                    var = var.lower()
                    if var == "modificar":
                        product[i].modelo = input("Ingrese el modelo\n")
                        product[i].km = int(input("Indique los Kilomentros del Vehiculo\n"))
                        product[i].Precio = int(input("Indique el Valor del Vehiculo\n"))
                    elif var == "no":
                        print("Pasando al siguiente Vehiculo...\n")
        elif c == 5:
            for i in range(len(product)):
                if type(product[i]) == Acoplado:
                    print(f"Acoplado = {product[i].modelo}\nKm = {product[i].km}\nPrecio = {product[i].precio}\n---------------\n")
                    print("Si desea Modificarlo Escriba [Modificar] en caso contrario escriba [No]\n\n ")
                    var = input()
                    var = var.lower()
                    if var == "modificar":
                        product[i].modelo = input("Ingrese el modelo\n")
                        product[i].km = int(input("Indique los Kilomentros del Vehiculo\n"))
                        product[i].Precio = int(input("Indique el Valor del Vehiculo\n"))
                    elif var == "no":
                        print("Pasando al siguiente Vehiculo...\n")
                else:
                    print("No hay disponibles\n---------------\n")
        elif c == 6:
            for i in range(len(product)):
                if type(product[i]) == Bicicleta:
                    print(f"Bicicleta = {product[i].modelo}\nKm = {product[i].uso}\nPrecio = {product[i].precio}\n---------------\n")
                    print("Si desea Modificarlo Escriba [Modificar] en caso contrario escriba [No]\n\n ")
                    var = input()
                    var = var.lower()
                    if var == "modificar":
                        product[i].modelo = input("Ingrese el modelo\n")
                        product[i].uso = int(input("Indique el uso de la Bicicleta\n"))
                        product[i].Precio = int(input("Indique el Valor de la Bicicleta\n"))
                    elif var == "no":
                        print("Pasando al siguiente Vehiculo...\n")
        elif c == 7:
            j = 0
            print("Vuelva Pronto\n---------------\n")
        else:
            print("Opcion Invalida....")
    return(product)