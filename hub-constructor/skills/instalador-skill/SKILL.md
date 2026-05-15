---
name: instalador-skill
description: >
  Instala una skill de la comunidad con verificación de fuente, inspección del contenido
  y confirmación explícita del usuario antes de proceder. Nunca instala sin aprobación.
argument-hint: "[nombre-skill o URL de la skill a instalar]"
user-invocable: true
---

# Skill: Instalador de Skills de la Comunidad

## Propósito

Descubrimiento e instalación segura de skills de la comunidad. Aplica un trust gate real:
verifica la fuente, muestra el contenido completo para revisión y solicita confirmación explícita
antes de instalar cualquier cosa en el entorno.

---

## Paso 0 — Identificación de la skill

1. **Nombre o URL**: ¿cuál es el nombre o la URL de la skill a instalar?
2. **Plugin destino**: ¿en qué plugin se instalará? (ej. `civil-comercial`, `laboral`)
3. **Fuente**: ¿de dónde proviene? (repositorio oficial, fork, otra URL)

---

## Paso 1 — Verificación de fuente

Comparar la fuente indicada con la lista de fuentes confiables en `CLAUDE.md`:

- **Fuente confiable**: continuar al Paso 2.
- **Fuente no listada**:

  ```
  ⚠️ ADVERTENCIA: Esta skill proviene de una fuente no verificada.
  Fuente: [URL/repositorio indicado]
  Instalación desde fuentes no verificadas puede introducir contenido no revisado.

  ¿Querés continuar bajo tu responsabilidad? (sí / no)
  ```

  Si el usuario confirma: advertir nuevamente y solicitar segunda confirmación explícita.

---

## Paso 2 — Inspección del contenido

Mostrar el contenido completo de la skill:

```
--- CONTENIDO DE LA SKILL ---
[frontmatter YAML completo]
[cuerpo del SKILL.md]
--- FIN DEL CONTENIDO ---
```

Luego verificar:

- ¿El frontmatter tiene los campos requeridos (`name`, `description`, `user-invocable`)?
- ¿La descripción supera los 1024 caracteres? Si sí: alertar.
- ¿El contenido contiene instrucciones de ejecución de código o acceso a sistemas externos? Si sí: alerta específica.

---

## Paso 3 — Alerta de permisos (si aplica)

Si la skill referencia herramientas de shell, escritura fuera del directorio del plugin,
o acceso a red no estándar:

```
🔴 ALERTA DE PERMISOS: Esta skill solicita acceso a [herramienta/recurso].
Esto requiere aprobación del administrador del sistema antes de instalar.
```

No continuar hasta obtener esa aprobación.

---

## Paso 4 — Confirmación explícita

```
Para confirmar la instalación, escribí exactamente:
CONFIRMO INSTALAR [nombre-skill] EN [plugin-destino]
```

No instalar si la respuesta no coincide exactamente con la frase requerida.

---

## Paso 5 — Instalación

Copiar el archivo al directorio correcto:
`{plugin-destino}/skills/{nombre-skill}/SKILL.md`

---

## Paso 6 — Verificación post-instalación

Confirmar que:
- El archivo existe en la ruta correcta.
- El frontmatter YAML es válido.
- El `name` en el frontmatter coincide con el nombre del directorio.

Registrar la instalación: nombre de skill, fuente, fecha, usuario que aprobó.

```
✅ Instalación completada.
Skill: [nombre]
Plugin: [plugin-destino]
Ruta: [ruta completa]
Fuente: [URL/repositorio]
```

---

## Guardrails

- NUNCA instalar sin la confirmación explícita del Paso 4.
- NUNCA instalar desde fuentes no verificadas sin la doble advertencia y doble confirmación.
- Si la skill contiene código ejecutable (no solo markdown con instrucciones), detener y escalar al administrador.
- Si la fuente es una URL directa (no un repositorio conocido), verificar que el hash del archivo descargado coincida con el hash publicado en el repositorio oficial antes de instalar.
- No modificar skills existentes sin confirmación del usuario de que desea sobreescribir.
