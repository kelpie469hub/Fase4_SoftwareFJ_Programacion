from abc import ABC, abstractmethod
from src.excepciones import DatoInvalidoError

# Clase Abstracta y Cliente
# Archivo: src/entidades.py

class EntidadBase(ABC):
    """Clase abstracta general del sistema."""
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

    @abstractmethod
    def obtener_detalles(self):
        """Método abstracto que obliga a las clases hijas a implementar."""
        pass


class Cliente(EntidadBase):
    """Clase Cliente con encapsulación y validaciones estrictas."""
    
    def __init__(self, id_cliente, nombre, correo, telefono):
        super().__init__(id_cliente)
        self._nombre = None
        self._correo = None
        self._telefono = None
        
        # Usamos los setters para aplicar las validaciones
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # --- Propiedades y Validaciones (Encapsulación) ---
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise DatoInvalidoError("El nombre del cliente no puede estar vacío.")
        if not valor.replace(" ", "").isalpha():
            raise DatoInvalidoError("El nombre solo debe contener letras.")
        self._nombre = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not valor or "@" not in valor or "." not in valor:
            raise DatoInvalidoError(f"El correo '{valor}' no es válido. Debe contener @ y un dominio.")
        self._correo = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not valor or not valor.isdigit() or len(valor) < 7:
            raise DatoInvalidoError(f"El teléfono '{valor}' no es válido. Debe tener al menos 7 dígitos numéricos.")
        self._telefono = valor

    def obtener_detalles(self):
        return f"Cliente [{self._id_entidad}] - Nombre: {self._nombre}, Correo: {self._correo}, Tel: {self._telefono}"
    import datetime
from src.servicios import Servicio
from src.excepciones import ReservaInvalidaError

class Reserva(EntidadBase):
    """Clase que integra un Cliente, un Servicio, duración y estado."""
    
    def __init__(self, id_reserva, cliente, servicio, duracion_horas):
        super().__init__(id_reserva)
        
        # Validaciones básicas antes de crear la reserva
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("El cliente proporcionado no es válido.")
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("El servicio proporcionado no es válido.")
        if duracion_horas <= 0:
            raise ReservaInvalidaError("La duración de la reserva debe ser mayor a cero.")
            
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "Pendiente" # Estados posibles: Pendiente, Confirmada, Cancelada, Procesada

    def confirmar(self):
        """Confirma la reserva si está pendiente."""
        if self.estado != "Pendiente":
            raise ReservaInvalidaError(f"No se puede confirmar una reserva en estado '{self.estado}'.")
        self.estado = "Confirmada"
        return f"Reserva {self._id_entidad} confirmada exitosamente."

    def cancelar(self):
        """Cancela la reserva."""
        if self.estado == "Cancelada":
            raise ReservaInvalidaError("La reserva ya se encuentra cancelada.")
        self.estado = "Cancelada"
        return f"Reserva {self._id_entidad} cancelada."

    def procesar(self, impuesto=0.0, descuento=0.0):
        """Procesa la reserva calculando el costo final."""
        if self.estado != "Confirmada":
            raise ReservaInvalidaError("Solo se pueden procesar reservas en estado 'Confirmada'.")
        
        # Llamamos al método calcular_costo del servicio (Polimorfismo en acción)
        costo_final = self.servicio.calcular_costo(self.duracion_horas, impuesto, descuento)
        self.estado = "Procesada"
        return costo_final

    def obtener_detalles(self):
        return (f"Reserva [{self._id_entidad}] - Estado: {self.estado}\n"
                f"  -> {self.cliente.obtener_detalles()}\n"
                f"  -> Servicio: {self.servicio.describir_servicio()}\n"
                f"  -> Duración: {self.duracion_horas} horas")