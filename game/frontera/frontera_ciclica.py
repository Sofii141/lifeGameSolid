from .i_condicion_frontera import ICondicionFrontera

class CondicionFronteraCiclica(ICondicionFrontera):
    """
    Implementación concreta de Condición de Frontera Cíclica.
    
    Esta clase implementa la lógica donde los bordes opuestos del Lattice están 
    conectados (ej., una célula que se sale por el lado derecho aparece por el izquierdo).
    """
    
    def obtener_coordenada_real(self, coordenada_deseada: int, dimension_maxima: int) -> int:
        """
        Calcula la coordenada real utilizando la operación módulo.
        
        Si la coordenada se sale por encima o por debajo de los límites [0, dimension_maxima - 1],
        la operación módulo (%) la envuelve al lado opuesto.
        
        Args:
            coordenada_deseada: La coordenada propuesta por la Vecindad.
            dimension_maxima: El tamaño máximo del eje (ej. ancho o alto).
            
        Returns:
            La coordenada real ajustada por la regla cíclica.
        """
        # La operación módulo (%) se encarga de manejar tanto los valores
        # positivos (que se salen del límite superior) como los negativos 
        # (que se salen del límite inferior) en Python.
        return coordenada_deseada % dimension_maxima