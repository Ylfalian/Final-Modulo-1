class usuario():
    def __init__(self,user,contra):
        self.user = user
        self.contra = contra 
        self.conectado = False 
        self.intentos = 2
        self.seguridad = 1
class empleado():
    def __init__(self,user,contra):
        self.user = user
        self.contra = contra 
        self.conectado = False 
        self.intentos = 2
        self.seguridad = 2
class admin():
    def __init__(self,user,contra):
        self.user = user
        self.contra = contra
        self.intentos = 2
        self.seguridad = 3
