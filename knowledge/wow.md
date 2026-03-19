# Way of Working (WoW) - Proyecto WS

Bienvenidos a la documentación base que rige el "Way of Working" para el proyecto **WS**. Como Arquitecto del WoW, mi responsabilidad es asegurar que la infraestructura, los esquemas y las operativas del proyecto sigan las directrices de Diseño por Gobernanza.

## Directrices Principales
1. **Nomenclatura (Naming Convention):** Todos los elementos personalizados llevarán el prefijo `WS: `.
2. **Minimalismo en Permisos:** Aplicamos el principio de menor privilegio, usando *Roles* en lugar de usuarios individuales.
3. **Integridad del Flujo y Calidad (Data Guardian):** Obligación de cumplir el DoR y validaciones en las transiciones de estados (To Do -> In Progress -> Done).

## Índice Temático

1. [Gestión de Identidad, Grupos y Roles](./usuarios_grupos_roles_permisos.md)
   - *Detalles sobre la política de accesos y la auditoría de usuarios del proyecto WS.*
2. [Blueprint Arquitectónico y Tipos de Incidencias](./ws_blueprint_estructural.md)
3. [Workflows y Diseño para Higiene de Datos](./ws_workflows_higiene.md)
4. [Metodologías Ágiles y Tableros](./ws_metodologias_agiles.md)
5. [Ecosistema e Integraciones MCP](./ws_integraciones_ecosistema.md)

---
**Resultado del Setup Initial:** El proyecto `WS` cuenta ahora con una infraestructura de gobernanza completa, auditada y lista para escalar.
