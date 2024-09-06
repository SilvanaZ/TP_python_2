from src.empleados.maestro_pizzero import MaestroPizzero
from src.empleados.mozo import Mozo



class TesterPizzeria:
    def main(self):
        # 5.a. Crear objetos de tipo MaestroPizzero, Mozo y Pizza
        maestro_pizzero = MaestroPizzero("Giovanni")
        mozo1 = Mozo("Alfredo")
        mozo2 = Mozo("Mario")

        # 5.b. Enviar mensajes tomarPedido, cocinar y entregar al MaestroPizzero
        maestro_pizzero.tomarPedido("Margarita")
        maestro_pizzero.tomarPedido("Pepperoni")
        maestro_pizzero.cocinar()
        pizzas_entregadas = maestro_pizzero.entregar()

        print(f"Pizzas entregadas por {maestro_pizzero.obtenerNombre()}: {[str(pizza) for pizza in pizzas_entregadas]}")

        # 5.c. Enviar mensajes tomarPizzas y servirPizzas a los objetos Mozo
        mozo1.tomarPizzas(pizzas_entregadas[:2])  # Mozo 1 toma hasta 2 pizzas
        print(f"Pizzas tomadas por {mozo1.obtenerNombre()}: {[str(pizza) for pizza in mozo1.obtenerPizzas()]}")
        mozo1.servirPizzas()  # Mozo 1 sirve las pizzas
        print(f"Estado de {mozo1.obtenerNombre()} después de servir: {mozo1.obtenerPizzas()}")

        # Comparación de objetos (punto 4)
        mozo1 = Mozo('Alfredo')
        mozo2 = Mozo('Alfredo')
        print("i. ¿mozo1 y mozo2 hacen referencia al mismo objeto?", mozo1 is mozo2)
        print("ii. ¿mozo1 y mozo2 son objetos equivalentes?", mozo1 == mozo2)
        print("iii. ¿mozo1 y mozo2 comparten la misma posición de memoria?", id(mozo1) == id(mozo2))

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()
