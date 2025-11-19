from typing import Tuple, Dict, Any
from abc import ABC, abstractmethod

class IEstrategiaVecindad(ABC):
    """
    Interfaz para definir una Estrategia de Vecindad.
    
    Esta interfaz es pequeña y específica, forzando a las implementaciones 
    a definir únicamente la lógica para identificar y contar el estado de los vecinos.
    """
    
    @abstractmethod
    def contar_vecinos_vivos(self, celula: Tuple[int, int], lattice: Dict[Tuple[int, int], Any], dimensiones: Tuple[int, int], frontera: Any) -> int:
        """
        Método abstracto para contar los vecinos vivos de una célula dada.
        
        Args:
            celula: La coordenada (x, y) de la célula central.
            lattice: El diccionario con el estado de todas las células.
            dimensiones: Las dimensiones máximas del Lattice (X_MAX, Y_MAX).
            frontera: Un objeto que implementa la ICondicionFrontera (se usa Any aquí 
                      para evitar dependencia circular en el archivo de interfaz, 
                      aunque en la implementación se especifica).
            
        Raises:
            NotImplementedError: Si el método no es implementado por una subclase.
        """
        pass