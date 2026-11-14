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