import sys
import config

from game.juego_de_la_vida import JuegoDeLaVida 
from game.vecindad.vecindad_moore import VecindadMoore 
from game.frontera.frontera_ciclica import CondicionFronteraCiclica
from game.lattice.lattice_2d import Lattice2d 
from view.pygame_view import PygameView

class AplicacionSimulacion:
    """
    Clase principal (Controladora) que coordina el Autómata Celular (Modelo) y la Vista.
    
    Esta clase actúa como el Ensamblador de la aplicación, inyectando las dependencias
    concretas en el Autómata Celular.
    """
    
    def __init__(self, argumentos: list):
        """
        Constructor que procesa los argumentos de línea de comandos e inicializa el Modelo.
        
        Args:
            argumentos: La lista de argumentos pasados desde la línea de comandos (sys.argv).
        """
        # Validación y extracción de dimensiones del Lattice
        if len(argumentos) != 3: 
            sys.exit("USO: main.py CELDAS_X CELDAS_Y")
        try:
            dimensiones_lattice = (int(argumentos[1]), int(argumentos[2]))
        except ValueError:
            sys.exit("Error: Las dimensiones deben ser números enteros.")
            
        self.dimensiones_lattice = dimensiones_lattice
        self.juego_terminado = False # Bandera de estado para indicar el cierre de la ventana
        self.vista = None            # La Vista se inicializa en 'init_vista()' dentro del hilo.

        # 1. Componentes del Modelo 
        condicion_frontera = CondicionFronteraCiclica() 
        estrategia_vecindad = VecindadMoore() 
        lattice = Lattice2d() 
        
        # 2. Inicializar el Autómata (Modelo)
        # Se inyectan las implementaciones concretas en la clase abstracta AutomataCelular
        self.automata = JuegoDeLaVida(
            config.OCCUPANCY, 
            estrategia_vecindad,
            condicion_frontera,
            lattice, 
            self.dimensiones_lattice 
        )

    def init_vista(self):
        """
        Inicializa la Vista de Pygame y sus elementos gráficos.
        
        Por el diseño de hilos, esta llamada debe ocurrir dentro del hilo
        secundario.
        """
        self.vista = PygameView(
            config.TITLE, 
            config.VERSION, 
            config.CELL_DIMENSIONS, 
            config.FRAMERATE, 
            config.COLORS
        )
        # Inicializa la pantalla de Pygame con las dimensiones calculadas.
        self.vista.init(self.dimensiones_lattice)
        
    def tick_y_avanzar(self):
        """
        Ejecuta un único paso (tick) del bucle principal de la simulación.

        Este método es llamado repetidamente por el hilo de ejecución (EjecutorSimulacion).
        """
        # 1. Controla la velocidad de la simulación.
        self.vista.tick()
        
        # 2. Procesa la entrada del usuario (ej., evento QUIT).
        if self.vista.handle_input():
            self.juego_terminado = True
        
        # 3. Lógica de avance (solo si el juego no ha terminado).
        if not self.juego_terminado:
            # Pide al Modelo (Autómata) que avance una generación.
            self.automata.avanzar_generacion()
            
            # Obtiene el estado actual del Modelo.
            estado_actual = self.automata.obtener_lattice().obtener_estado()
            
            # Pide a la Vista que dibuje el nuevo estado.
            self.vista.draw_board(estado_actual)
