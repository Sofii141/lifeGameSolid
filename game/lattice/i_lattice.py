from abc import ABC, abstractmethod
from typing import Tuple, Dict, Any

class ILattice(ABC):
    """
    Interfaz para la estructura de datos que almacena el estado de la retícula.
    
    Esta interfaz define los métodos necesarios para la gestión del estado 
    (inicialización, lectura, escritura) y las dimensiones del AC.
    """
    
    @abstractmethod
    def inicializar(self, dimensiones: Tuple[int, int], ocupacion_inicial: float):
        """
        Inicializa el lattice con sus dimensiones y estado inicial.
        
        Args:
            dimensiones: El tamaño de la lattice.
            ocupacion_inicial: La probabilidad de ocupación inicial.
        """
        pass
    
    @abstractmethod
    def obtener_dimensiones(self) -> Tuple[int, int]:
        """
        Devuelve las dimensiones (X_MAX, Y_MAX) del Lattice.
        
        Returns:
            Una tupla que representa el tamaño de la retícula.
        """
        pass
    
    @abstractmethod
    def obtener_estado(self) -> Dict[Tuple[int, int], Any]:
        """
        Devuelve el diccionario completo de coordenadas y estados del Lattice.
        
        Returns:
            Un diccionario con el estado actual de todas las células.
        """
        pass
    
    @abstractmethod
    def actualizar_estado(self, celula: Tuple[int, int], nuevo_estado: Any):
        """
        Asigna un nuevo estado a una célula específica.
        
        Args:
            celula: La coordenada (x, y) de la célula a actualizar.
            nuevo_estado: El nuevo estado (valor) a asignar.
        """
        pass