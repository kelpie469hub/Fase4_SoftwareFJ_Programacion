from abc import ABC, abstractmethod
from src.excepciones import DatoInvalidoError

# Clase Abstracta Servicio y Clases Derivadas
# Archivo: src/servicios.py

class Servicio(ABC):
    """Clase abstracta que representa un servicio general de Software FJ."""
    
    def __init__(self, id_servicio, nombre, costo_base):
        if costo_base <= 0:
            raise DatoInvalidoError("El costo base debe ser mayor a cero.")
        self._id_servicio = id_servicio
        self._nombre = nombre
        self._costo_base = costo_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_base(self):
        return self._costo_base

    @abstractmethod
    def calcular_costo(self, duracion_horas, *args, **kwargs):
        """Método abstracto para calcular el costo. Será diferente en cada servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Método abstracto para describir el servicio."""
        pass


class ReservaSala(Servicio):
    def __init__(self, id_servicio, nombre, costo_base, capacidad_personas):
        super().__init__(id_servicio, nombre, costo_base)
        self.capacidad_personas = capacidad_personas

    def calcular_costo(self, duracion_horas, impuesto=0.0, descuento=0.0):
        """Sobrecarga de método: calcula el costo con impuestos y descuentos opcionales."""
        if duracion_horas <= 0:
            raise DatoInvalidoError("La duración debe ser mayor a cero.")
            
        subtotal = self._costo_base * duracion_horas
        total_con_impuesto = subtotal + (subtotal * impuesto)
        total_final = total_con_impuesto - (total_con_impuesto * descuento)
        return total_final

    def describir_servicio(self):
        return f"Reserva de Sala '{self._nombre}' (Capacidad: {self.capacidad_personas} personas)."


class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre, costo_base, tipo_equipo):
        super().__init__(id_servicio, nombre, costo_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, duracion_horas, impuesto=0.0, descuento=0.0):
        # Los equipos tienen un recargo extra del 10% por mantenimiento
        subtotal = (self._costo_base * duracion_horas) * 1.10
        total_con_impuesto = subtotal + (subtotal * impuesto)
        total_final = total_con_impuesto - (total_con_impuesto * descuento)
        return total_final

    def describir_servicio(self):
        return f"Alquiler de Equipo '{self._nombre}' (Tipo: {self.tipo_equipo})."


class AsesoriaEspecializada(Servicio):
    def __init__(self, id_servicio, nombre, costo_base, area_especialidad):
        super().__init__(id_servicio, nombre, costo_base)
        self.area_especialidad = area_especialidad

    def calcular_costo(self, duracion_horas, impuesto=0.0, descuento=0.0, es_urgente=False):
        # Sobrecarga: Si es urgente, se cobra un 20% extra
        subtotal = self._costo_base * duracion_horas
        if es_urgente:
            subtotal = subtotal * 1.20
            
        total_con_impuesto = subtotal + (subtotal * impuesto)
        total_final = total_con_impuesto - (total_con_impuesto * descuento)
        return total_final

    def describir_servicio(self):
        return f"Asesoría Especializada '{self._nombre}' (Área: {self.area_especialidad})."