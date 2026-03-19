---
name: jira_blueprint_architect
description: Definir Issue Types (Epics, Features, Stories), campos personalizados y esquemas de pantallas.
---

# jira_blueprint_architect

## Objetivo
Orquestar y establecer la arquitectura de tickets (jerarquía y campos) de los proyectos en Jira respetando la convención de nombres y el ciclo de vida general.

## Tareas principales
- Crear la jerarquía de `Issue Types` necesaria (por ejemplo, para SAFe: Portfolio Epic > Solution Capability > Feature > Story).
- Configurar campos personalizados, asegurando el formato `[PROYECTO_KEY]: [Nombre]` para evitar duplicidad de campos globales.
- Integrar la validación y **gestión de esquemas compartidos**: evaluar siempre el impacto en otros proyectos antes de alterar un esquema existente, reduciendo "fatiga de configuración".
- Configurar esquemas de pantallas vinculando campos solo en las transiciones y vistas necesarias.

## Ejemplo de uso
"Crea la jerarquía de tickets necesaria para SAFe (Portfolio Epic > Solution Capability > Feature > Story)."
