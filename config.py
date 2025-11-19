# Almacena todas las constantes de configuración global.

# Título y versión del programa
TITLE = "The Game of Life - SOLID Edition"
VERSION = "2.2"

# Dimensiones de cada celda (en píxeles) para el dibujado en Pygame
CELL_DIMENSIONS = (8, 8)

# Tasa de cuadros por segundo (FPS) de la simulación.
# Controla la velocidad de la evolución del juego.
FRAMERATE = 20

# Probabilidad inicial de Ocupación:
# Representa la fracción (0.0 a 1.0) de células que estarán VIVAS (1) 
# al inicio del juego (al generarse el tablero aleatorio).
OCCUPANCY = 0.20

# Colores usados para representar los estados de las células
# 0: Muerta (Negro) | 1: Viva (Amarillo/Blanco)
COLORS = {0: (0, 0, 0), 1: (200, 200, 100)}