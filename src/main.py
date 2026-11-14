# Archivo principal: Simulación del Sistema Integral Software FJ
from src.entidades import Cliente, Reserva
from src.servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from src.excepciones import DatoInvalidoError, ReservaInvalidaError, SoftwareFJError
from src.logger import registrar_evento, registrar_error

def ejecutar_simulacion():
    print("="*60)
    print(" INICIANDO SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("="*60)
    
    # ---------------------------------------------------------
    # OPERACIÓN 1: Registro válido de cliente
    # ---------------------------------------------------------
    try:
        cliente1 = Cliente("C001", "Ana Gomez", "ana@correo.com", "3001234567")
        registrar_evento("Operación 1: Cliente 'Ana Gomez' registrado correctamente.")
        print(f"\n[ÉXITO] {cliente1.obtener_detalles()}")
    except Exception as e:
        registrar_error(f"Error inesperado en Op 1: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 2: Registro inválido de cliente (Correo malo)
    # ---------------------------------------------------------
    try:
        cliente2 = Cliente("C002", "Carlos Perez", "carlos_correo_malo", "3109876543")
    except DatoInvalidoError as e:
        registrar_error(f"Operación 2 (Validación): {e}")
        print(f"\n[ERROR CONTROLADO] No se pudo crear el cliente: {e}")
    else:
        print("Cliente creado exitosamente (esto no debería imprimirse).")
    finally:
        print(" -> Finalizada validación de cliente.")

    # ---------------------------------------------------------
    # OPERACIÓN 3: Creación válida de Servicios
    # ---------------------------------------------------------
    try:
        sala = ReservaSala("S001", "Sala VIP", 50000, 10)
        equipo = AlquilerEquipo("S002", "Video Beam", 30000, "Proyector")
        asesoria = AsesoriaEspecializada("S003", "Asesoría en Python", 80000, "Programación")
        
        registrar_evento("Operación 3: 3 servicios creados correctamente.")
        print(f"\n[ÉXITO] Servicios creados:\n - {sala.describir_servicio()}\n - {equipo.describir_servicio()}\n - {asesoria.describir_servicio()}")
    except SoftwareFJError as e:
        registrar_error(f"Error creando servicios: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 4: Creación inválida de Servicio (Costo negativo)
    # ---------------------------------------------------------
    try:
        servicio_malo = ReservaSala("S004", "Sala Fantasma", -100, 5)
    except DatoInvalidoError as e:
        registrar_error(f"Operación 4 (Validación de Servicio): {e}")
        print(f"\n[ERROR CONTROLADO] No se pudo crear el servicio: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 5: Reserva exitosa y confirmación
    # ---------------------------------------------------------
    try:
        reserva1 = Reserva("R001", cliente1, sala, 3)
        print(f"\n[INFO] Creando reserva...\n{reserva1.obtener_detalles()}")
        
        mensaje = reserva1.confirmar()
        registrar_evento(f"Operación 5: {mensaje}")
        print(f"[ÉXITO] {mensaje}")
    except SoftwareFJError as e:
        registrar_error(f"Error en reserva 1: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 6: Reserva con duración inválida (Falla)
    # ---------------------------------------------------------
    try:
        reserva_mala = Reserva("R002", cliente1, equipo, -5)
    except ReservaInvalidaError as e:
        registrar_error(f"Operación 6 (Reserva fallida): {e}")
        print(f"\n[ERROR CONTROLADO] No se pudo crear la reserva: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 7: Procesar reserva exitosa (Calcula costo con polimorfismo)
    # ---------------------------------------------------------
    try:
        # Procesamos con 19% de impuesto (IVA) y 10% de descuento
        costo_total = reserva1.procesar(impuesto=0.19, descuento=0.10)
        registrar_evento(f"Operación 7: Reserva {reserva1._id_entidad} procesada. Costo: ${costo_total:,.2f}")
        print(f"\n[ÉXITO] Reserva procesada. Costo total (con IVA y desc): ${costo_total:,.2f}")
        print(f"Estado actual: {reserva1.estado}")
    except ReservaInvalidaError as e:
        registrar_error(f"Error procesando reserva: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 8: Intentar procesar una reserva ya procesada (Falla)
    # ---------------------------------------------------------
    try:
        reserva1.procesar()
    except ReservaInvalidaError as e:
        registrar_error(f"Operación 8 (Doble proceso): {e}")
        print(f"\n[ERROR CONTROLADO] {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 9: Encadenamiento de Excepciones
    # ---------------------------------------------------------
    print("\n--- Operación 9: Encadenamiento de Excepciones ---")
    try:
        try:
            # Forzamos un error de tipo para encadenarlo
            duracion = int("tres")
        except ValueError as e_original:
            # 'raise ... from ...' es el encadenamiento
            raise ReservaInvalidaError("La duración debe ser un número entero.") from e_original
    except ReservaInvalidaError as e_final:
        registrar_error(f"Operación 9 (Excepción encadenada): {e_final}. Causa original: {e_final.__cause__}")
        print(f"[ERROR CONTROLADO] {e_final}\n -> Causa raíz: {e_final.__cause__}")

    # ---------------------------------------------------------
    # OPERACIÓN 10: Cancelar reserva y demostrar que no se puede confirmar
    # ---------------------------------------------------------
    try:
        reserva2 = Reserva("R003", cliente1, asesoria, 2)
        print(f"\n[INFO] Cancelando reserva R003...")
        reserva2.cancelar()
        
        print("[INFO] Intentando confirmar reserva cancelada...")
        reserva2.confirmar()
    except ReservaInvalidaError as e:
        registrar_error(f"Operación 10 (Confirmar cancelada): {e}")
        print(f"[ERROR CONTROLADO] {e}")

    print("\n" + "="*60)
    print(" SIMULACIÓN FINALIZADA. El sistema sigue estable.")
    print(" Revisa la carpeta 'logs' para ver el archivo eventos.log")
    print("="*60)

if __name__ == "__main__":
    ejecutar_simulacion()