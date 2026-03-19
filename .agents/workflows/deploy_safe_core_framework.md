---
description: Deploy SAFe Core Framework Workflow
---

# Deploy SAFe Core Framework

Este workflow automatiza la implementación base del framework SAFe en tu entorno Jira, tomando como base las directrices (Rules) y haciendo uso de las habilidades técnicas (Skills) expandidas.

## Pasos de Ejecución

1. **Análisis Estructural y Metodológico (Skill: `agile_methodologist`):**
   - Identifica y define la jerarquía de niveles que utilizará tu proyecto (Portfolio, Large Solution, Program, Team).
   - Elige el modelo híbrido (Kanban a nivel estratégico y Scrum a nivel operativo).

2. **Configuración de Identidad (Skill: `jira_identity_manager`):**
   - Crea grupos estratégicos según el Way of Working: `SPC`, `Release Train Engineers`, `Product Management`.
   - Define los Roles de Proyecto necesarios y asocia flujos a **Roles** (Permission Minimalism) evitando la asignación a usuarios concretos.

3. **Arquitectura y Ciclo de Vida de Esquemas (Skill: `jira_blueprint_architect`):**
   - Configura Issue Types específicos (Epic > Feature > Story).
   - Crea e implementa campos personalizados (`WSJF`, `Story Points`), prefijándolos con el Project Key.
   - Aplica validación cruzada para evitar la fatiga técnica en el rediseño de esquemas para otras iniciativas.

4. **Diseño de Flujo y Control de Datos (Skills: `jira_workflow_designer`, `jira_data_guardian`):**
   - Estructura y asocia el workflow del "Continuous Delivery Pipeline".
   - Establece Validadores para exigir el estricto cumplimiento del DoR antes de transicionar tickets críticos.
   - Configura condiciones y post-funciones de automatización en transiciones de estado clave.

5. **Integración Externa y Alertas (Skill: `jira_connector`):**
   - Relaciona el flujo técnico configurando el vínculo SCM y las transiciones (e.g. In Progress a Done vía GitHub/GitLab).
   - Genera políticas de alertas directas hacia Slack/Teams, por ejemplo al notificar límites WIP vulnerados o "Features estáticas".

6. **Métricas y Auditoría Continua (Skill: `jira_data_guardian`):**
   - Elabora el marco local de monitoreo (Tableros *Velocity*, *Burndown* y *Control Charts* para métricas de "Cycle Time").
