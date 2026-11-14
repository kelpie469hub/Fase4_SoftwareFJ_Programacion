# Fase4_SoftwareFJ_Programacion
Trabajo fase 4 unad

# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

## 📌 Información del curso
- **Curso:** Programación (213023)
- **Fase:** 4 – Componente práctico
- **Programa:** Ingeniería de ELECTRONICA – UNAD
- **Integrantes:** GERMAN ALBEIRO CAMARGO ZAMBRANO, MONICA TATIANA SAENZ SANTAMARIA

## 📖 Descripción del proyecto
Aplicación orientada a objetos (sin base de datos) que gestiona clientes, servicios (reservas de salas, alquiler de equipos, asesorías) y reservas. Implementa abstracción, herencia, polimorfismo, encapsulación y manejo avanzado de excepciones con registro en archivo de logs.

## 🏗️ Arquitectura y clases principales
- `Entidad` (clase abstracta base)
- `Cliente` (encapsulación y validaciones)
- `Servicio` (abstracta) → `ServicioReservaSalas`, `ServicioAlquilerEquipos`, `ServicioAsesoriaEspecializada`
- `Reserva` (estados: PENDIENTE, CONFIRMADA, CANCELADA, PROCESADA)
- Excepciones personalizadas: `ValidacionError`, `ServicioNoDisponibleError`, etc.
- Registro de logs en `logs/software_fj.log`

## 🚀 Cómo ejecutar
1. Clona el repositorio.
2. Ejecuta `python src/main.py`.
3. Revisa el archivo `logs/software_fj.log` para ver los eventos y errores registrados.

## 🧪 Simulación incluida
El script `main.py` ejecuta **más de 10 operaciones** (válidas e inválidas) que demuestran la robustez del sistema: clientes con datos incorrectos, servicios no disponibles, reservas con duración inválida, operaciones no permitidas, cálculos con impuestos/descuentos, etc.

## 📂 Estructura del repositorio
