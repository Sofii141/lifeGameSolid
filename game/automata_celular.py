from abc import ABC, abstractmethod
from typing import Tuple, Dict, Any

# Importaciones de Abstracciones (Interfaces) 
from .vecindad.i_estrategia_vecindad import IEstrategiaVecindad 
from .frontera.i_condicion_frontera import ICondicionFrontera
from .lattice.i_lattice import ILattice 

class AutomataCelular(ABC):
    """
    Clase base abstracta que define el contrato de un Autómata Celular (AC).
    
    Esta clase implementa la lógica común a todos los AC y solo depende de 
    Abstracciones (Interfaces) para sus componentes principales (Vecindad, 
    Frontera, Lattice).
    """

    def __init__(self, ocupacion_inicial: float, 
                 estrategia_vecindad: IEstrategiaVecindad, 
                 condicion_frontera: ICondicionFrontera, 
                 lattice: ILattice,
                 dimensiones: Tuple[int, int]): 
        """
        Constructor que recibe todas las dependencias requeridas y las inyecta.
        
        Args:
            ocupacion_inicial: Probabilidad inicial de que una célula esté viva.
            estrategia_vecindad: Objeto que implementa la lógica de vecindad (IEstrategiaVecindad).
            condicion_frontera: Objeto que implementa la lógica de borde (ICondicionFrontera).
            lattice: Objeto que almacena el estado del lattice (ILattice).
            dimensiones: Tamaño (X_MAX, Y_MAX) del Lattice para su inicialización.
        """
        
        self.ocupacion_inicial = ocupacion_inicial
        
        # Dependencias (Contratos/Abstracciones) - La clase SÓLO conoce las interfaces.
        self.estrategia_vecindad = estrategia_vecindad 
        self.condicion_frontera = condicion_frontera 
        
        # Inicialización del Lattice (Le pide al Lattice inyectado que se inicialice)
        # La clase AutomataCelular NO almacena 'self.dimensiones', las obtiene de ILattice.
        self.lattice: ILattice = lattice
        self.lattice.inicializar(dimensiones, ocupacion_inicial) 

    @abstractmethod
    def avanzar_generacion(self):
        """
        Método abstracto que define la Regla de Transición Local.
        
        Debe ser implementado por cualquier subclase concreta (ej., JuegoDeLaVida)
        para definir su lógica de evolución específica.
        """
        pass
            
    def obtener_lattice(self) -> ILattice:
        """
        Método de acceso para obtener la abstracción del lattice (ILattice).
        
        Returns:
            La instancia de ILattice inyectada.
        """
        return self.lattice