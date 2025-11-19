import sys
from aplicacion_simulacion import AplicacionSimulacion
from ejecutor_hilo import EjecutorSimulacion

def iniciar_aplicacion():
    """
    Función de punto de entrada principal para iniciar la simulación.
    
    Esta función se encarga de ensamblar los componentes de la aplicación 
    e iniciar la ejecución en un hilo separado, cumpliendo con el requisito.
    """
    
    # 1. Crea la instancia de AplicacionSimulacion.
    #    Esta clase gestiona las dependencias del Modelo (Autómata) y la Vista (Pygame).
    aplicacion = AplicacionSimulacion(sys.argv)
    
    # 2. Crea el objeto EjecutorSimulacion (el hilo de ejecución).
    #    Se inyecta la instancia de 'aplicacion' para que el hilo pueda acceder 
    #    a su lógica de Modelo y Vista.
    program_thread = EjecutorSimulacion(aplicacion)
    
    # 3. Inicia la ejecución del hilo.
    #    El método run() de EjecutorSimulacion comenzará a ejecutarse en paralelo.
    program_thread.start()
    
    # 4. Espera a que el hilo de simulación termine.
    #    El método join() detiene la ejecución del hilo principal (main) hasta 
    #    que el 'program_thread' haya finalizado (p.ej., cuando se cierra la ventana).
    program_thread.join()


if __name__ == "__main__":
    # Código que se ejecuta cuando el script es invocado directamente.
    iniciar_aplicacion()