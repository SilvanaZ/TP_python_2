class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def __str__(self):
        return f"{self.nombre} - {self.rol}"

    def trabajar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")