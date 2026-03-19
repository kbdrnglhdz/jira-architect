# 4. Metodologías Ágiles y Tableros (Proyecto WS)

**Principio de diseño:** Trazabilidad escalable. El trabajo debe estar organizado en una jerarquía que permita ver desde el detalle técnico hasta el valor de negocio.

En el proyecto **WS**, adoptamos un enfoque híbrido que permite la agilidad del equipo (Scrum/Kanban) manteniendo la alineación con el Portfolio (SAFe).

## Estructura del Backlog

Para garantizar un flujo de valor constante, el backlog de WS se organiza bajo las siguientes reglas:

1. **Jerarquía Top-Down**:
   - **Epic**: Define el "Qué" y el "Por qué" a alto nivel.
   - **Story/Task**: Define el "Cómo" a nivel de implementación.
   - *Regla de Oro*: Ninguna Historia de Usuario (Story) debe existir sin estar vinculada a un Epic padre.

2. **Gestión de Sprints (Scrum)**:
   - Los Sprints en WS tienen una duración recomendada de 2 semanas.
   - **Definition of Ready (DoR)**: Antes de entrar a un Sprint, la historia debe tener Estimación, Criterios de Aceptación y Justificación de Negocio.

3. **Flujo de Valor (Kanban)**:
   - El tablero visual de WS debe reflejar fielmente el workflow (To Do -> In Progress -> Done).
   - Se monitorean métricas como el **Cycle Time** y el **Lead Time** para identificar desperdicios en el proceso.

## Estado Actual del Backlog (SAFe Implementation)

Se ha ejecutado la estructura jerárquica en el proyecto WS:
1. **Epic (Portfolio)**: `WS-2: Infraestructura y Gobernanza Inicial`.
2. **Feature (Program)**: `WS-6: [FEATURE] Continuous Delivery Pipeline Setup`.
3. **Stories (Team)**: Vinculadas a la Feature WS-6, asegurando que no existan tareas "huérfanas".

**Métricas Operativas Entrantes:**
- Se han habilitado campos para **WSJF** y **Story Points**.
- El Agente audita que cada historia tenga su `Justificación de negocio` antes de ser transicionada.
