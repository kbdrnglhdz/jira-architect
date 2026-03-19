---
name: jira_workflow_designer
description: Configurar transiciones, condiciones, validadores y post-funciones en workflows de Jira para la higiene de datos.
---

# jira_workflow_designer

## Objetivo
Diseñar el flujo de trabajo (Workflow) asegurando la robustez operativa y la higiene de los datos críticos en Jira.

## Tareas principales
- Configurar transiciones de estado, garantizando que cada estado se asigne correctamente a una categoría (To Do, In Progress, Done).
- Implementar validadores, requiriendo pantallas de validación para forzar la carga de campos en transiciones críticas.
- **Auditoría e Higiene del Dato**: Integrar reglas de validación en el Workflow para que los elementos sin cumplir con el *Definition of Ready (DoR)* (por ejemplo, carencia de Story Points, base description o WSJF) no puedan avanzar.
- Establecer condiciones y post-funciones (reglas de automatización).

## Ejemplo de uso
"Implementa un workflow para Features que requiera aprobación del PM antes de pasar a 'Ready for Dev', y asegúrate de que tiene un Definition of Ready configurado para no avanzar sin estimaciones."
