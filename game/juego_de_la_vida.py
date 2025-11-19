from .automata_celular import AutomataCelular
from .vecindad.i_estrategia_vecindad import IEstrategiaVecindad
from .frontera.i_condicion_frontera import ICondicionFrontera 
from .lattice.i_lattice import ILattice 
from typing import Tuple

class JuegoDeLaVida(AutomataCelular):
    """
    Implementación concreta del Autómata Celular para el Juego de la Vida de Conway.
    
    Esta clase es un subtipo válido de AutomataCelular y define la Regla
    de Transición Local específica de este juego.
    """
    
    def __init__(self, ocupacion: float, estrategia_vecindad: IEstrategiaVecindad, 
                 condicion_frontera: ICondicionFrontera, 
                 lattice: ILattice,
                 dimensiones: Tuple[int, int]):
        """
        Constructor que inicializa el Juego de la Vida, pasando todas las 
        abstracciones requeridas a su clase base.
        """
        super().__init__(ocupacion, estrategia_vecindad, condicion_frontera, lattice, dimensiones)

    def avanzar_generacion(self):
        """
        Implementación de la Regla de Transición Local del Juego de la Vida.
        Calcula el estado futuro de cada célula basándose en los estados actuales.
        """
        
        # Obtenemos las propiedades y el estado del Lattice (desde las abstracciones)
        dimensiones = self.lattice.obtener_dimensiones()
        reticula_estado = self.lattice.obtener_estado()

        # Fase 1: Marcar cambios (Usando estados temporales 2 y -1)
        # Esto asegura que todas las decisiones se tomen en base al estado inicial 
        # de la generación, evitando conflictos de actualización.
        for celula in reticula_estado:
            
            # Pide a la Estrategia de Vecindad contar los vecinos, usando la Condición de Frontera inyectada.
            vecinos = self.estrategia_vecindad.contar_vecinos_vivos(
                celula, 
                reticula_estado,
                dimensiones, 
                self.condicion_frontera
            )
            estado_actual = reticula_estado[celula]
            
            # Reglas de Conway's Life
            # 1. Reproducción: Célula muerta (0) con 3 vecinos vivos, NACE (marca temporal 2)
            if estado_actual == 0 and vecinos == 3:
                self.lattice.actualizar_estado(celula, 2)
            
            # 2. Supervivencia/Muerte por soledad o sobrepoblación: Célula viva (1)
            #    con < 2 o > 3 vecinos, MUERE (marca temporal -1)
            elif estado_actual == 1 and vecinos not in [2, 3]:
                self.lattice.actualizar_estado(celula, -1)

        # Fase 2: Realizar cambios (Transición de Estados)
        # Se recorre nuevamente para aplicar los estados temporales marcados.
        for celula in reticula_estado:
            estado = reticula_estado[celula]
            
            # Aplicar Nacimiento: 2 (Nace) -> 1 (Viva)
            if estado == 2: 
                self.lattice.actualizar_estado(celula, 1) 
            
            # Aplicar Muerte: -1 (Muere) -> 0 (Muerta)
            if estado == -1: 
                self.lattice.actualizar_estado(celula, 0)