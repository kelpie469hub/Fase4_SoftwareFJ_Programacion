import logging
import os


# Registro de Eventos (Logs)
# Archivo: src/logger.py

# Aseguramos que la carpeta 'logs' exista
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configuramos el logger
logger = logging.getLogger('SoftwareFJ')
logger.setLevel(logging.INFO)

# Formato del mensaje: Fecha - Tipo (INFO/ERROR) - Mensaje
formato = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Guardar en el archivo logs/eventos.log
archivo_handler = logging.FileHandler('logs/eventos.log', encoding='utf-8')
archivo_handler.setFormatter(formato)

# Mostrar también en la consola
consola_handler = logging.StreamHandler()
consola_handler.setFormatter(formato)

logger.addHandler(archivo_handler)
logger.addHandler(consola_handler)

def registrar_evento(mensaje):
    """Función para registrar eventos normales."""
    logger.info(mensaje)

def registrar_error(mensaje):
    """Función para registrar errores."""
    logger.error(mensaje)