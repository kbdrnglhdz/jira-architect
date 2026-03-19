# Building Blocks: Elementos Estructurales Base de Jira

Este documento es una guía paso a paso para crear de forma manual los cimientos ("ladrillos") de la arquitectura de tu proyecto en Jira. Estos elementos representan la estructura de datos pura antes de ser sometidos a validaciones de proceso (*workflows*) o integrarse dentro de un esquema complejo.

*(Nota: Aunque estos elementos pueden crearse vía API, conocer su ubicación en la UI de Jira es clave para el rol de WoW Architect al debugear o hacer mantenimiento).*

---

## 1. Tipos de Incidencias (Issue Types)

Un *Issue Type* define "qué se está reportando" (ej. un Bug, una Tarea, un Epic o un Incidente de Producción).

### Paso a paso:
1. Navega a **Configuración de Jira (⚙️) > Problemas (Issues)**.
2. En la barra lateral izquierda, selecciona **Tipos de incidencias (Issue types)**.
3. Haz clic en el botón superior derecho **Añadir tipo de incidencia (Add issue type)**.
4. Rellena el formulario:
   - **Nombre:** Usa tu prefijo de gobernanza si aplica (ej. `WS: Incidente de Producción`).
   - **Descripción:** Explica la finalidad del tipo de incidencia para que los usuarios (y otros admins) sepan cuándo usarlo.
   - **Tipo:** Selecciona si es una Tarea Estándar (`Standard Issue Type`) o una Sub-tarea (`Sub-task`).
   *Nota: La jerarquía Epic se maneja mediante el Issue Type predeterminado Epic.*
5. Haz clic en **Añadir (Add)** y tu nuevo tipo de incidencia se añadirá al inventario global de Jira.

---

## 2. Campos Personalizados (Custom Fields)

Los *Custom Fields* albergan la data que recolectas al crear o editar el ticket. Es imperativo evitar la duplicidad de campos (por ejemplo, tener dos campos llamados "Fecha de inicio").

### Paso a paso:
1. Ve a **Configuración de Jira (⚙️) > Problemas (Issues)**.
2. Selecciona **Campos personalizados (Custom fields)** en el panel izquierdo.
3. Haz clic en **Añadir campo personalizado (Create custom field)** en la esquina superior derecha.
4. Elige el **Tipo de campo** adecuado según tu necesidad de *Higiene de Datos* (Data Guardian):
   - *Texto simple:* Si quieres que el usuario detalle (ej: `WS: Servicio Afectado`).
   - *Selector único / Múltiple:* Si necesitas obligarlo a escoger de un catálogo para mejorar la consistencia métrica (ej: `WS: Impacto`).
   - *Selector de Fecha y Hora:* (ej: `WS: SLA Deadline`).
5. Tras seleccionar el tipo de campo y dar a **Siguiente**, proporciona:
   - **Nombre:** Siguiendo tu estructura (ej. `WS: Impacto`).
   - **Descripción:** (Opcional, pero muy recomendado) Instrucciones en pantalla para guiar al usuario que va a llenarlo.
6. Clic en **Crear (Create)**.
7. La siguiente pantalla te pedirá asociar el campo a una *Pantalla (Screen)* actual. Puedes optar por vincularlo inmediatamente marcando las casillas, pero como mejor práctica, **no lo asocies todavía si vas a crear una pantalla desde cero**. Solo baja al fondo y dale a Actualizar.

---

## 3. Pantallas (Screens) y Pestañas (Tabs)

Las Pantallas son las vistas donde los Campos Personalizados (Custom Fields) y de Sistema (System Fields) se le muestran al usuario para que deposite la información.

### Creación de una Pantalla (Screen):
1. Ve a **Configuración de Jira (⚙️) > Problemas (Issues) > Pantallas (Screens)**.
2. Haz clic en **Añadir pantalla (Add screen)**.
3. Asigna un nombre claro y estructurado (ej. `WS: Pantalla de Incidente de Producción`).
4. Añade una descripción y presiona **Añadir (Add)**.

### Organización y Creación de Pestañas (Tabs):
Crear múltiples Pestañas (Tabs) dentro de una pantalla mejora radicalmente la Experiencia de Usuario, subdividiendo el formulario grande en pestañas temáticas.
1. Haz clic en la pantalla que acabas de crear (esto te llevará a la interfaz de edición/mapeo de campos).
2. De manera predeterminada existirá una pestaña principal (la puedes re-nombrar a *Detalles Generales*).
3. Para agregar una pestaña adicional (ej: *Resolución* o *Información Técnica*), dirígete al botón gris **Añadir Pestaña (Add tab)** justo al lado de las pestañas existentes.
4. Escribe el nombre de tu nueva pestaña y haz clic en **Añadir (Add)**.

---

## 4. Mapeo (Wiring Fino) de Campos dentro de las Pantallas

Ahora debes insertar los Campos Personalizados globales en tu pantalla para hacerla funcional y acomodarlos en el lugar o pestaña correcto.

### Paso a paso:
1. Posiciónate en la Pantalla (`WS: Pantalla de Incidente de Producción`) desde el editor general (**Configuración > Problemas > Pantallas** y clic en la pantalla).
2. Selecciona la pestaña en la que deseas trabajar haciendo clic encima (ej. *Detalles Generales*).
3. Ve a la parte baja de la lista en la barra de búsqueda "**Seleccionar campo... (Select Field...)**".
4. Escribe o selecciona del menú desplegable el nombre de los campos del sistema o los custom fields que quieras agregar (ej. `Summary`, `Description`, `Reporter`, `WS: Impacto`, `WS: Urgencia`).
5. Una vez en la lista, puedes arrastrar con el mouse los campos de arriba hacia abajo para darles un **orden lógico visual** que el usuario de deba seguir.
6. A continuación, cambia de pestaña haciendo clic arriba (ej. selecciona la pestaña *Diagnóstico y Prevención*) y repite la operación para buscar y agregar campos técnicos (ej. `WS: Causa Raíz Inicial`, `WS: Workaround`).

> **📌 Siguiente Fase de Arquitectura:**
> ¡Tus ladrillos de datos ya están creados y empaquetados en una Pantalla Funcional! 
> Sin embargo, la pantalla por sí sola está flotando en el archivo global de Jira. Para hacer que salte cuando selecciones ese Issue Type en tu Proyecto particular, deberás **cablear los esquemas**, tal como se detalla en el documento `wiring_structural.md`.
