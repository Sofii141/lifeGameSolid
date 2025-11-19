import pygame
from pygame.locals import *
from typing import Tuple, Dict, Any

class PygameView:
    """
    Clase PygameView: 
    
    Implementa la capa de Vista para la simulación. Su responsabilidad es interactuar 
    directamente con la librería Pygame para:
    1. Mostrar el estado del Modelo (tablero/Lattice).
    2. Recibir las acciones básicas del usuario (ej., cerrar la ventana).
    """
    
    def __init__(self, title: str, version: str, cell_dimensions: Tuple[int, int], framerate: int, colors: Dict[int, Tuple[int, int, int]]):
        """
        Constructor que recibe todas las configuraciones visuales desde config.py y las almacena.
        
        Args:
            title: Título de la ventana.
            version: Versión del programa.
            cell_dimensions: Ancho y alto de cada célula en píxeles.
            framerate: Tasa de cuadros por segundo (FPS).
            colors: Diccionario de mapeo de estados del Modelo a colores RGB.
        """
        self.title = title
        self.version = version
        self.cell_dimensions = cell_dimensions
        self.framerate = framerate
        self.colors = colors
        
        self.screen = None  # Surface principal (la ventana)
        self.bg = None      # Surface de fondo para dibujar (evita parpadeo)
        self.clock = None   # Objeto Clock para control de FPS

        
    def init(self, board_dimensions: Tuple[int, int]):
        """
        Inicializa Pygame y configura la ventana de visualización.
        
        Args:
            board_dimensions: Dimensiones del tablero en número de células (X, Y).
        """
        pygame.init()

        # Calcula las dimensiones de la ventana en píxeles
        dimensions = (board_dimensions[0] * self.cell_dimensions[0],
                      board_dimensions[1] * self.cell_dimensions[1])
        
        self.screen = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(self.title + " " + self.version)
        self.bg = self.screen.convert() # Surface de dibujo
        self.clock = pygame.time.Clock() # Objeto para controlar el FPS
        
    def tick(self):
        """
        Controla el tiempo. Llama al método tick() del clock para pausar la 
        ejecución hasta alcanzar el framerate deseado.
        """
        self.clock.tick(self.framerate)

    def draw_board(self, board: Dict[Tuple[int, int], Any]):
        """
        Renderiza el estado actual del tablero/Lattice en la ventana.
        
        Args:
            board: Un diccionario que representa el estado del Lattice (coordenadas: estado).
        """
        for cell in board:
            # Calcula el rectángulo (posición y tamaño) de la célula a dibujar
            rectangle = (cell[0] * self.cell_dimensions[0], cell[1] * self.cell_dimensions[1],
                         self.cell_dimensions[0], self.cell_dimensions[1])
                         
            # Dibuja la célula rellenando el rectángulo con el color mapeado al estado.
            self.bg.fill(self.colors[board[cell]], rectangle)

        # Copia la surface de dibujo (bg) a la surface principal (screen)
        self.screen.blit(self.bg, (0, 0))
        # Actualiza el contenido visible de la ventana
        pygame.display.flip()

    def handle_input(self) -> bool:
        """
        Procesa eventos de usuario de bajo nivel (ej., teclado, ratón, cierre de ventana).
        
        Returns:
            True si se detecta el evento QUIT (cerrar ventana), False en caso contrario.
        """
        for e in pygame.event.get():
            if e.type == QUIT:
                return True # Indica al Controlador que debe salir del bucle
        return False # Continúa la simulación