class Pizza:
    def __init__(self, variedad):
        self.variedad = variedad

    def __str__(self):
        return f"Pizza de {self.variedad}"


class MaestroPizzero:
    def __init__(self, nom):
        self.nombre = nom
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    # Comando para establecer el nombre del maestro pizzero
    def establecerNombre(self, nom):
        self.nombre = nom

    # Comando para tomar un pedido y agregar una pizza a la lista de 'pizzasPorCocinar'
    def tomarPedido(self, var):
        if var:
            nueva_pizza = Pizza(var)
            self.pizzasPorCocinar.append(nueva_pizza)
            return nueva_pizza
        else:
            raise ValueError("El tipo de pizza no puede estar vacío")

    # Comando para cocinar pizzas (mueve de 'pizzasPorCocinar' a 'pizzasPorEntregar')
    def cocinar(self):
        if self.pizzasPorCocinar:
            self.pizzasPorEntregar.extend(self.pizzasPorCocinar)
            self.pizzasPorCocinar.clear()

    # Comando para entregar hasta 2 pizzas
    def entregar(self):
        pizzas_a_entregar = self.pizzasPorEntregar[:2]
        self.pizzasPorEntregar = self.pizzasPorEntregar[2:]
        return pizzas_a_entregar

    # Consulta para obtener el nombre del maestro pizzero
    def obtenerNombre(self):
        return self.nombre

    # Consulta para obtener las pizzas por cocinar
    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar

    # Consulta para obtener las pizzas por entregar
    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar


# Ejemplo de uso
pizzero = MaestroPizzero("Mario")
pizzero.tomarPedido("Margarita")
pizzero.tomarPedido("Pepperoni")
pizzero.cocinar()
print(pizzero.entregar())  # Debería entregar 2 pizzas
print(pizzero.obtenerPizzasPorEntregar())  # Debería estar vacía si no hay más pizzas
