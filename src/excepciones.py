
# Manejo de Excepciones
# Archivo: src/excepciones.py

class SoftwareFJError(Exception):
    """Clase base para todas las excepciones del sistema Software FJ."""
    pass

class DatoInvalidoError(SoftwareFJError):
    """Se lanza cuando un dato no cumple con las validaciones (ej. correo malo)."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un servicio no está disponible o no existe."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando hay un problema al crear o procesar una reserva."""
    pass