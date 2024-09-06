import unittest

class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def __str__(self):
        return f"{self.nombre} - {self.rol}"

    def trabajar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Pruebas unitarias
class TestEmpleado(unittest.TestCase):
    
    def test_creacion_empleado(self):
        empleado = Empleado("Silvana", "Desarrolladora")
        self.assertEqual(empleado.nombre, "Silvana")
        self.assertEqual(empleado.rol, "Desarrolladora")
    
    def test_str_empleado(self):
        empleado = Empleado("Silvana", "Desarrolladora")
        self.assertEqual(str(empleado), "Silvana - Desarrolladora")
    
    def test_trabajar(self):
        empleado = Empleado("Silvana", "Desarrolladora")
        with self.assertRaises(NotImplementedError):
            empleado.trabajar()

if __name__ == "__main__":
    unittest.main()
