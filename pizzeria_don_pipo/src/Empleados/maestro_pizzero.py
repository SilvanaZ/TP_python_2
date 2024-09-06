from .empleado import Empleado

class MaestroPizzero(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Maestro Pizzero")
    
    def preparar_pizza(self, cantidad_pizzas):
        print(f"{self.nombre} está preparando {cantidad_pizzas} pizzas.")
    
    def recibir_pedido(self, pedido):
        print(f"{self.nombre} ha recibido un pedido de {len(pedido)} pizzas.")
        self.preparar_pizza(len(pedido))
    
    def trabajar(self):
        print(f"{self.nombre} está listo para recibir pedidos.")