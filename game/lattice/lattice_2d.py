import random
from typing import Tuple, Dict, Any
from .i_lattice import ILattice 

class Lattice2d(ILattice):
    """
    Implementación concreta de ILattice para una retícula bidimensional.
    
    Esta clase es responsable del almacenamiento de los datos del Autómata Celular.
    Utiliza un diccionario cuyas claves son tuplas (coordenadas) y cuyos valores 
    son el estado de la célula.
    """

    def __init__(self):
        """
        Constructor que inicializa el estado interno del lattice.
        """
        self._dimensiones: Tuple[int, int] = (0, 0)
        self._estado: Dict[Tuple[int, int], Any] = {}
        
    def inicializar(self, dimensiones: Tuple[int, int], ocupacion_inicial: float):
        """
        Inicializa el lattice con sus dimensiones y un estado inicial aleatorio.
        
        Args:
            dimensiones: La tupla (X_MAX, Y_MAX) que define el tamaño del lattice.
            ocupacion_inicial: La probabilidad (0.0 a 1.0) de que una célula esté viva (1).
        """
        self._dimensiones = dimensiones
        X_MAX, Y_MAX = dimensiones
        
        # Generación aleatoria del estado inicial de cada célula.
        for x in range(X_MAX):
            for y in range(Y_MAX):
                # Asigna 1 (vivo) o 0 (muerto) según la probabilidad de ocupación.
                inicial = 1 if random.random() < ocupacion_inicial else 0
                self._estado[(x, y)] = inicial

    def obtener_dimensiones(self) -> Tuple[int, int]:
        """
        Devuelve las dimensiones (X_MAX, Y_MAX) del Lattice.
        
        Returns:
            Una tupla con las dimensiones del lattice.
        """
        return self._dimensiones
        
    def obtener_estado(self) -> Dict[Tuple[int, int], Any]:
        """
        Devuelve el diccionario de coordenadas y estados (el estado completo del Lattice).
        
        Returns:
            El diccionario que mapea coordenadas a estados de células.
        """
        return self._estado
        
    def actualizar_estado(self, celula: Tuple[int, int], nuevo_estado: Any):
        """
        Asigna un nuevo estado a una célula específica.
        
        Args:
            celula: La coordenada (x, y) de la célula a actualizar.
            nuevo_estado: El nuevo valor de estado (ej., 0, 1, 2, -1).
        """
        self._estado[celula] = nuevo_estado