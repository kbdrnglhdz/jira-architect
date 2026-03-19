# Wiring Estructural de Jira (Vía Interfaz de Usuario)

Este documento sirve como "receta de cocina" para configurar todos los elementos estructurales y de comportamiento lógico de Jira que no pueden ser automatizados robustamente de manera nativa utilizando la API REST o herramientas de scripting (MCP Atlassian).

Se divide fundamentalmente en dos desafíos que, como *WoW Architect*, deberás realizar a mano a través de la interfaz de administración global: **La lógica profunda de los Workflows** y **el mapeo final de los Esquemas de Pantallas a un proyecto vivo**.

---

## Parte 1: Creación de Workflows con Higiene de Datos (Data Guardian) desde Cero

Un Workflow robusto en Jira no es solo un mapa de estados visual; está diseñado para frenar transiciones ilógicas y mantener la higiene de datos a través del uso de Condiciones, Validadores y Post-funciones.

### Paso 1.1: Inicializar el Workflow Base
1. Ingresa a **Configuración de Jira (⚙️) > Problemas (Issues)**.
2. En el menú lateral izquierdo, haz clic en **Flujos de trabajo (Workflows)**.
3. Haz clic en el botón superior derecho **Añadir flujo de trabajo (Add workflow)** para iniciar uno desde cero.
4. Nombra el flujo de trabajo obedeciendo las directrices estrictas de nomenclatura (e.g., `WS: Producción Incident Workflow`).

### Paso 1.2: Definir Estados y Transiciones
1. Asegúrate de estar trabajando en la vista de **Diagrama (Diagram)**.
2. Haz clic en **Añadir estado (Add status)** para incorporar todos los pasos de tu ciclo de vida (ej. *To Do*, *Revisión*, *Done*). Asegúrate que cada Estado encaje correctamente en las categorías básicas de Jira (Gris, Azul, Verde).
3. Agrega **Transiciones (Transitions)** conectando un estado con otro y nombrando la acción. (Evita usar "Cualquier estado a sí mismo" en procesos muy controlados).

### Paso 1.3: Higiene de Datos (Data Guardian) - Implementar Validadores
*Los validadores impiden que el ticket cambie de estado si no se cumple una regla específica.*
1. En el editor de Diagrama, haz clic encima de la línea que representa tu transición crítica (Ej. De *In Progress* a *Done*).
2. En el menú derecho, haz clic en **Validadores (Validators)**.
3. Haz clic en **Añadir validador (Add validator)**.
4. Escoge **Field Required Validator** (o el validador equivalente si tienes plugins como ScriptRunner o JMWE).
5. Selecciona los campos que creaste previamente vía API que **deben** estar llenos antes de cerrar (Ej. `WS: Impacto`, `WS: Causa Raíz Inicial`). Ahora, el usuario recibirá un error de bloqueo en pantalla si dichos campos están en blanco.

### Paso 1.4: Configurar Elementos Adicionales en la Transición
1. **Pantallas de Transición (Transition Screens):** Para que el usuario pueda llenar los campos obligatorios del Validador mientras transita, ve a la transición deseada de tu diagrama, presiona **Editar (Edit)** y en el desplegable de **Pantalla (Screen)**, conéctala con tu pantalla (Ej. `WS: Transition Screen - DoR Validation`).
2. **Post-funciones:** Haz clic en **Post Functions**. Aquí debes añadir integraciones u operaciones que Jira hará a las espaldas del usuario tras ocurrir la transición. Ejemplo: *Limpiar la resolución si el ticket vuelve a Open*.
3. **Draft y Publicar:** Los Workflows no se guardan solos, al final haz clic en **Publicar borrador (Publish Draft)**.

---

## Parte 2: Cableado (Wiring) de Esquemas en un Proyecto Vivo

Acabas de usar la API para crear Custom Fields y Pantallas (Screens), pero eso no es suficiente. Hay que decirle a Jira "dónde, cuándo y para quién" mostrar esas pantallas y flujos de trabajo en un proyecto específico, ensamblando las capas del sándwich metodológico.

### Paso 2.1: Crear el Screen Scheme (Esquema de Pantalla)
*Define qué pantalla se usa para las operaciones de Crear, Editar o Ver de manera neutral, sin vincular a un ticket particular todavía.*
1. Ve a **⚙️ Configuración > Problemas > Esquemas de pantallas (Screen schemes)**.
2. Clic en **Añadir esquema de pantalla (Add screen scheme)**.
3. Asígnale el nombre (ej. `WS: Incidentes Screen Scheme`) y selecciona en el menú tu **Default Screen** (la pantalla que diseñaste para incidentes).
4. Guardar. *(Opcional: Si necesitas que cuando alguien Edite un bug salgan campos diferentes a cuando lo Crea, edita este esquema y asocia "Edit Issue" con otra pantalla).*

### Paso 2.2: Actualizar el Issue Type Screen Scheme (Asignación Final a Nivel Proyecto)
*Atribuye los Esquemas de Pantallas a los Tipos de Incidencias que viven dentro del proyecto.*
1. Ve a **⚙️ Configuración > Problemas > Esquemas de pantalla de tipo de incidencia (Issue type screen schemes)**.
2. Encuentra el que pertenece a tu proyecto (Normalmente nombrado `WS: Scrum Issue Type Screen Scheme` o entra al de tu proyecto para editar en vivo). **Edítalo**.
3. Haz clic en el botón superior **Asociar un tipo de incidencia a un esquema de pantalla (Associate an issue type with a screen scheme)**.
4. Elige el Issue Type que creaste (ej. `Incidente de Producción`).
5. Elige el Screen Scheme que configuraste en el Paso 2.1. Guardar.

### Paso 2.3: Actualizar el Workflow Scheme (Asignación del Flujo)
*Le dice al proyecto qué Workflow usar de acuerdo al tipo de ticket en particular.*
1. Ve a **⚙️ Configuración > Problemas > Esquemas de flujo de trabajo (Workflow schemes)**.
2. Localiza el esquema activo de tu proyecto y pulsa en **Editar**.
3. Haz clic en **Añadir flujo de trabajo > Añadir un flujo existente (Add workflow > Add existing)**.
4. Selecciona tu nuevo Workflow de Data Guardian (Paso 1).
5. Se mostrará una ventana preguntando para qué Issue Types aplica. Selecciona los tipos correctos (ej. `Incidente de Producción`).
6. Presiona **Publicar**.

### Paso 2.4: Permutar el Esquema de un Proyecto (Opcional si decidiste no editar los del proyecto activo)
Si en lugar de usar los *Schemes* activos de un proyecto por diseño generaste esquemas desde cero y ahora necesitas "conectar el encendedor":
1. Dirígete a las configuraciones locales de tu proyecto en Jira.
2. Ve a la barra lateral en **Pantallas (Screens)** o en **Flujo de Trabajo (Workflows)**.
3. Busca el menú de opciones (A través del botón `Acciones` ubicado habitualmente a la derecha).
4. Elige **Usar otro esquema (Use a different scheme)** y migra tu proyecto a los nuevos esquemas creados. Esto disparará un pequeño task de migración nativo de Jira para realinear tickets antiguos a las nuevas reglas.
