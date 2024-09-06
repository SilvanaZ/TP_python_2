class Pizza:
    def __init__(self, var):
        # Atributo de instancia: variedad de la pizza
        self.variedad = var

    # Comando para establecer la variedad de la pizza
    def establecerVariedad(self, var):
        self.variedad = var

    # Consulta para obtener la variedad de la pizza
    def obtenerVariedad(self):
        return self.variedad
