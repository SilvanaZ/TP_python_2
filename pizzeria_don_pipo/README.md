
# Pizzería Don Pipo

Este proyecto simula la operación de la pizzería de Don Pipo, aplicando conceptos de Programación Orientada a Objetos (POO) en Python.

## Descripción

La pizzería cuenta con tres empleados:
- Un maestro pizzero, encargado de preparar las pizzas.
- Dos mozos, que se encargan de entregar los pedidos.

### Reglas de Negocio
1. El maestro pizzero puede recibir un pedido a la vez, pero puede preparar múltiples pizzas al mismo tiempo.
2. Los mozos solo pueden cargar hasta dos pizzas al mismo tiempo.

## Estructura del Proyecto

```
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

## Ejecución

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio o descarga el archivo comprimido con el código fuente.
2. Instala Python 3.x en tu máquina.
3. Ejecuta el archivo `main.py` en la carpeta `src` para ver la simulación del flujo de la pizzería:

```bash
python src/main.py
```

## Pruebas

Para ejecutar las pruebas, utiliza el framework `unittest` o `pytest`. Desde la carpeta raíz del proyecto, ejecuta el siguiente comando:

```bash
pytest
```

Esto ejecutará las pruebas contenidas en la carpeta `tests/`.

## Integrantes

Cada miembro del grupo debe estar listado en el archivo `integrantes.txt`, ubicado en la raíz del proyecto.

