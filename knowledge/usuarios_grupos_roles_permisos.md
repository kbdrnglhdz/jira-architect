# 1. Gestión de Identidad, Grupos y Roles (Proyecto WS)

**Principio de diseño:** Minimalismo de permisos. No asocies permisos ni notificaciones a usuarios (ej: `juan.perez`) ni a grupos globales (`jira-software-users`) sin un análisis previo. 

Para manejar el esquema de permisos y notificaciones en el proyecto **WS**, utilizamos la gestión basada en **Roles del Proyecto**.

## Estrategia de Roles para WS

En Jira, el proyecto `WS` utilizará los roles por defecto con un propósito estricto:

1. **WS: Administrators (Administrators)**: 
   - *Descripción*: Capacidad de editar componentes, versiones y administrar configuraciones de tablero (Board).
   - *Usuarios*: Product Owners Core / Scrum Masters.
2. **WS: Developers (Developers)**: 
   - *Descripción*: Capacidad de transicionar incidencias, loguear horas (Worklogs) y asignar tareas.
   - *Usuarios*: Miembros del Dev Team.
3. **WS: Viewers (Users/Browsers)**: 
   - *Descripción*: Modo lectura. Capacidad para ver el progreso sin alterar data (para asegurar la higiene del dato).
   - *Usuarios*: Stakeholders y management.

## Demostración y Auditoría Actual

*En este paso, el agente MCP Atlassian procede a inspeccionar la data existente en el proyecto WS (como componentes y tickets activos) para detectar quiénes están operando actualmente como asignados (Assignees) y poder auditar que se estén aplicando las reglas de roles correctas.*
