# 2. Blueprint Arquitectónico y Tipos de Incidencias (Proyecto WS)

**Principio de diseño:** Nomenclatura Estricta (`WS: [Nombre]`) y consistencia en los Tipos de Incidencias (Issue Types) compartidos o propios.

En el proyecto **WS**, aplicaremos una taxonomía estándar que nos permita escalar sin ensuciar la instancia global de Jira. Esto aplica tanto a Tipos de Incidencia, como a campos personalizados (Custom Fields) y a esquemas de pantallas (Screen Schemes).

## Tipos de Incidencias (Issue Types)

Acorde a mi evaluación como *WoW Architect* para el ecosistema de **WS**, estructuraremos el trabajo con la siguiente jerarquía para lograr trazabilidad (cumpliendo con metodologías ágiles e híbridas):

1. **Jerarquía Nivel Portfolio (Si aplica)**
   - `WS: Initiative`: Grandes apuestas u OKRs a largo plazo.
2. **Jerarquía Nivel Programa/Proyecto**
   - `WS: Epic`: Agrupación de funcionalidades que aportan gran valor y superan un Sprint (Típicamente > 1 mes).
   - `WS: Feature` *(Opcional)*: En entornos SAFe, representa funcionalidades entregables a nivel tren (ART).
3. **Jerarquía Nivel Equipo de Trabajo (Squad)**
   - `WS: Story`: Unidad funcional que entrega valor de negocio y es abordable en un único Sprint.
   - `WS: Task`: Labores técnicas o administrativas que no aportan funcionalidad directa al negocio.
   - `WS: Bug`: Defectos o problemas sobre funcionalidades que ya estaban en producción.
4. **Sub-Tareas (Sub-tasks)**
   - `WS: Sub-task`: Desglose granular a nivel técnico para desarrollo, pruebas, UX o despliegues.

## Validación y Creación (Realizada)

A través de la integración MCP, hemos implementado la jerarquía SAFe real en el proyecto WS:

1. **Portfolio Epic**: `WS-2: Infraestructura y Gobernanza Inicial`.
2. **Program Feature**: `WS-6: [FEATURE] Continuous Delivery Pipeline Setup` (Vinculada a WS-2).
3. **Team Stories**: 
   - `WS-7: [STORY] Setup de Grupos SPC, RTE y Product Management`.
   - `WS-8: [STORY] Definir Roles de Proyecto y Permisos`.
   - `WS-9: [STORY] Implementar Validadores de Workflow (DoR/DoD)`.

Cada ticket incluye el campo obligatorio `Justificación de negocio` bajo el estándar ADF (Atlassian Document Format).
