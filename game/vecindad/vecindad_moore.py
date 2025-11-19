from typing import Tuple, Dict, Any
from .i_estrategia_vecindad import IEstrategiaVecindad
from ..frontera.i_condicion_frontera import ICondicionFrontera 

class VecindadMoore(IEstrategiaVecindad):
    """
    Implementación concreta de IEstrategiaVecindad utilizando la Vecindad de Moore.
    
    Esta estrategia considera las 8 células adyacentes a una célula central.
    Delega el manejo de coordenadas fuera de límite (bordes) a la interfaz 
    ICondicionFrontera inyectada.
    """

    def contar_vecinos_vivos(self, celula: Tuple[int, int], lattice: Dict[Tuple[int, int], Any], dimensiones: Tuple[int, int], frontera: ICondicionFrontera) -> int:
        """
        Cuenta el número de vecinos "vivos" para una célula dada.
        
        Args:
            celula: La coordenada (x, y) de la célula central.
            lattice: El diccionario con el estado actual de todas las células.
            dimensiones: Las dimensiones máximas del lattice (X_MAX, Y_MAX).
            frontera: La instancia de ICondicionFrontera para el manejo de bordes.
            
        Returns:
            El número total de vecinos vivos (estado 1 o -1).
        """
        puntaje = 0
        x, y = celula
        X_MAX, Y_MAX = dimensiones
        
        # Lista de las 8 direcciones (deltas) para la Vecindad de Moore
        deltas = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]

        for dx, dy in deltas:
            # 1. Aplicar la Condición de Frontera para obtener la coordenada real.
            #    Esto es clave: la VecindadMoore no sabe cómo manejar el borde, 
            #    solo pide la coordenada "real" a la implementación de Frontera.
            nx = frontera.obtener_coordenada_real(x + dx, X_MAX)
            ny = frontera.obtener_coordenada_real(y + dy, Y_MAX)
            
            vecino = (nx, ny)

            # 2. Revisa el estado del vecino en el Lattice.
            #    Se cuenta como "vivo" si su estado es 1 (vivo) o -1 (marcado para morir).
            if lattice.get(vecino) in [1, -1]: 
                puntaje += 1

        return puntaje