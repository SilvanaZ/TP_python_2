from src.empleados.maestro_pizzero import Pizza

class Mozo:
    def __init__(self, nom):
        # Atributo de instancia: nombre del mozo y lista de pizzas (inicialmente vacía)
        self.nombre = nom
        self.pizzas = []

    # Comando para establecer el nombre del mozo
    def establecerNombre(self, nom):
        self.nombre = nom

    # Comando para que el mozo tome pizzas (máximo 2)
    def tomarPizzas(self, pizzas):
        if len(pizzas) + len(self.pizzas) > 2:
            raise ValueError("El mozo no puede llevar más de 2 pizzas.")
        self.pizzas.extend(pizzas[:2 - len(self.pizzas)])

    # Comando para servir las pizzas (limpia la lista de pizzas)
    def servirPizzas(self):
        self.pizzas.clear()

    # Consulta para obtener el nombre del mozo
    def obtenerNombre(self):
        return self.nombre

    # Consulta para obtener las pizzas que el mozo está llevando
    def obtenerPizzas(self):
        return self.pizzas

    # Consulta para saber si el mozo está libre
    def obtenerEstadoLibre(self):
        return len(self.pizzas) < 2

# Ejemplo de uso
mozo = Mozo("Carlos")
print(mozo.obtenerEstadoLibre())  # Debería imprimir True (libre)

pizza1 = Pizza("Margarita")
pizza2 = Pizza("Pepperoni")
mozo.tomarPizzas([pizza1, pizza2])

print(mozo.obtenerPizzas())  # Debería imprimir las dos pizzas
print(mozo.obtenerEstadoLibre())  # Debería imprimir False (ocupado)

mozo.servirPizzas()
print(mozo.obtenerPizzas())  # Debería imprimir una lista vacía
print(mozo.obtenerEstadoLibre())  # Debería imprimir True (libre)
