
# 🍕 **Pizzería Don Pipo** 🍕
**Proyecto de Simulación de Pizzería usando Programación Orientada a Objetos (POO) en Python**

---

## 📝 **Descripción del Proyecto**

**Pizzería Don Pipo** es una simulación que representa el funcionamiento de una pizzería ficticia, aplicando conceptos de Programación Orientada a Objetos (POO) en Python. El proyecto cuenta con una estructura modular y organizada para facilitar la comprensión y mantenimiento del código.

### 👨‍🍳 **Empleados**
- **Maestro Pizzero**: Responsable de preparar las pizzas. 
- **Mozos**: Dos mozos encargados de entregar los pedidos a los clientes.

### 📋 **Reglas de Negocio**
1. El **Maestro Pizzero** puede recibir un pedido a la vez, pero puede preparar múltiples pizzas simultáneamente.
2. Los **Mozos** pueden cargar hasta dos pizzas al mismo tiempo.

---

## 📂 **Estructura del Proyecto**

```plaintext
pizzeria_don_pipo/
│
├── src/
│   ├── empleados/
│   │   ├── __init__.py
│   │   ├── empleado.py
│   │   ├── maestro_pizzero.py
│   │   └── mozo.py
│   │
│   ├── pedidos/
│   │   ├── __init__.py
│   │   ├── pedido.py
│   │
│   ├── main.py
│   └── utils.py
│
├── tests/
│   ├── test_maestro_pizzero.py
│   ├── test_mozo.py
│   └── test_pedido.py
│
├── integrantes.txt
└── README.md
```

---

## 🚀 **Ejecución del Proyecto**

Sigue estos pasos para ejecutar la simulación de la pizzería:

1. **Clona el repositorio** o **descarga el archivo comprimido** con el código fuente.
2. Asegúrate de tener **Python 3.x** instalado en tu máquina.
3. Ejecuta el archivo `main.py` en la carpeta `src` para iniciar la simulación:

   ```bash
   python src/main.py
   ```

---

## ✅ **Pruebas**

Para asegurarte de que todo funciona correctamente, puedes ejecutar las pruebas incluidas. Usa `pytest` o `unittest` desde la carpeta raíz del proyecto:

```bash
pytest
```

Esto ejecutará todas las pruebas dentro de la carpeta `tests/`.

---

## 👥 **Integrantes**

El proyecto fue desarrollado por un equipo de colaboradores. Los nombres de los integrantes están listados en el archivo `integrantes.txt` en la raíz del proyecto.
