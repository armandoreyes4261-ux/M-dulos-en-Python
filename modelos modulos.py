class Usuario:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion

    def presentacion(self):
        return f"Hola, me llamo {self.nombre} y trabajo como {self.profesion}."