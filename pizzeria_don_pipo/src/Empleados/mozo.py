from .empleado import Empleado


class Mozo(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Mozo")
        self.capacidad = 2  # Capacidad de cargar hasta 2 pizzas
    
    def cargar_pizzas(self, cantidad_pizzas):
        if cantidad_pizzas > self.capacidad:
            print(f"{self.nombre} no puede cargar más de {self.capacidad} pizzas.")
        else:
            print(f"{self.nombre} ha cargado {cantidad_pizzas} pizzas.")
    
    def entregar_pizzas(self, cantidad_pizzas):
        print(f"{self.nombre} ha entregado {cantidad_pizzas} pizzas.")
    
    def trabajar(self):
        print(f"{self.nombre} está listo para entregar pedidos.")