# 3. Workflows y Diseño para Higiene de Datos (Proyecto WS)

**Principio de diseño:** Integridad del flujo. Cada estado debe tener una categoría clara y las transiciones críticas deben validar que el dato sea de alta calidad.

En el proyecto **WS**, el flujo de trabajo no es solo un camino de estados, sino una barrera de control para garantizar que la información que llega a "Done" sea veraz y útil para las métricas de negocio.

## Estructura del Workflow WS

Utilizamos un flujo estándar adaptado con políticas de **Data Guardian**:

1. **To Do (Categoría: Por hacer)**
   - *Estado inicial*: El ticket ha sido creado pero no cumple necesariamente con el **DoR (Definition of Ready)**.
   - *Regla*: No se debe asignar tiempo ni recursos hasta que el ticket sea refinado.

2. **In Progress (Categoría: En curso)**
   - *Transición Crítica (Start Progress)*: Al mover un ticket a este estado, el sistema (Agente) valida que el ticket tenga un **Asignado (Assignee)** y que la **Justificación de Negocio** sea coherente.
   - *WIP Limits*: Se recomienda no tener más de 3 tareas por desarrollador en este estado para evitar cuellos de botella.

3. **Done (Categoría: Listo)**
   - *Transición de Cierre (Resolve)*: Solo se permite si se ha cumplido el **DoD (Definition of Done)**.
   - *Higiene del Dato*: El cierre de un ticket dispara automáticamente una auditoría de campos (ej. si se logueó el tiempo trabajado si el proyecto lo requiere).

## Demostración de Transición (Higiene en Vivo)

Acabamos de realizar una transición sobre el ticket **WS-1**. 
- **Acción**: Movimiento de "To Do" a "In Progress".
- **Validación**: El agente verificó la existencia de la justificación de negocio antes de proceder.
- **Resultado**: El estado del ticket ha sido actualizado exitosamente, permitiendo ahora la trazabilidad del esfuerzo.

---
*Nota: En configuraciones avanzadas, añadiremos pantallas de transición (Transition Screens) para obligar al usuario a llenar campos como "Causa raíz" en bugs o "Lecciones aprendidas" en tareas complejas.*
