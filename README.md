
# 👾 The Game of Life - Edición SOLID & Modular

Este proyecto implementa el clásico Autómata Celular **Juego de la Vida de Conway** utilizando el lenguaje Python y la librería Pygame para la visualización. El diseño se enfoca rigurosamente en la modularidad y los **Principios SOLID** (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion), garantizando una arquitectura robusta, extensible y mantenible.

## 🌟 Características de Diseño (Principios SOLID)

El núcleo del proyecto reside en la **Abstracción** y la **Inversión de Dependencias (DIP)**:

*   **Modelo (Paquete `game`):** La lógica del Autómata Celular (`AutomataCelular` y `JuegoDeLaVida`) no conoce ninguna implementación concreta. Solo interactúa con interfaces (`ILattice`, `IEstrategiaVecindad`, `ICondicionFrontera`).
*   **Ensamblaje (Controlador):** La clase `AplicacionSimulacion` es la única responsable de crear e **inyectar** las implementaciones concretas (ej., `VecindadMoore`, `FronteraCiclica`) en las abstracciones del Modelo. Esto permite cambiar completamente el comportamiento del juego (ej. de Moore a Vecindad de Von Neumann) sin modificar el código principal.
*   **Modularidad (ISP y SRP):** El diseño está segregado en módulos pequeños y específicos:
    *   `frontera/`: Solo maneja el cálculo de coordenadas de borde.
    *   `vecindad/`: Solo calcula la posición de los vecinos.
    *   `lattice/`: Solo se encarga del almacenamiento de datos.
*   **Requisito de Hilo:** El módulo `ejecutor_hilo.py` encapsula la ejecución en un hilo separado, asegurando que el `main.py` permanezca como un punto de entrada limpio y el diseño del núcleo sea independiente del control de concurrencia.

## 📂 Estructura del Proyecto

```
.
├── game/
│   ├── frontera/                  # Lógica de las Condiciones de Borde (Interfaces e Implementaciones)
│   │   ├── frontera_ciclica.py
│   │   └── i_condicion_frontera.py
│   ├── lattice/                   # Estructura de Datos de la Retícula (Interfaces e Implementaciones)
│   │   ├── i_lattice.py
│   │   └── lattice_2d.py
│   ├── vecindad/                  # Estrategias de Vecindad (Interfaces e Implementaciones)
│   │   ├── i_estrategia_vecindad.py
│   │   └── vecindad_moore.py
│   ├── automata_celular.py        # Clase base abstracta (DIP)
│   └── juego_de_la_vida.py        # Regla de Transición (LSP)
├── view/
│   └── pygame_view.py             # Lógica de Presentación (Vista)
├── aplicacion_simulacion.py       # Ensamblador y Controlador Principal (DIP)
├── config.py                      # Constantes de configuración global
├── ejecutor_hilo.py               # Gestión de la ejecución en un hilo separado
└── main.py                        # Punto de entrada principal (Lo más corto posible)
```

## 🚀 Cómo Ejecutar el Proyecto

### 1. Requisitos

Asegúrese de tener Python (3.x recomendado) y la librería `pygame` instalados.

```bash
pip install pygame
```

### 2. Ejecución

El programa requiere que se especifiquen las dimensiones de la retícula (ancho y alto en número de células) como argumentos de línea de comandos.

```bash
# SINTAXIS: python main.py [CELDAS_X] [CELDAS_Y]
python main.py 100 80
```

*   Esto iniciará el simulador con un tablero de 100x80 células.
*   La simulación se ejecutará en un **hilo separado** (`EjecutorSimulacion`), y la ventana de Pygame se cerrará al hacer clic en la 'X'.

## 📝 Documentación del Código

Cada archivo y clase ha sido documentado exhaustivamente, incluyendo:
*   **Docstrings:** Explicando el propósito de cada clase y método.
*   **Comentarios:** Detallando la aplicación de los principios SOLID (ej., dónde ocurre la Inversión de Dependencias en el constructor de `AutomataCelular`).
*   **Tipado Estático:** Utilizando `typing` para mejorar la claridad y la integridad del código.
