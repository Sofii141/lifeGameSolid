from abc import ABC, abstractmethod
from typing import Tuple, Dict, Any

class ICondicionFrontera(ABC):
    """
    Interfaz para definir la Condición de Frontera.
    
    Esta interfaz es pequeña y específica, encargándose de la única
    responsabilidad de calcular coordenadas cuando se accede fuera de los límites.
    """
    
    @abstractmethod
    def obtener_coordenada_real(self, coordenada_deseada: int, dimension_maxima: int) -> int:
        """
        Método abstracto para calcular la coordenada que se debe usar en la retícula.
        
        Si la coordenada_deseada está fuera de [0, dimension_maxima - 1], este 
        método determina el comportamiento del borde (ej. cíclico, fijo, etc.).
        
        Args:
            coordenada_deseada: La coordenada calculada antes de aplicar la regla de frontera.
            dimension_maxima: El tamaño máximo del eje (ej. ancho o alto de la retícula).
            
        Returns:
            La coordenada real dentro de los límites de la retícula.
            
        Raises:
            NotImplementedError: Si el método no es implementado por una subclase.
        """
        pass