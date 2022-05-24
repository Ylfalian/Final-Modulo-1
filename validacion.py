from userconfig import *
cuentas = []
cu = usuario("ricardo@gmail.com","pepe123")
cu2 = empleado("jose@gmail.com","jose456")
cu3 = admin("admin@gmail.com","admin123")
cuentas.append (cu)
cuentas.append (cu2)
cuentas.append (cu3)

def vali (sel):
    if sel == 1:
        print("Ingrese el mail y luego la contraseña")
        mail = input()
        contra = input()
        for i in range (len(cuentas)):
            if mail == cuentas[i].user and contra == cuentas[i].contra:
                return cuentas[i]
    elif sel == 2:
        print("Ingrese el mail y luego la contraseña")
        mail = input()
        contra = input()
        cuentas.append (usuario(mail,contra))
        return

