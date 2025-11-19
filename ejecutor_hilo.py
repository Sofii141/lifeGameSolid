import threading
import time
from aplicacion_simulacion import AplicacionSimulacion

# Bandera de control global para la ejecución de la simulación.
# Es usada para detener el bucle del hilo de forma controlada.
SIMULACION_ACTIVA = True

class EjecutorSimulacion(threading.Thread):
    """
    Clase EjecutorSimulacion: 
    
    Hereda de threading.Thread para ejecutar la aplicación de forma asíncrona.
    Encapsula el bucle de la simulación en un hilo secundario, separando la 
    responsabilidad de la concurrencia.
    """
    
    def __init__(self, aplicacion: AplicacionSimulacion):
        """
        Constructor que recibe y almacena la instancia de la aplicación a ejecutar.
        
        Args:
            aplicacion: La instancia de AplicacionSimulacion que contiene 
                        el Modelo (Autómata) y la Vista (Pygame).
        """
        threading.Thread.__init__(self)
        self.aplicacion = aplicacion
        
        # El hilo 'daemon' permite que el programa principal termine automáticamente
        # cuando todos los hilos no-daemon (el principal) hayan finalizado.
        self.daemon = True 

    def run(self):
        """
        Método de ejecución principal del hilo. 
        Contiene el bucle de la simulación del Autómata Celular.
        """
        global SIMULACION_ACTIVA
        
        # Inicialización de Pygame en Hilo Secundario.
        # Pygame se inicializa dentro del hilo. 
        # Esto puede causar problemas de 'No responde' en algunos OS.
        
        # Inicializa la Vista (Pygame.init(), pantalla, etc.)
        self.aplicacion.init_vista() 
        
        # Bucle principal de la simulación, controlado por la bandera global.
        while SIMULACION_ACTIVA:
            # Ejecuta un solo paso: maneja input, avanza la generación y redibuja.
            self.aplicacion.tick_y_avanzar()
            
            # Condición de salida: si la vista recibe un evento QUIT, establece la bandera.
            if self.aplicacion.juego_terminado: 
                SIMULACION_ACTIVA = False
                
        print("Simulación terminada.")