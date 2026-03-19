---
name: jira_connector
description: Integrar el ecosistema de herramientas mediante Model Context Protocol (MCP) para automatizar el movimiento de tickets y alertas.
---

# jira_connector

## Objetivo
Actuar como puente de sincronización e información conectando Jira con las herramientas del ecosistema usando MCP, reduciendo el trabajo manual.

## Tareas principales
- Sincronización de repositorios: Integrar y automatizar flujos con GitHub/GitLab (ej: mover tickets de "In Progress" a "Done" cuando se hace merge de un Pull Request o usar commits con el Issue Key para el pase automático).
- Notificaciones Inteligentes: Implementar alertas basadas en reglas de negocio usando Slack/Teams (ej: notificar cuando un ticket quede estancado por más de 3 días en una columna, o cuando un "WIP limit" ha sido excedido).

## Ejemplo de uso
"Configura una integración con GitHub para que las historias pasen a Resolved al hacer merge del PR y avisa a Slack si la Feature principal lleva más de 5 días bloqueada."
